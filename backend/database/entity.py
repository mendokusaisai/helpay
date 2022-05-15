from google.cloud import datastore

from database.database import Database


class Entity:
    def __init__(self, entity: datastore.Entity, type: str) -> None:
        self._entity = entity
        self.type = type
        self._is_dirty = False

    def put(self, force=False):
        if self._is_dirty or force:
            Database.put(self._entity)

    def delete(self):
        Database.delete(self.type, self.id)

    def to_dict(self) -> dict:
        dict_entity = {"id": self.id}
        dict_entity.update(self._entity)

        return dict_entity

    @property
    def id(self) -> int:
        return self._entity.id
