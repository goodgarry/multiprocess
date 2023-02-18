# Работа с процессами
# Manager  - средство для обмена информацией между процессами.
# В Manager можно создавать словари, списки и другие обьекты для передачи данных между процессами.
# Каждый процесс может получить данные от менеджера или записать новые.
import multiprocessing
import time
import random


def f(m_dict, m_array):
    m_dict["name"] = "test"
    m_dict["version"] = "1.0"
    m_array.append(1)
    m_array.append(2)


def f2(m_dict, m_array):
    print(m_dict)
    print(m_array)

if __name__ == "__main__":
    with multiprocessing.Manager() as m:
        d = m.dict()
        l = m.list()
        pr = multiprocessing.Process(target=f, args = (d,l,))
        pr.start()
        pr.join()
        pr2 = multiprocessing.Process(target=f2, args = (d,l,))
        pr2.start()
        pr2.join()
        print("dict", d)
        print("list", l)