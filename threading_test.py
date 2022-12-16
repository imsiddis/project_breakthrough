import time
import threading

def func():
    print("Hello")
    time.sleep(1)
    print("World")
    time.sleep(1)
    print("!")

t = threading.Thread(target=func)
t.start()
print(threading.active_count())