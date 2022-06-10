import os
from typing import Optional

from google.cloud import datastore
from log import logger


class Database(object):
    namespace: str = ""
    if "DATASTORE_NAMESPACE" in os.environ.keys():
        namespace: str = os.environ["DATASTORE_NAMESPACE"]
    client: datastore.Client = datastore.Client(namespace=namespace)
    logger.info("Database namespace set to default")

    @classmethod
    def set_namespace(cls, namespace:str):
        logger.info(f"namespace={namespace}")
        cls.namespace = namespace
        cls.client = datastore.Client(namespace=namespace)

    @classmethod
    def put(cls, e: datastore.Entity) -> None:
        cls.client.put(e)

    @classmethod
    def get_by_id(cls, kind: str, _id: int) -> Optional[datastore.Entity]:
        return cls.client.get(cls.client.key(kind, _id))

    @classmethod
    def delete(cls, kind: str, _id: int) -> None:
        cls.client.delete(cls.client.key(kind, int(_id)))

    @classmethod
    def clear(cls) -> None:
        query = cls.client.query(namespace=cls.namespace)
        keys = [entity.key for entity in query.fetch()]
        cls.client.delete_multi(keys)
