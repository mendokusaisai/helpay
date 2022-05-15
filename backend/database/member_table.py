from typing import Optional

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
        super().__init__()
        self.members = self.get_all_members()

    def get_all_members(self) -> Container:
        query = Database.client.query(kind="Member")
        for ent in query.fetch():
            logger.debug(ent)
        self.members = Container([Member(entity) for entity in query.fetch()])
        return self.members

    def search_member(self, _id: int) -> Optional[T_ENTITY]:
        return self.members.get(_id)
