from flask import Blueprint, request
from flask_restful import Api, Resource

from database.card_table import CardTable
from database.database import Database
from log import logger

api_bp = Blueprint("api", __name__, url_prefix="/api")


class Cards(Resource):
    def get(self) -> list[dict]:
        """
        すべてのカード情報を取得する
        json文字列に変換する
        """
        all_cards = CardTable.get_all_cards()
        all_cards_dict = [card.to_dict() for card in all_cards]
        return all_cards_dict


class DeleteCard(Resource):
    def post(self) -> bool:
        payload = request.json
        if payload is None:
            return False
        CardTable.delete_card(payload["id"])
        return True


class NewCards(Resource):
    def get(self):
        new_card = CardTable.create_card()
        Database.put(new_card)
        logger.debug(f"new_card : {new_card}")
        return new_card.to_dict()


class SaveCard(Resource):
    def post(self):
        payload = request.json
        if payload is None:
            return
        for card in payload:
            CardTable.update_card(card)


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
api.add_resource(SaveCard, "/cards/save/")
api.add_resource(Members, "/members/")
