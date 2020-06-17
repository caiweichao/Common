import pymysql
from util.read_config import ConfigLoader
from util.logs import log


# 连接数据库建立游标，执行sql，关闭数据库

class Mysql_Util:

    def __init__(self, connect_name):
        config = ConfigLoader()
        host = config.get(connect_name, 'host')
        user = config.get(connect_name, 'user')
        pwd = config.get(connect_name, 'pwd')
        port = config.getint(connect_name, 'port')
        try:
            self.db = pymysql.Connect(host=host, user=user, password=pwd, database=None, port=int(port))
        except TimeoutError as e:
            log.error('数据库链接超时请检查，地址{0}，用户名{1}，密码{2}，端口号{3} \n {4}'.format(host, user, pwd, port, e))
            raise e
        except IndentationError as e:
            log.error('数据库链接用户名不存在请检查 用户名：{0} \n {1}'.format(user, e))
        except pymysql.err.OperationalError as e:
            log.error('用户名或密码错误请检查 用户名：{0} 密码：{1} \n {2}'.format(user, pwd, e))

    # 查询单条数据并且返回 可以通过sql查询指定的值 也可以通过索引去选择指定的值
    def fetch_one(self, sql, name=None):
        # 修改返回值为数组键值对
        # cursor=self.db.cursors.DictCursor()
        cursor = self.db.cursor()
        try:
            # 按照sql进行查询
            cursor.execute(sql)
            if name is None:
                # 返回一条数据 还有 all size（自己控制）
                sql_data = cursor.fetchone()
                return sql_data
            elif name is not None:
                sql_data = cursor.fetchone()
                return sql_data[name]
        except pymysql.err.ProgrammingError as e:
            log.error("请检查sql是否正确 sql={}".format(sql))
            raise e

    def fetch_all(self, sql):  # 查询多条数据并且返回
        # 修改返回值为数组键值对 cursor=pymysql.cursors.DictCursor
        cursor = self.db.cursor()
        try:
            # 按照sql进行查询
            cursor.execute(sql)
            # 返回一条数据 还有 all size（自己控制）
            sql_data = cursor.fetchall()
        except pymysql.err.ProgrammingError as e:
            log.error("请检查sql是否正确 sql={}".format(sql))
            raise e
        return sql_data

    def insert_data(self, sql):
        cursor = self.db.cursor()
        try:
            # 执行sql
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except pymysql.err.ProgrammingError as e:
            log.error("请检查sql是否正确 sql={}".format(sql))
            raise e

    def close_connect(self):
        # 关闭数据库链接
        self.db.close()


if __name__ == '__main__':
    sql = f"select id from tem_platform_uat.ipe_user where ID = 732;"
    test = Mysql_Util('mysql')
    data = test.fetch_one(sql)
    print(data[0])
