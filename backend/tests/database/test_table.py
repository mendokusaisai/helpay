from google.cloud import datastore

from database.card import Card
from database.container import Container
from database.database import Database
from database.table import Table

KIND = "test"


def test_save_all():
    _entities = [Card(datastore.Entity(Database.client.key(KIND))) for _ in range(5)]
    for entity in _entities:
        entity._entity["name"] = ""
        entity.name = "a"
    container = Container(_entities)
    table = Table(container)
    table.save_all()

    query = Database.client.query(kind="test")
    _get_entities = [Card(entity) for entity in query.fetch()]
    assert 5 == len(_get_entities)
