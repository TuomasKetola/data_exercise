import sqlite3
from sqlite3 import Error
from datetime import datetime, timedelta



def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
#     finally:
#         if conn:
#             conn.close()
    return conn


def fetch_from_db(conn,q):
    cur = conn.cursor()
    cur.execute(q)
    rows = cur.fetchall()
    return rows

conn = create_connection('trains.db') # just use ram as its small data

# scheduled arrival 
datetime_str = '2022-11-10 15:58:00'

datetime_schedule = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

avg_late_seconds = fetch_from_db(conn,'select avg(difference_in_time) from train_data')[0][0] * 60
new_time = datetime_schedule + timedelta(seconds=avg_late_seconds)
print("arvioitu saapumisaika tampereella: {}".format(
new_time.strftime("%Y-%m-%d %H:%M:%S")
    ))
