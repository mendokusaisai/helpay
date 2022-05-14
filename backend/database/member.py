from google.cloud import datastore

from database.database import Database
from database.entity import Entity


class Member(Entity):
    def __init__(self, entity: datastore.Entity) -> None:
        super().__init__(entity, type="Member")
