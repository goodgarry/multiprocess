# Запуск процессов через классы

import time
import multiprocessing

class Process(multiprocessing.Process):
    # Перезаписываем метод run из класса
    def run(self):
        print("work")
#Для обхода ошибки используем проверку процесса.
if __name__ == '__main__':
    pr = Process()
    pr.start()
