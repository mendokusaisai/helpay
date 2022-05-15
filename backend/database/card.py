from google.cloud import datastore

from database.entity import Entity
from database.member import Member


class Card(Entity):
    def __init__(self, entity: datastore.Entity) -> None:
        super().__init__(entity, type="Card")

    @property
    def name(self) -> str:
        return self._entity["name"]

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            value = str(value)
        if self._entity["name"] != value:
            self._entity["name"] = value
            self._is_dirty = True

    @property
    def point(self) -> int:
        return self._entity["point"]

    @point.setter
    def point(self, value: int) -> None:
        if not isinstance(value, int):
            value = int(value)
        if self._entity["point"] != value:
            self._entity["point"] = value
            self._is_dirty = True

    @property
    def targets(self) -> list[Member]:
        return self._entity["targets"]

    @targets.setter
    def targets(self, value: list[Member]) -> None:
        _targets = self.to_dict()["targets"]
        if set(_targets) != set(value):
            self._entity["targets"] = value
            self._is_dirty = True
