# Изучение барьеров - противоположность семафорам.
# Технологии синхронизации потоков.

# Барьер - все потоки дождутся окончания остальных потоков и только тогда закончат свою работу,
# после чего подключатся оставшиеся 5 барьеров
import threading
import time
import random
from threading import Thread, BoundedSemaphore

# Все потоки дождались момента, пока все они не выполнят свой код и только тогда вывели преодоление барьера.
# Таким образом потоки находились в ожидании, пока все не дошли до barrier.wait().
# Если количество потоков меньше значения барьера, то они будут находиться в ожидании, пока не появятся новые потоки.

def test(barrier):
    slp = random.randint(3,7)
    time.sleep(slp)
    print(f"{threading.current_thread().name} запущен в {time.ctime()}")

    barrier.wait()
    print(f"{threading.current_thread().name} преодолел барьер в {time.ctime()} ")

bar = threading.Barrier(5)
for i in range(5):
    Thread(target=test, args = (bar,)).start()