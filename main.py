from ftplib import FTP

from models.model import append_to_db, retrieve_folders
from bot.bot import send_message


ftp = FTP('ftp.us.debian.org')
ftp.login('anonymous', 'anonymous@')


db_folders = retrieve_folders()

def get_folders_name():
	folders = []
	try:
	    folders = ftp.nlst()
	except ftplib.error_perm as resp:
	    if str(resp) == "550 No files found":
	        print("No files in this directory")
	    else:
	        raise('Error')
	
	for folder in folders:
		if folder in db_folders:
			print('pass')
			pass
		else:
			print(folder)
			count_files(folder)



def count_files(folder):
	try:
		ftp.cwd(folder)
	except:
		print('Error 500')

	files = []
	try:
	    files = ftp.nlst()
	except ftplib.error_perm as resp:
	    if str(resp) == "550 No files found":
	        print("No files in this directory")
	    else:
	        print('Error')
	        
	print(len(files))
	append_to_db(folder, '', len(files))
	send_message(folder, len(files))

	ftp.cwd('../')
	print('done')



get_folders_name()