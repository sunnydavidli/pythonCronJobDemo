import schedule
import time

def job():
    print("I'm working...")
    print("Sleepy!")

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    
print("test)

def test():
    print("have a fun!")
 