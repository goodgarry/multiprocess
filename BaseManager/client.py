# Клиентская часть basemanager
# Обращаемся к BaseManager и получаем доступ к функции и ее выводу из другого скрипта
#
from multiprocessing import managers

if __name__ == "__main__":
    managers.BaseManager.register("get")
    manager = managers.BaseManager(address=("127.0.0.1",4444), authkey=b"abc")
    print("client connected")
    manager.connect()

    res = manager.get()
    print("result:", res)