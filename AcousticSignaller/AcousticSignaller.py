from random import randint
from threading import Timer

def get_time() -> int:
    return randint(3,5)

def random_beep():
    print('beep boop')
    time = get_time()
    Timer(time, random_beep).start()

Timer(get_time(), random_beep).start()

while True:
    pass