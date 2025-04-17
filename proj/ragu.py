import chromadb


class ChromaDBClient:
    def __init__(self, collection_name: str, embedding_function: callable):
        """
        Initialize ChromaDB client and create a collection
        """
        self.client = chromadb.Client()
        self.collection_name = collection_name
        self.embedding_function = embedding_function

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_function
        )

    def add_documents(self, documents: list):
        """
        Add documents to the collection
        """
        self.collection.add(
            ids=[doc["id"] for doc in documents],
            documents=[doc["text"] for doc in documents],
            metadatas=[doc["metadata"] for doc in documents]
        )


