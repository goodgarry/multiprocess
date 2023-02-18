# Работа с процессами
# Condition в отличии от Event срабатывает только один раз.
# То есть в то время как события достаточно активировать только один раз,
# состояния придется активировать каждый раз, как потребуется выполнить код.

import time
import random
import multiprocessing



def f1(cond):
    while True:
        with cond:
            cond.wait()
            print("Получили событие")

def f2(cond):
    for i in range(100):
        if i%10 == 0:
            with cond:
                cond.notify()
        else:
            print(f"f2: {i}")
        time.sleep(1)

if __name__ == '__main__':
    cond = multiprocessing.Condition()
    multiprocessing.Process(target=f1,args=(cond,)).start()
    multiprocessing.Process(target=f2,args=(cond,)).start()