# Изучение очередей для процессов
# Позволяют передавать данные между процессами
import multiprocessing
import random


def get_text(q):
    val = random.randint(0,10)
    q.put(str(val))

#Для обхода ошибки используем проверку процесса.
if __name__ == '__main__':
    # Создаем очередь и попробуем получить ее значение из другого процесса.
    queue = multiprocessing.Queue()
    pr_list = []
    for _ in range(5):
        pr = multiprocessing.Process(target=get_text,args=(queue,))
        pr.start()

    for i in pr_list:
        i.join()
    # Основной процесс смог получить значение, которое было добавлено в побочном процессе.
    # С помощью очереди можно передавать информацию между процессами.
    # Получаем элементы с помощью итерации. Когда iter получит None тип(все элементы выведены) итерация закончится
    for elem in iter(queue.get, None):
        print(elem)


