import os
from typing import Optional

from google.cloud import datastore
from log import logger


class Database(object):
    namespace: str = os.environ["DATASTORE_NAMESPACE"]
    logger.info(f"namespace={namespace}")
    client = datastore.Client(namespace=namespace)

    @classmethod
    def put(cls, e: datastore.Entity) -> None:
        cls.client.put(e)

    @classmethod
    def get_by_id(cls, kind: str, _id: int) -> Optional[datastore.Entity]:
        return cls.client.get(cls.client.key(kind, _id))

    @classmethod
    def get_by_name(cls, kind: str, name: str) -> Optional[datastore.Entity]:
        return cls.client.get(cls.client.key(kind, name))

    @classmethod
    def create_by_id(
        cls, kind: str, _id: Optional[int] = None
    ) -> Optional[datastore.Entity]:
        if _id is None:
            return datastore.Entity(cls.client.key(kind))
        elif cls.get_by_id(kind, _id) is not None:
            logger.debug(f"createByName(): Entity({kind},{id}) is already exist.")
            return None
        return datastore.Entity(cls.client.key(kind, _id))

    @classmethod
    def create_by_name(cls, kind: str, name: str) -> Optional[datastore.Entity]:
        if cls.get_by_name(kind, name) is not None:
            logger.debug(f"createByName(): Entity({kind},{name}) is already exist.")
            return None
        return datastore.Entity(cls.client.key(kind, name))

    @classmethod
    def create_user(cls, _id: str) -> datastore.Entity:
        return datastore.Entity(cls.client.key("User", _id))

    @classmethod
    def get_user(cls, _id: str) -> datastore.Entity:
        return cls.client.get(cls.client.key("User", _id))

    @classmethod
    def get_users(cls, ids: list[str]) -> list[datastore.Entity]:
        keys = [cls.client.key("User", v) for v in ids]
        return cls.client.get_multi(keys)

    @classmethod
    def delete(cls, kind: str, _id: int) -> None:
        cls.client.delete(cls.client.key(kind, int(_id)))
