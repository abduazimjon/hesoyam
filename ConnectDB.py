from psycopg2 import connect

host = 'localhost'
username = 'postgres'
password = '1974'
db_name = 'Autoschool'


def get_region():
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = """
                SELECT region_id, region_name FROM viloyat
                ORDER BY region_id ASC
                """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res
    except Exception as e:
        print('Error', e)
