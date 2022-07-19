import sqlite3


def db_connect(dsn):
    conn = sqlite3.connect(dsn, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    return conn


class DBClient:
    def __init__(self, dsn):
        self.conn = db_connect(dsn)

    def metrics(self, start_time, end_time):
        params = {'start': start_time, 'end': end_time}
        sql = 'SELECT * FROM metrics WHERE time >= :start AND time <= :end'
        return self.conn.execute(sql, params)