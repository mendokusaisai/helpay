from google.cloud import datastore

from database.entity import Entity


class Member(Entity):
    def __init__(self, entity: datastore.Entity) -> None:
        super().__init__(entity, type="Member")

    @property
    def name(self) -> str:
        return self._entity["name"]

    @name.setter
    def name(self, value: str) -> None:
        if self._entity["name"] != value:
            self._entity["name"] = value
            self._is_dirty = True

    @property
    def point(self) -> int:
        return self._entity["point"]

    @point.setter
    def point(self, value: int) -> None:
        if self._entity["point"] != value:
            self._entity["point"] = value
            self._is_dirty = True
