from database.member import Member
from database.member_table import MemberTable
from flask import Blueprint, request
from flask_restful import Api, Resource
from log import logger

member_api_bp = Blueprint("member_api", __name__, url_prefix="/api")


class Members(Resource):
    def get(self):
        """
        すべてのメンバー情報を取得する
        json文字列に変換する
        """
        _table = MemberTable()
        all_members = _table.get_all_members()
        all_members_dict = [card.to_dict() for card in all_members]
        return all_members_dict


class NewMember(Resource):
    def get(self):
        _member_table = MemberTable()
        new_member = _member_table.create_member()
        logger.debug(f"new_card : {new_member}")
        return new_member.to_dict()


class DeleteMember(Resource):
    def post(self) -> bool:
        payload = request.json
        if payload is None:
            return False
        _table = MemberTable()
        logger.debug(f"delete card! id:{payload['id']}")
        logger.debug(f"{type(payload['id'])}")
        _table.delete_member(payload["id"])
        return True


class SaveMembers(Resource):
    def post(self):
        payload = request.json
        if payload is None:
            return
        member_table = MemberTable()
        for member_json in payload:
            logger.info(member_json)
            target_member: Member = member_table.search_member(member_json["id"])
            target_member.name = member_json["name"]
            target_member.point = member_json["point"]
        member_table.save_all()


api = Api(member_api_bp)

api.add_resource(Members, "/members/")
api.add_resource(NewMember, "/members/new/")
api.add_resource(DeleteMember, "/members/delete/")
api.add_resource(SaveMembers, "/members/save/")
