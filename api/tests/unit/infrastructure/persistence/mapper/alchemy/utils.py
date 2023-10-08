from dataclasses import asdict, is_dataclass
from typing import Any, Dict, List, Set, Union

from src.verdantech_api.domain.models.common.entities import RootEntity
from src.verdantech_api.infrastructure.persistence.mapper.alchemy.model import (
    BaseAlchemyModel,
)


def assert_equivalent_models(
    model1: BaseAlchemyModel,
    model2: BaseAlchemyModel,
) -> None:
    """Given two sqlalchemy models, compare their attributes such that
        two models are equivalent if all attributes excluding their
        SQLAlchemy instance attribute (_sa_instance_state) are
        equivalent. This is useful in tests because we can create an
        expected_model and compare it against the result of a mapping
        operation of a domain model.

    Args:
        model1 (BaseAlchemyModel): first model to compare
        model2 (BaseAlchemyModel): second model to compare

    Raises:
        AssertionError: if models are unequal
    """
    # Keep track of attributes that have been compared
    visited_attrs = set()
    visited_attrs.add(id(model1))

    def remove_instance_attr(model: BaseAlchemyModel) -> Dict[str, Any]:
        """Remove the attribute SQLAlchemy uses to keep track of seperate
            instances of the same model, so that we can treat two models
            as equal if they have are different instances with the same
            attributes

        Args:
            model (BaseAlchemyModel): the model to strip instance
                attribute from

        Returns:
            Dict[str, Any]: the model in dictionary form
        """
        return {
            key: value
            for key, value in model.__dict__.items()
            if key != "_sa_instance_state"
        }

    def recursive_compare(
        dict1: Dict[str, Any],
        dict2: Dict[str, Any],
        depth: int,
        visited_attrs: Set[int],
    ) -> bool:
        """Recursively compare two models in dictionary form.
            If any child attributes are themselves SQLAlchemy models,
            apply the same instance-attribute removal and comparison.

        Args:
            dict1 (Dict[str, Any]): first model in dict form
            dict2 (Dict[str, Any]): second model in dict form
            depth (int): current depth of recursive traversal
            visited_attrs (Set[int]): list of IDs of attributes
                that have already been visited

        Returns:
            bool: the result of the comparison
        """
        # Cap comparison if depth goes too far
        if depth > 50:
            raise RecursionError("Max depth exceeded")

        # False if the key structures don't match
        if set(dict1.keys()) != set(dict2.keys()):
            return False

        for key1, value1 in dict1.items():
            print(f"VISITED_ATTRIBUTES: {visited_attrs}")
            # Continue if attribute has already been visited
            if id(value1) in visited_attrs:
                print(f"VISITED_ATTRIBUTES: triggered")
                continue

            key2 = key1
            value2 = dict2[key2]

            print(f"Model1: {key1}:{value1}")
            print(f"Model2: {key2}:{value2}")

            # If attribute is a list, recurse with each
            # member of the list
            # TODO: expand typing here to cover all applicable iterables
            if isinstance(value1, Union[List, Set]):
                visited_attrs.add(id(value1))
                if len(value1) != len(value2):
                    return False
                for item1, item2 in zip(value1, value2):
                    if not recursive_compare(
                        remove_instance_attr(item1),
                        remove_instance_attr(item2),
                        depth + 1,
                        visited_attrs,
                    ):
                        return False

            # If attribute is a SQLAlchemy model, recurse comparison
            elif isinstance(value1, BaseAlchemyModel):
                visited_attrs.add(id(value1))
                if not recursive_compare(
                    remove_instance_attr(value1),
                    remove_instance_attr(value2),
                    depth + 1,
                    visited_attrs,
                ):
                    return False

            # If attribute is neither a list nor a SQLAlchemy model,
            # compare normally
            else:
                if value1 != value2:
                    return False
        return True

    assert (
        recursive_compare(
            remove_instance_attr(model1),
            remove_instance_attr(model2),
            depth=0,
            visited_attrs=visited_attrs,
        )
        is True
    )


def assert_equivalent_entities(entity1: RootEntity, entity2: RootEntity) -> None:
    """Given two domain entities, compare their attributes such that
        two models are equivalent if all attributes excluding their
        are equivalent. This is useful in tests because we can create an
        expected_model and compare it against the result of a mapping
        operation of a database representation.

    Args:
        model1 (RootEntity): first entity to compare
        model2 (RootEntity): second entity to compare

    Raises:
        AssertionError: if entities are unequal
    """

    # Keep track of attributes that have been compared
    visited_attrs = set()
    visited_attrs.add(id(entity1))

    def recursive_compare(
        dict1: Dict[str, Any],
        dict2: Dict[str, Any],
        depth: int,
        visited_attrs: Set[int],
    ) -> bool:
        """Recursively compare two entities in dictionary form.
            If any child attributes are themselves dataclasses/entities,
            apply the same recursive comparison.

        Args:
            dict1 (Dict[str, Any]): first entity in dict form
            dict2 (Dict[str, Any]): second entity in dict form
            depth (int): current depth of recursive traversal
            visited_attrs (Set[int]): list of IDs of attributes
                that have already been visited

        Returns:
            bool: the result of the comparison
        """
        
        # Cap comparison if depth goes too far
        if depth > 50:
            raise RecursionError("Max depth exceeded")

        # False if the key structures don't match
        if set(dict1.keys()) != set(dict2.keys()):
            return False

        for key1, value1 in dict1.items():
            print(f"VISITED_ATTRIBUTES: {visited_attrs}")
            # Continue if attribute has already been visited
            if id(value1) in visited_attrs:
                print(f"VISITED_ATTRIBUTES: triggered")
                continue

            key2 = key1
            value2 = dict2[key2]
            print(f"Entity1: {key1}:{value1}")
            print(f"Entity2: {key2}:{value2}")

            # If attribute is a list, recurse with each
            # member of the list
            # TODO: expand typing here to cover all applicable iterables
            if isinstance(value1, Union[List, Set]):
                visited_attrs.add(id(value1))
                if len(value1) != len(value2):
                    return False
                for item1, item2 in zip(value1, value2):
                    if not recursive_compare(
                        asdict(item1) if is_dataclass(item1) else item1,
                        asdict(item2) if is_dataclass(item2) else item2,
                        depth + 1,
                        visited_attrs,
                    ):
                        return False

            # If attribute is a dataclass (entity), recurse comparison
            elif is_dataclass(value1):
                visited_attrs.add(id(value1))
                if not recursive_compare(
                    asdict(value1), asdict(value2), depth + 1, visited_attrs
                ):
                    return False

            # If a  ttribute is neither a list nor a dataclass,
            # compare normally
            else:
                if value1 != value2:
                    return False

        return True

    assert recursive_compare(asdict(entity1), asdict(entity2), 0, visited_attrs)
