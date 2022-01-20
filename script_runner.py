import schedule
import time
  
def call_main_func():
    print("Geeksforgeeks")
  
schedule.every(.1).minutes.do(call_main_func)
  
while True:
    schedule.run_pending()
    time.sleep(1)