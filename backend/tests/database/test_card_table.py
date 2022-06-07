import pytest

from database.card_table import CardTable


def test_create_card(db):
    table = CardTable()
    assert 0 == len(table.entities)
    table.create_card()
    assert 1 == len(table.entities)


def test_get_all_cards(db):
    table = CardTable()
    assert 0 == len(table.entities)
    table.create_card()
    table.create_card()
    ret = table.get_all_cards()
    assert 2 == len(table.entities)
    assert 2 == len(ret)


def test_search_card(db):
    table = CardTable()
    with pytest.raises(KeyError):
        table.search_card(1)
    card = table.create_card()
    searched = table.search_card(card.id)
    assert card.id == searched.id


def test_delete_card(db):
    table = CardTable()
    table.create_card()
    card = table.create_card()
    assert 2 == len(table.entities)
    table.delete_card(card.id)
    assert 1 == len(table.entities)
    with pytest.raises(KeyError):
        table.search_card(card.id)
