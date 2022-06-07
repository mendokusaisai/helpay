import pytest
from google.cloud import datastore

from database.database import Database
from database.entity import Entity


@pytest.fixture
def entity(db) -> Entity:
    _datastore_entity = datastore.Entity(Database.client.key("test"))
    _datastore_entity["name"] = "aa"
    _entity = Entity(_datastore_entity, "test")
    _entity.put(True)
    return _entity


def test_put(db):
    _entity = datastore.Entity(Database.client.key("test"))
    entity = Entity(_entity, "test")
    entity.put()
    assert _entity.id is None
    entity.put(True)
    assert _entity.id is not None


def test_delete(entity: Entity):
    _id = entity.id
    entity.delete()
    assert Database.get_by_id("test", _id) is None


def test_to_dict(entity: Entity):
    expect = {"id": entity.id, "name": "aa"}
    assert expect == entity.to_dict()


def test_id(entity: Entity):
    assert entity.id == entity._entity.id
