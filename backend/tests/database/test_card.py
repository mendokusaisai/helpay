from google.cloud import datastore

from database.card import Card
from database.database import Database
from database.member import Member

KIND = "test"


def test_name():
    _entity = datastore.Entity(Database.client.key(KIND))
    _entity["name"] = ""
    card = Card(_entity)
    card.name = "name_test"
    assert "name_test" == card.name
    assert "name_test" == card._entity["name"]


def test_point():
    _entity = datastore.Entity(Database.client.key(KIND))
    _entity["point"] = 0
    card = Card(_entity)
    card.point = 10
    assert 10 == card.point
    assert 10 == card._entity["point"]


def test_target():
    _entity_member = datastore.Entity(Database.client.key(KIND))
    _member = Member(_entity_member)

    _entity_card = datastore.Entity(Database.client.key(KIND))
    _entity_card["targets"] = []
    card = Card(_entity_card)
    card.targets = [_member]
    assert [_member] == card.targets
    assert [_member] == card._entity["targets"]


def test_target_put(db):
    _entity_member = datastore.Entity(Database.client.key("member"))
    _member = Member(_entity_member)
    _member.put(True)

    _entity_card = datastore.Entity(Database.client.key(KIND))
    _entity_card["targets"] = []
    card = Card(_entity_card)
    card.targets = [_member.id]

    assert card._is_dirty
    card.put()
    assert not card._is_dirty
