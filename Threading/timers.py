# Использование таймеров
import time
import threading


def test(a):
    while True:
        print(a)
        time.sleep(1)


# Используем класс Timer(interval-кол-во секунд до запуска потока, function - функция запуска потока
# args - аргументы, kargs - кортеж с аргументами)
# Поток заработает через 10 секунд после запуска.
threading.Timer(2, test,args = ("test1",)).start()
# Запускаем цикл в основном потоке, чтобы проверить блокировку. Блокировки нет, оба потока работают.


# Таймер можно остановить до запуска потока. В таком случае поток не будет запущен.
# Для этого используем thr.cancel()
thr = threading.Timer(4, test,args = ("test2",))
thr.start()
# Для потоков с таймером работают все функции потоков без таймеров.
# Единственное отличие - thr.cancel()
for _ in range(3):
    time.sleep(1)
thr.cancel()
print("Поток 2 остановлен. Вывод test2 не запущен.")
while True:
    print("111")
    time.sleep(2)