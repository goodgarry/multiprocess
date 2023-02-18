# Поток - дополнительная работа кода в программе. Пример - проверка ключа активации программы.
# Процесс - новая программа, у которой свои задачи. Пример -
# В задачах, связанных с вводом-выводом, multithreading может повысить производительность.
# В задачах, связанных с вводом-выводом, multiprocessing также может повысить производительность, но издержки, как правило, оказываются выше, чем при использовании multithreading.
# Существование Python GIL дает нам понять, что в любой момент времени в программе может выполняться всего один поток.
# В задачах, связанных с процессором, использование multithreading может понизить производительность.
# В задачах, связанных с процессором, использование multiprocessing может повысить производительность.
import threading
import time
# Модуль из стандартной библиотеки
# threading.current_tread() - обратиться к потоку, который работает в функции
def get_data(data,value):
    for _ in range(value):
        print(f"[{threading.current_thread().name}] - {data}")
        time.sleep(1)
# Для второго потока
thr_list = []
for i in range(5):
# threading(self, group, target - функция, которую запускаем в потоке, name - название потока,
# args = () - аргументы функции, kwargs - словарь, daemon - демон или нет)
# В args при одном аргументе нужно ставить запятую, тк передается кортеж
    thr = threading.Thread(target = get_data, args = (str(time.time()),i),name = f"thread {i}")
    thr_list.append(thr)
    thr.start()


for i in thr_list:
    i.join()

# Разбор потоков-демонов. Если обьявить поток демоном, то в случае завершения основного потока
# завершатся и все потоки-демоны. Обычные потоки продолжат работу.

thr = threading.Thread(target=get_data, args = (str(time.time()),5), name = "daemon", daemon = True)
thr2 = threading.Thread(target=get_data, args = (str(time.time()),5), name = "just thread", daemon = False)
# Можно поставить статус демона с помощью команды
thr2.setDaemon(True)
thr.start()
thr2.start()
# При запуске кода видно, что он завершается после вывода finish, хотя потоки еще не завершили свою работу.
# Если пропишем thr2.setDaemon(False), то поток продолжит работу, а поток thr1 - завершится.
print("finish")
n = 0
# Запускаем цикл в основном потоке, чтобы посмотреть работу сразу трех потоков
#while True:
#   n+=1
#    print(n)
#    time.sleep(1)
#    if n % 10 ==0:
# С помошью кода ниже можно проверить количество потоков, посмотреть их названия и проверить
# продолжает ли работу определенный поток
#        print("active threads:", threading.activeCount())
#        print("enumerate:",threading.enumerate())
#        print("thr1 is alive",thr1.is_alive())
#        print("thr2 is alive", thr1.is_alive())
