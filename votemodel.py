from peewee import *

from datetime import datetime

from my_exception import MyException

db = MySQLDatabase(host='114.215.71.74', user='root', passwd='mysql',
                   database='system_manager_ssh_0818', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class Order(BaseModel):
    a_id = IntegerField()
    head_url = CharField()
    gift_id = CharField()
    open_id = CharField()
    w_order_id = CharField()
    money = DoubleField()
    nick_name = CharField()
    create_time = DateTimeField(default=datetime.now())
    p_id = IntegerField()
    a_id = IntegerField()
    status = IntegerField()
    transaction_id = CharField()
    time_end = DateTimeField()

    class Meta:
        db_table = 'tb_order'

    @classmethod
    def add_order(cls, **kwargs):
        a_id = kwargs.get('a_id')
        head_url = kwargs.get('head_url')
        gift_id = kwargs.get('gift_id')
        w_order_id = kwargs.get('w_order_id')
        open_id = kwargs.get('open_id')
        options = kwargs.get('options')
        status = kwargs.get('status')
        nick_name = kwargs.get('nick_name')
        p_id = kwargs.get('p_id')
        transaction_id = kwargs.get('transaction_id')
        money = kwargs.get('money')

        p = cls.create(a_id=a_id, head_url=head_url,
                       gift_id=gift_id,
                       w_order_id=w_order_id,
                       open_id=open_id,
                       options=options,
                       status=status,
                       nick_name=nick_name,
                       p_id=p_id,
                       money=money,
                       transaction_id=transaction_id)
        return p


class VoteLog(BaseModel):
    a_id = IntegerField()
    head_url = CharField()
    gift_id = CharField()
    multiple = IntegerField()
    order_id = IntegerField()
    open_id = CharField()
    options = IntegerField()
    vote_count = IntegerField()
    nick_name = CharField()
    create_time = DateTimeField(default=datetime.now())
    p_id = IntegerField()

    class Meta:
        db_table = 'tb_vote_log'

    # 添加投票计录信息

    @classmethod
    @db.commit_on_success
    def add_vote_log(cls, **kwargs):
        '''
        添加投票记录
        :param kwargs:
        :return:
        '''
        a_id = kwargs.get('a_id')
        head_url = kwargs.get('head_url')
        gift_id = kwargs.get('gift_id')
        multiple = kwargs.get('multiple')
        order_id = kwargs.get('order_id')
        open_id = kwargs.get('open_id')
        options = kwargs.get('options')
        vote_count = kwargs.get('vote_count')
        nick_name = kwargs.get('nick_name')
        p_id = kwargs.get('p_id')
        p = cls.create(a_id=a_id, head_url=head_url,
                       gift_id=gift_id,
                       multiple=multiple,
                       order_id=order_id,
                       open_id=open_id,
                       options=options,
                       vote_count=vote_count,
                       nick_name=nick_name,
                       p_id=p_id)

        Order.add_order(**kwargs)
        # 测试事务.
        # raise Exception
        return p

    '''
    通过活动
    :param a_id 活动id
    :param p_id 人id.
    :param open_id 微信open_id.
    '''

    @classmethod
    def get_vote_log_list(cls, a_id, p_id, open_id):
        query = cls.select().where((VoteLog.a_id == a_id) & (VoteLog.p_id == p_id) & (VoteLog.open_id == open_id))
        raise MyException("查询出错.")
        return query
    '''
    测试用原生sql获取数据.
    :param a_id 活动id
    :param p_id 人id.
    :param open_id 微信open_id.
    '''
    @classmethod
    def get_vote_log_list_sql(cls, a_id, p_id, open_id):
        query = cls.raw("select * from tb_vote_log where p_id=%s", p_id)
        # print(query.sql())
        return query
