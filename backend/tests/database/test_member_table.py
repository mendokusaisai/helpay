import pytest

from database.member_table import MemberTable


def test_create_member(db):
    table = MemberTable()
    assert 0 == len(table.entities)
    table.create_member()
    assert 1 == len(table.entities)


def test_get_all_members(db):
    table = MemberTable()
    assert 0 == len(table.entities)
    table.create_member()
    table.create_member()
    ret = table.get_all_members()
    assert 2 == len(table.entities)
    assert 2 == len(ret)


def test_search_member(db):
    table = MemberTable()
    with pytest.raises(KeyError):
        table.search_member(1)
    member = table.create_member()
    searched = table.search_member(member.id)
    assert member.id == searched.id


def test_delete_member(db):
    table = MemberTable()
    table.create_member()
    member = table.create_member()
    assert 2 == len(table.entities)
    table.delete_member(member.id)
    assert 1 == len(table.entities)
    with pytest.raises(KeyError):
        table.search_member(member.id)
