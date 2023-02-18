# Хранение данных в потоках, задавание атрибутов

import time
import threading
data = threading.local()
# .local - хранилище данных для потоков.
# С помощью data.value можно задать значение в потоке.
# У каждого потока можно задавать свои значения, получить значение одного потока из другого нельзя.
# Вывод кода:
# 111 222
# Название атрибута можно придумать самостоятельно:
# data.value = 111, data.test = 222 - вывод будет соответствующим.
#  Данные в атрибутах могут быть любые. int, str, словарь, кортеж и тд.
def get():
    print(data.value)

def t1():
    data.value = 111
    get()
def t2():
    data.test = 222
    print(data.test)
threading.Thread(target= t1).start()
threading.Thread(target=t2).start()