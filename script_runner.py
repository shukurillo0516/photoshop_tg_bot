import schedule
import time

from main import get_folders_name
  
def call_main_func():
    get_folders_name()
  
schedule.every(1).minutes.do(call_main_func)
  
while True:
    schedule.run_pending()
    time.sleep(1)