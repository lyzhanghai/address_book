import unittest
from votemodel import *

from my_exception import MyException

class TestVote(unittest.TestCase):
    def test_add_vote_log(self):
        vote_log = {
            'a_id': 1,
            'head_url': 'http://www.baidu.com',
            'gift_id': '1',
            'multiple': 1,
            'order_id': 1,
            'open_id': '123456789',
            'options': 1,
            'vote_count': 2,
            'nick_name': 'feiliming',
            'p_id': 1

        }
        v = VoteLog.add_vote_log(**vote_log)
        print(v)
        print(v.id)

    def test_get_vote_by_id(self):
        query = VoteLog.get(VoteLog.id == 6)
        print(query)
        print(query.nick_name)

    def test_get_vote_by_pid(self):
        query = VoteLog.select().where(VoteLog.p_id == 1).order_by(VoteLog.id.desc())
        for item in query:
            print(item.nick_name, item.head_url)

    def test_add_order(self):
        order = {
            'a_id': 1,
            'head_url': 'http://www.baidu.com',
            'gift_id': '1',
            'status': 1,
            'w_order_id': 1,
            'open_id': '123456789',
            'nick_name': 'feiliming',
            'money': 100,
            'p_id': 1
        }
        o = Order.add_order(**order)
        print(o)
        print(o.id)

    def test_get_vote_log_list(self):
        a_id = 1
        p_id = 1
        open_id = 1
        try:
            result = VoteLog.get_vote_log_list(a_id, p_id, open_id)
        except MyException as e:
            print(e.value)
        # for item in result:
        #     print(item.nick_name)

    def test_get_vote_log_list_sql(self):
        a_id = 1
        p_id = 1
        open_id = 1
        result = VoteLog.get_vote_log_list_sql(a_id,p_id,open_id)
        for item in result:
            print(item.nick_name)