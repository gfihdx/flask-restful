import sqlite3


# 将游标获取的元组根据数据库列表转为字典表
def make_dicts(cursor, row):
    return dict((cursor.description[i][0], value) for i, value in enumerate(row))


class SqlHelper(object):
    def __init__(self):
        self.path = r"e:\test\test.db"

    # 打开数据库连接
    def get_db(self):
        db = sqlite3.connect(self.path)
        db.row_factory = make_dicts
        return db

    # 执行SQL语句，但不返回结果
    def execute_sql(self, sql, prms=()):
        c = self.get_db().cursor()
        c.execute(sql, prms)
        c.connection.commit()

    # 执行用于选择数据的SQL语句。
    def query_sql(self, sql, prms=(), one=False):
        c = self.get_db().cursor()
        result = c.execute(sql, prms).fetchall()
        c.close()
        return (result[0] if result else None) if one else result


db = SqlHelper()
