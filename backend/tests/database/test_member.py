from google.cloud import datastore

from database.database import Database
from database.member import Member

KIND = "test"


def test_name():
    _entity = datastore.Entity(Database.client.key(KIND))
    _entity["name"] = ""
    member = Member(_entity)
    member.name = "name_test"
    assert "name_test" == member.name
    assert "name_test" == member._entity["name"]


def test_point():
    _entity = datastore.Entity(Database.client.key(KIND))
    _entity["point"] = 0
    member = Member(_entity)
    member.point = 10
    assert 10 == member.point
    assert 10 == member._entity["point"]
