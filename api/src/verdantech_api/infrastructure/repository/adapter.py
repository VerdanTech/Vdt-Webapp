from typing import Dict, List, Type
from abc import abstractstaticmethod
from litestar.contrib.mongodb_motor._async import (
    MongoDbMotorAsyncRepository,
    DocumentType,
)

from serpyco import SerpycoSerializer

from src.verdantech_api.domain.utils.sanitizers.object import ObjectSanitizer
from src.verdantech_api.domain.utils.sanitizers.sanitization.generic import (
    SanitizationT,
)
from src.verdantech_api.domain.models.common import Entity


class ModelAdapter:
    @abstractstaticmethod
    def to_document(
        model: Entity,
        serializer: AbstractSerializer,
        sanitizer: ObjectSanitizer,
        disabled_fields: Dict[str, List[Type[SanitizationT]] | None] | None,
        many: bool = False
    ) -> DocumentType:
        """Serialize the domain entity to a dictionary, after sanitization

        Args:
            model (Entity): the model to serialize
            serializer (AbstractSerializer): serializer class
            sanitizer (ObjectSanitizer): sanitizer class
            disabled_fields (Dict[str, List[Type[SanitizationT]]  |  None] | None):
                keys are field names to skip sanitization on, and values are a
                list of sanitization types to skip sanitization on that field,
                or None if all sanitizations are to be skipped

        Returns:
            DocumentType: the model represented as dict
        """
        ...

    @abstractstaticmethod
    def from_document(document: DocumentType, serializer: AbstractSerializer, many: bool = False) -> Entity:
        """Deserialize the dictionary into a domain entity

        Args:
            document (DocumentType): the dictionary to serialize
            serializer (AbstractSerializer): serializer class

        Returns:
            Entity: the domain entity
        """
        ...

    @abstractstaticmethod
    def entity_fields_to_kwargs() -> Dict[str, Any]:
        ...


class SerpycoModelAdapter(ModelAdapter):
    @staticmethod
    def to_document(
        entity: List[Entity],
        serializer: AbstractSerializer,
        sanitizer: ObjectSanitizer,
        disabled_fields: Dict[str, List[Type[SanitizationT]] | None] | None,
        many: bool = False
    ) -> DocumentType:
        # sanitize
        pass

    @staticmethod
    def from_document(document: DocumentType, serializer: AbstractSerializer, many: bool = False) -> Entity:
        pass


class EntityMongoAsyncRepository(MongoDbMotorAsyncRepository):
    """Modify the stock mongodb repository to accept domain models"""

    entity: List[Entity]
    serializer: AbstractSerializer
    disabled_fields: Dict[str, List[Type[SanitizationT]] | None] | None

    def __init__(
        self,
        sanitizer: ObjectSanitizer,
        adapter: ModelAdapter,
        collection: AsyncIOMotorCollection,
        **kwargs: Any,
    ) -> None:
        super().__init__(collection=collection, **kwargs)
        self.sanitizer = sanitizer
        self.adapter = adapter

    def _to_document(self, entity: Entity, many: bool = False):
        return self.adapter.to_document(
            entity=entity,
            serializer=self.serializer,
            sanitizer=self.sanitizer,
            disabled_fields=self.disabled_fields,
            many=many
        )
    
    def _from_document(self, document: DocumentType, many: bool = False):
        return self.adapter.from_document(document=document, serializer=self.serializer, many=many)

    async def add(self, data: Entity) -> Entity:
        document = self._to_document(entity=data)
        document = await super().add(data=document)
        return self._from_document(document=document)

    async def add_many(self, data: List[Entity]) -> List[Entity]:
        document = self._to_document(entity=data, many=True)
        document = await super().add_many(data=document)
        return self._from_document(document=document, many=True)

    async def count(
        self,
        *filters: FilterTypes,
        **kwargs: Any,
    ) -> int:
        """Count the number of documents in the collection matching the filters.

        Args:
            *filters: Filters to apply to the collection.
            **kwargs: Additional keyword arguments to filter the collection.

        Returns:
            The number of documents in the collection matching the filters.
        """

        query = self._build_query_from_filters(*filters)
        query.update(kwargs)
        return cast(int, await self.collection.count_documents(query))

    async def delete(self, item_id: Any) -> DocumentType:
        """Delete instance identified by ``item_id``.

        Args:
            item_id: Identifier of instance to be deleted.

        Returns:
            The deleted instance.

        Raises:
            NotFoundError: If no instance found identified by ``item_id``.
        """
        with wrap_pymongo_exception():
            document = await self.collection.find_one_and_delete(
                {self.id_attribute: item_id}
            )
            self.check_not_found(document)
            return cast(DocumentType, document)

    async def delete_many(self, item_ids: list[Any]) -> list[DocumentType]:
        """Delete instance identified by ``item_id``.

        Args:
            item_ids: Identifier of instance to be deleted.

        Returns:
            The deleted instances.

        """
        with wrap_pymongo_exception():
            documents_to_delete = await self.collection.find(
                {self.id_attribute: {"$in": item_ids}}
            ).to_list(None)
            await self.collection.delete_many({self.id_attribute: {"$in": item_ids}})
            return cast(List[DocumentType], documents_to_delete)

    async def exists(self, **kwargs: Any) -> bool:
        """Return true if the object specified by ``kwargs`` exists.

        Args:
            **kwargs: Identifier of the instance to be retrieved.

        Returns:
            True if the instance was found. False if not found.

        """
        existing = await self.count(**kwargs)
        return existing > 0

    async def get(self, item_id: Any, **kwargs: Any) -> DocumentType:
        """Get instance identified by ``item_id``.

        Args:
            item_id: Identifier of the instance to be retrieved.
            **kwargs: Additional parameters

        Returns:
            The retrieved instance.

        Raises:
            NotFoundError: If no instance found identified by ``item_id``.
        """
        with wrap_pymongo_exception():
            document = await self.collection.find_one(
                {self.id_attribute: item_id, **kwargs}
            )
            self.check_not_found(document)
            return cast(DocumentType, document)

    async def get_one(self, **kwargs: Any) -> DocumentType:
        """Get instance identified by ``kwargs``.

        Args:
            **kwargs: Identifier of the instance to be retrieved.

        Returns:
            The retrieved instance.

        Raises:
            NotFoundError: If no instance found identified by `item_id`.
        """
        with wrap_pymongo_exception():
            document = await self.collection.find_one(kwargs)
            self.check_not_found(document)
            return cast(DocumentType, document)

    async def get_or_create(
        self,
        match_fields: list[str] | str | None = None,
        upsert: bool = True,
        **kwargs: Any,
    ) -> tuple[DocumentType, bool]:
        """Get instance identified by ``kwargs`` or create if it doesn't exist.

        Args:
            match_fields: a list of keys to use to match the existing model.  When empty, all fields are matched.
            upsert: When using match_fields and actual model values differ from `kwargs`, perform an update operation on the model.
            **kwargs: Identifier of the instance to be retrieved.

        Returns:
            a tuple that includes the instance and whether it was newly created.
        """
        if isinstance(match_fields, str):
            match_fields = [match_fields]
        # KeyError is expected to be thrown if a match_field is not in field_values, not sure if this is the best way to handle this
        # Could also do a ".get" and then check for None but not sure if that is better since it would be a silent failure
        match_filter = (
            kwargs if match_fields is None else {k: kwargs[k] for k in match_fields}
        )

        doc = await self.get_one_or_none(**match_filter)

        if doc is None:
            doc = self.model_type(kwargs)
            c = await self.add(doc)
            return c, True

        if upsert:
            update = {"$set": kwargs}
            with wrap_pymongo_exception():
                return (
                    await self.collection.find_one_and_update(
                        doc, update, return_document=ReturnDocument.AFTER
                    ),
                    False,
                )
        return doc, False

    async def get_one_or_none(self, **kwargs: Any) -> DocumentType | None:
        """Get instance identified by ``kwargs`` or None if not found.

        Args:
            **kwargs: Identifier of the instance to be retrieved.

        Returns:
            The retrieved instance or None
        """
        with wrap_pymongo_exception():
            return cast(Optional[DocumentType], await self.collection.find_one(kwargs))

    async def update(self, data: DocumentType) -> DocumentType:
        """Update instance with the attribute values present on ``data``.

        Args:
            data: An instance that should have a value for `self.id_attribute` that exists in the
                collection.

        Returns:
            The updated instance.

        Raises:
            NotFoundError: If no instance found with same identifier as ``data``.
        """
        with wrap_pymongo_exception():
            result = await self.collection.find_one_and_update(
                {self.id_attribute: self.get_id_attribute_value(data)},
                {"$set": data},
                return_document=ReturnDocument.AFTER,
            )
            self.check_not_found(result)
            return cast(DocumentType, result)

    async def update_many(self, data: list[DocumentType]) -> list[DocumentType]:
        """Update one or more instances with the attribute values present on ``data``.

        Args:
            data: A list of documents to update.  Each should have a value for `self.id_attribute` that exists in the
                collection.

        Returns:
            The updated instances.

        Raises:
            NotFoundError: If no instance found with same identifier as `data`.
        """

        bulk_operations = []

        for instance_data in data:
            _id = self.get_id_attribute_value(instance_data)
            bulk_operations.append(UpdateOne({"_id": _id}, {"$set": instance_data}))

        with wrap_pymongo_exception():
            result = await self.collection.bulk_write(bulk_operations)

            if result.matched_count != len(data):
                raise NotFoundError(
                    f"Some instances were not found and updated. Total data: {len(data)}, Matched: {result.matched_count}"
                )

            return data

    async def upsert(self, data: DocumentType) -> DocumentType:
        """Update or create instance.

        Updates instance with the attribute values present on `data`, or creates a new instance if
        one doesn't exist.

        Args:
            data: Instance to update existing, or be created. Identifier used to determine if an
                existing instance exists is the value of an attribute on `data` named as value of
                `self.id_attribute`.

        Returns:
            The updated or created instance.
        """
        _id = self.get_id_attribute_value(data)

        with wrap_pymongo_exception():
            document = await self.collection.find_one_and_update(
                {"_id": data["_id"]},
                {"$set": data},
                return_document=ReturnDocument.AFTER,
            )
            return cast(DocumentType, document)

    async def list_and_count(
        self, *filters: FilterTypes, **kwargs: Any
    ) -> tuple[list[DocumentType], int]:
        """List records with total count.

        Args:
            *filters: Types for specific filtering operations.
            **kwargs: Instance attribute value filters.

        Returns:
            Count of records returned by query, ignoring pagination.
        """
        query = self._build_query_from_filters(*filters)
        query.update(kwargs)

        with wrap_pymongo_exception():
            cursor = self.collection.find(query)
            docs = await cursor.to_list(length=None)
            return docs, len(docs)

    async def list(self, *filters: FilterTypes, **kwargs: Any) -> list[DocumentType]:
        """Get a list of instances, optionally filtered.

        Args:
            *filters: Types for specific filtering operations.
            **kwargs: Instance attribute value filters.

        Returns:
            The list of instances, after filtering applied.
        """
        query = self._build_query_from_filters(*filters)
        query.update(kwargs)

        with wrap_pymongo_exception():
            cursor = self.collection.find(query)
            return cast(List[DocumentType], await cursor.to_list(length=None))
