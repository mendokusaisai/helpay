from google.cloud import datastore
from log import logger

from database.card import Card
from database.container import T_ENTITY, Container
from database.database import Database
from database.member import Member
from database.table import Table


class CardTable(Table):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(CardTable, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        super().__init__(self.get_all_cards())

    def create_card(self) -> Card:
        _entity = datastore.Entity(Database.client.key("Card"))
        _entity["name"] = ""
        _entity["point"] = 0
        _entity["targets"] = []
        card = Card(_entity)
        card.put(force=True)
        self.entities.append(card)
        return card

    def get_all_cards(self) -> Container:
        query = Database.client.query(kind="Card")
        self.entities = Container([Card(entity) for entity in query.fetch()])
        query = Database.client.query(kind="Member")
        members = Container([Member(entity) for entity in query.fetch()])
        for entity in self.entities:
            entity.targets = [members.get(target_id).to_dict() for target_id in entity.targets]

        return self.entities

    def search_card(self, _id: int) -> T_ENTITY:
        if not isinstance(_id, int):
            _id = int(_id)
        return self.entities.get(_id)

    def delete_card(self, _id: int) -> None:
        if not isinstance(_id, int):
            _id = int(_id)
        for card in self.entities.copy():
            if card.id == _id:
                card.delete()
                self.entities.remove(card)
