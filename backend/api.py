from flask import Blueprint, request
from flask_restful import Api, Resource

from database.card import Card
from database.card_table import CardTable
from database.member_table import MemberTable
from log import logger

api_bp = Blueprint("api", __name__, url_prefix="/api")


class Cards(Resource):
    def get(self) -> list[dict]:
        """
        すべてのカード情報を取得する
        json文字列に変換する
        """
        _table = CardTable()
        all_cards = _table.get_all_cards()
        all_cards_dict = [card.to_dict() for card in all_cards]
        return all_cards_dict


class DeleteCard(Resource):
    def post(self) -> bool:
        payload = request.json
        if payload is None:
            return False
        _table = CardTable()
        _table.delete_card(payload["id"])
        return True


class NewCards(Resource):
    def get(self):
        _card_table = CardTable()
        new_card = _card_table.create_card()
        logger.debug(f"new_card : {new_card}")
        return new_card.to_dict()


class SaveCards(Resource):
    def post(self):
        payload = request.json
        if payload is None:
            return
        card_table = CardTable()
        member_table = MemberTable()
        for card_json in payload:
            logger.info(card_json)
            target_card: Card = card_table.search_card(card_json["id"])
            target_card.name = card_json["name"]
            target_card.point = card_json["point"]
            # Member保存
            _targets = [member_table.search_member(_id) for _id in card_json["targets"]]
            target_card.targets = _targets
        card_table.save_all()


class Members(Resource):
    def get(self):
        return [
            {"id": 1, "name": "taro", "point": 1000},
            {"id": 2, "name": "hanako", "point": 500},
        ]


api = Api(api_bp)
api.add_resource(Cards, "/cards/")
api.add_resource(DeleteCard, "/cards/delete/")
api.add_resource(NewCards, "/cards/new/")
api.add_resource(SaveCards, "/cards/save/")
api.add_resource(Members, "/members/")
