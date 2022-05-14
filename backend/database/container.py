from typing import Generic, Optional, TypeVar

from database.entity import Entity

T_ENTITY = TypeVar("T_ENTITY", bound=Entity)


class Container(Generic[T_ENTITY]):
    def __init__(self, entities: list[T_ENTITY]) -> None:
        self._entities: list[T_ENTITY] = entities

    def __iter__(self):
        self._cnt = 0
        return self

    def __next__(self):
        if self._cnt > len(self._entities) - 1:
            raise StopIteration
        result = self._entities[self._cnt]
        self._cnt += 1
        return result

    def get(self, _id: int) -> Optional[T_ENTITY]:
        for entity in self._entities:
            if entity.id == _id:
                return entity
        return None

    def append(self, entity: T_ENTITY) -> None:
        self._entities.append(entity)

    def remove(self, entity: T_ENTITY) -> None:
        self._entities.remove(entity)

    def copy(self) -> list[T_ENTITY]:
        return self._entities[:]
