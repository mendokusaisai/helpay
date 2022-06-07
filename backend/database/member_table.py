from typing import Optional

from google.cloud import datastore
from log import logger

from database.container import T_ENTITY, Container
from database.database import Database
from database.member import Member
from database.table import Table


class MemberTable(Table):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(MemberTable, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        super().__init__(self.get_all_members())

    def create_member(self) -> Member:
        _entity = datastore.Entity(Database.client.key("Member"))
        _entity["name"] = ""
        _entity["point"] = 0
        card = Member(_entity)
        card.put(force=True)
        self.entities.append(card)
        return card

    def get_all_members(self) -> Container:
        query = Database.client.query(kind="Member")
        for ent in query.fetch():
            logger.debug(ent)
        self.entities = Container([Member(entity) for entity in query.fetch()])
        return self.entities

    def search_member(self, _id: int) -> Optional[T_ENTITY]:
        return self.entities.get(_id)

    def delete_member(self, _id: int) -> None:
        if not isinstance(_id, int):
            _id = int(_id)
        for member in self.entities.copy():
            if member.id == _id:
                member.delete()
                self.entities.remove(member)
