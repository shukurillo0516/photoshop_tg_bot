import telegram
import datetime


bot = telegram.Bot(token = '5055002258:AAH0plokRYg9Y3MlcL3s9UveL1mB25bZrwk')
chat_id = '-605179515'


def send_message(folder_name, files_num):
	time = datetime.datetime.now()
	message = f"Appended folders: \n folder-name: {folder_name}, number of files: {files_num}, checking time: {time}\n"
	bot.send_message(text=message, chat_id=chat_id)

