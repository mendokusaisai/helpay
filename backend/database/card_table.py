from google.cloud import datastore
from log import logger

from database.card import Card
from database.database import Database
from database.table import Table


class CardTable(Table):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def create_card(cls) -> datastore.Entity:
        return datastore.Entity(Database.client.key("Card"))

    @classmethod
    def get_all_cards(cls) -> list[Card]:
        query = Database.client.query(kind="Card")
        for ent in query.fetch():
            logger.debug(ent)
        return [Card(entity) for entity in query.fetch()]

    @classmethod
    def update_card(cls, card: datastore.Entity) -> None:
        pass

    @classmethod
    def get_card(cls, _id: str) -> datastore.Entity:
        return Database.client.get(Database.client.key("Card", _id))

    @classmethod
    def get_cards(cls, ids: list[str]) -> list[datastore.Entity]:
        keys = [Database.client.key("Card", v) for v in ids]
        return Database.client.get_multi(keys)

    @classmethod
    def delete_card(cls, _id: int) -> None:
        Database.delete("Card", _id)
