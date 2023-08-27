from flask import Blueprint, jsonify

from models.user import User
from service import user_service

chat_bp = Blueprint('chat', __name__, template_folder='templates')

@chat_bp.route('/add')
def add():
    user = User()
    user.username = 'ldw'
    user.password = '123'
    user.nick_name = '下雨了'
    user_service.add(user)
    return '添加成功'

@chat_bp.route('/query/<id>')
def update(id):
    user = user_service.query(id)
    return jsonify({'code': 200, 'data': user.nick_name})






