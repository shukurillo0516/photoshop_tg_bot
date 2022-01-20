import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "photoshop_tg_bot.sqlite")


conn = sqlite3.connect(db_path)
# cur = conn.cursor()
# cur.execute('DROP TABLE IF EXISTS SentFiles')
# cur.execute('CREATE TABLE SentFiles (id INTEGER PRIMARY KEY AUTOINCREMENT, folderName TEXT, appendingTime TEXT, filesNum BIGINT)')


# conn = sqlite3.connect('photoshop_tg_bot.sqlite')


def append_to_db(folder_name, appending_time, files_num):
	# folder_name = folder_name if type(folder_name) == str else folder_name
	# appending_time = 
	cur = conn.cursor()
	cur.execute('INSERT INTO SentFiles (folderName, appendingTime, filesNum) VALUES (?, ?, ?)', (folder_name, appending_time, files_num))
	conn.commit()
	cur.close()


def retrieve_data():
	cur = conn.cursor()
	cur.execute('''SELECT * FROM SentFiles''')
	for row in cur:
		print(row)
	cur.close()

def retrieve_folders():
	cur = conn.cursor()

	folders = []
	db_folders = cur.execute('''SELECT folderName FROM SentFiles''')
	

	for folder in db_folders:
		folders.append(str(folder).replace('(', '').replace(')', '').replace(',', '').replace("'", ''))

	return folders
	cur.close()
