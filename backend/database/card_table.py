from typing import Optional

from google.cloud import datastore
from log import logger

from database.card import Card
from database.container import T_ENTITY, Container
from database.database import Database
from database.table import Table


class CardTable(Table):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(CardTable, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        super().__init__()
        self.cards = self.get_all_cards()

    def create_card(self) -> Card:
        _entity = datastore.Entity(Database.client.key("Card"))
        _entity["name"] = ""
        _entity["point"] = 0
        _entity["targets"] = []
        card = Card(_entity)
        card.put(force=True)
        self.cards.append(card)
        return card

    def get_all_cards(self) -> Container:
        query = Database.client.query(kind="Card")
        for ent in query.fetch():
            logger.debug(ent)
        self.cards = Container([Card(entity) for entity in query.fetch()])
        return self.cards

    def search_card(self, _id: int) -> Optional[T_ENTITY]:
        return self.cards.get(_id)

    def update_card(self, card: datastore.Entity) -> None:
        pass

    def delete_card(self, _id: int) -> None:
        for card in self.cards.copy():
            if card.id == _id:
                card.delete()
                self.cards.remove(card)
