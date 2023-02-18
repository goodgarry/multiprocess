# Запуск и управление процессами
# Процесс - отдельная программа, в отличии от потока.


# Библиотека для работы с процессами
import multiprocessing
import time
# Работа с процессами очень похожа на работу с потоками.
def test():
    for _ in range(5):
        print(f"{multiprocessing.current_process().name} - {time.time()}")
        time.sleep(1)

#Для обхода ошибки используем проверку процесса.
if __name__ == '__main__':
    prc = []
    for i in range(3):
        pr = multiprocessing.Process(target = test, name = f"prc-{i}")
        pr.start()
        # Проверка: работает ли процесс
        print(pr.is_alive())
        # Получить id процесса, для дальнейшей работы с ним
        print(pr.pid)
        prc.append(pr)
    print("Процессы запущены")
    for i in prc:
        # Подобная функция помогает дождаться завершения процесса.
        # Код основного процесса не пойдет дальше, пока не будет завершен процесс i.
        i.join()
    print("Процессы завершены")
    # Убийство процесса. Процесс завершится через 5 секунд после запуска.
    #time.sleep(5)
    #pr.terminate()