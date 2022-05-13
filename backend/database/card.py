from google.cloud import datastore

from database.entity import Entity


class Card(Entity):
    def __init__(self, entity: datastore.Entity) -> None:
        super().__init__(entity)

    def delete(self):
        pass
