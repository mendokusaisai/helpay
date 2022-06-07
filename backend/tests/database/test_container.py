import pytest
from google.cloud import datastore

from database.container import Container
from database.database import Database
from database.member import Member

DEFAULT_CONTAINER_LENGTH = 3


@pytest.fixture
def container() -> Container:
    members = [Member(datastore.Entity(Database.client.key("test"))) for _ in range(DEFAULT_CONTAINER_LENGTH)]
    for member in members:
        member.put(True)
    container = Container(members)
    return container


def test_len(db, container: Container):
    assert DEFAULT_CONTAINER_LENGTH == len(container)


def test_iter(db, container: Container):
    assert DEFAULT_CONTAINER_LENGTH == len(list(container))


def test_get(db, container: Container):
    _entity = container._entities[1]
    result = container.get(_entity.id)
    assert _entity == result


def test_append(db, container: Container):
    new_entity = Member(datastore.Entity(Database.client.key("test")))
    container.append(new_entity)
    assert DEFAULT_CONTAINER_LENGTH + 1 == len(container)


def test_remove(db, container: Container):
    delete_entity = container._entities[1]
    container.remove(delete_entity)
    assert DEFAULT_CONTAINER_LENGTH - 1 == len(container)


def test_copy(db, container: Container):
    copied = container.copy()
    assert copied == container._entities
