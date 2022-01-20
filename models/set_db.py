import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "photoshop_tg_bot.sqlite")


conn = sqlite3.connect(db_path)

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS SentFiles')
cur.execute('CREATE TABLE SentFiles (id INTEGER PRIMARY KEY AUTOINCREMENT, folderName TEXT, appendingTime TEXT, filesNum BIGINT)')

cur.close()