# Работа с процессами
# BaseManager - средство для передачи информации между процессами.
# Основное отличие от Manager: может передавать целые обьекты и функции.
# Очень интересная тема.
# Чтобы вспомнить подробности:
# https://www.youtube.com/watch?v=DxFnDpZ33hM&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=10
from multiprocessing import managers
import time

def get_time():
    return time.time()

if __name__ == "__main__":
    # Название BaseManager  не обязательно должно совпадать с названием функции
    managers.BaseManager.register("get", callable=get_time)
    manager = managers.BaseManager(address=('',4444),authkey=b'abc')
    server = manager.get_server()
    print("server start")
    server.serve_forever()