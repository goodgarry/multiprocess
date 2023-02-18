# Работа с процессами
# Event - система событий в работе с процессами.
# Изначально event = false,
# используя event.set() событие принимает значение true.

# С пмоощью event можно проверять, закончил ли работут тот или иной код
# и только тогда продолжать работу процесса.

from multiprocessing import Process, Event
import time
event = Event()

def test(event):
    print("Функция test запущена!")
    while True:
        event.wait()
        print("test")
        time.sleep(1)
def test2(event):
    for i in range(10):
        print(i)
        time.sleep(1)
    event.set()
#Для обхода ошибки используем проверку процесса.
if __name__ == '__main__':
    event = Event()
    Process(target=test,args=(event,)).start()
    Process(target=test2,args=(event,)).start()