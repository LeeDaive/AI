from flask import Blueprint, jsonify
import requests, json
from config.config import get_env
from models.auth import Auth
from extension.ext_database import db

bp = Blueprint('auth', __name__)
corpid = get_env('CORPID')
secret = get_env('CORPSECRET')

@bp.route('/get_access_token')
def get_access_token():
    response = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}')
    content = json.loads(response.content)
    if content['errcode'] == 0:
        access_token = content['access_token']
        auth = Auth(access_token=access_token)
        db.session.add(auth)
        db.session.commit()
        return jsonify({'code': 200, 'data': None})
    else:
        return jsonify({'code': 10000, 'data': '获取token异常'})

@bp.route('/send')
def send_message():
    #查询缓存的ACCESS_TOKEN
    auth = Auth.query.first()
    access_token = auth.access_token
    query_user(access_token)
    params = {
        "touser": "LiDaiWei",
        "msgtype": "text",
        "agentid": 1000002,
        "text": {
            "content": "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    response = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}', params)
    content = json.loads(response.content)
    if content['errcode'] == 0:
        access_token = content['access_token']
        auth = Auth(access_token=access_token)
        db.session.add(auth)
        db.session.commit()
        return jsonify({'code': 200, 'data': None})
    else:
        return jsonify({'code': 10000, 'data': '获取token异常'})

def query_user(access_token):
    response = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/list_id?access_token={access_token}',{"cursor": "1", "limit": 10000})
    content = json.loads(response.content)
    if content['errcode'] == 0:
        access_token = content['access_token']
        auth = Auth(access_token=access_token)
        db.session.add(auth)
        db.session.commit()
        return jsonify({'code': 200, 'data': None})
    else:
        return jsonify({'code': 10000, 'data': '获取token异常'})

