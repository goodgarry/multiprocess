# Изучение семафоров
# Технологии синхронизации потоков.

# Семафоры - счетчик потоков. Если выставить счетчику значение 5 и запустить 10 потоков,
# то только 5 из них смогут получить к нему доступ. Остальные будут ждать своей очереди.
# Если запустить семафор без value будет ограничение на один поток.
import threading
import time
import random
from threading import Thread, BoundedSemaphore


max_connections = 5
pool = BoundedSemaphore(value = max_connections)
# Запускаем 10 потоков, только 5 первых начинают работу.
# Как только проходит random секунд запускаются остальные потоки.
def test():
    with pool:
        t = random.randint(1,5)
        print(f"{threading.current_thread().name} - sleep:{t}")
        time.sleep(t)
for i in range(10):
    Thread(target=test).start()