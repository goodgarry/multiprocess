# Работа с трубами/каналами
# Средство для передачи данных между процессами
# Имеет две переменные, которые можно назвать самостоятельно.
# В одну переменную можно записать данные и получить их через другую.


import time
from multiprocessing import Pipe, Process

def send_data(conn):
    # Отправление сообщения через канал
    # Используем переменную input
    i = 0
    while True:
        conn.send(i)
        i=i+1
    #Закрытие доступа к каналу
    # Доступ к каналу закрывается только у процесса, который активировал команду.
    # Остальные каналы все еще могут получить информацию.
    #conn.close()


# Получаем информацию в другом процессе во время цикла
def get_data(output):
    while True:
        print("p2:",output.recv())
        time.sleep(1)

if __name__ == "__main__":
    input, output  = Pipe()
    p = Process(target=send_data, args=(input,)).start()
    p2 = Process(target=get_data, args=(output,)).start()

    # Получения сообщение через канал.
    # Используем переменную output
    print("data:", output.recv())