from google.cloud import datastore

from database.database import Database

KIND = "test"


def test_put(db):
    entity = datastore.Entity(Database.client.key(KIND))
    assert entity.id is None
    Database.put(entity)
    assert Database.namespace == "PYTEST"
    assert entity.id is not None


def test_get_by_id(db):
    entity = datastore.Entity(Database.client.key(KIND))
    Database.put(entity)
    assert entity == Database.get_by_id(KIND, entity.id)


def test_delete(db):
    entity = datastore.Entity(Database.client.key(KIND))
    Database.put(entity)
    assert entity == Database.get_by_id(KIND, entity.id)
    Database.delete(KIND, entity.id)
    assert None is Database.get_by_id(KIND, entity.id)
