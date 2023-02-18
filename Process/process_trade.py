# Переда информации между процессами

import multiprocessing
import time
import random

def add_value(locker,array, index):
    with locker:
        num = random.randint(0,5)
        ytime = time.ctime()
        array[index] = num
        print(f"array{[index]} = {num}, time {ytime}")
        time.sleep(num)


#Для обхода ошибки используем проверку процесса.
if __name__ == '__main__':
    # Создаем блокировщик
    lock = multiprocessing.Lock()
    # Создаем массив из процессов  Array("тип данных", кол-во)
    # С помощью него можно передавать информацию между процессами.
    arr = multiprocessing.Array("i",range(10))

    process = []
    # Создаем 10 процессов
    for i in range(10):
        pr = multiprocessing.Process(target=add_value, args=(lock, arr,i,))
        process.append(pr)
        pr.start()
    #Ждем окончания всех процессов
    for i in process:
        i.join()

    print(list(arr))
    print("Все процессы завершены")