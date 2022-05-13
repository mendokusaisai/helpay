from google.cloud import datastore
from log import logger

from database.database import Database


class Entity:
    def __init__(self, entity: datastore.Entity) -> None:
        self._entity = entity
        self._is_dirty = False

    def put(self):
        if self._is_dirty:
            Database.put(self._entuty)

    def to_dict(self) -> dict:
        dict_entity = {"id": self._entity.key.id}
        dict_entity.update(self._entity)

        return dict_entity
