# Синхронизация процессов с помощью RLock и Lock
# Работают так же как у потоков.


import multiprocessing


# Используя процессы надо явно указывать блокировщик, в отличии от потоков.
def get_value(locker):
    # Вместо locker.acquire() и locker.release() можно использовать with locker:
    with locker:
        #locker.acquire()
        name = multiprocessing.current_process().name
        print(f"Процесс {name} запущен")
        #locker.release()
        print(f"Процесс {name} завершен")
    #Для обхода ошибки используем проверку процесса.
if __name__ == '__main__':
    # Использование lock может сильно навредить программе, если какой либо из потоков разблокирует его.
    # Сравнение: Есть замок, но ключ к нему есть у каждого.
    # Лучше использовать RLock.
    lock = multiprocessing.Lock()
    # Чтобы такого избежать можно использовать threading.RLock()
    # В таком случае блокировку может разблокировать только тот поток,
    #          который его заблокировал.
    # Сравнение: Есть замок, ключ от него только у одного человека.
    rlock = multiprocessing.RLock()
    multiprocessing.Process(target=get_value,args=(rlock,)).start()
    multiprocessing.Process(target=get_value, args=(rlock,)).start()