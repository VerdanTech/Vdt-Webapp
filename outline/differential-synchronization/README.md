# The Differential Synchronization Feature Category

The Differential Synchronization algorithm is used to synchronize the document state of multiple clients. Instead of saving new data directly to the database, data should pass through an in-memory storage layer which collects the documents of all clients, executes the synchronization, and writes to the database only when a synchronized state is obtained. The in-memory layer is implemented with Redis on the backend.

For resources on differential synchronization, see these two documents:
- [Differential Synchronization by Neil Fraser, 2009](https://neil.fraser.name/writing/sync/)
- [Differential Synchronization with JSON Patch, 2021](https://saswat.dev/differential-synchronization-with-json-patch/)