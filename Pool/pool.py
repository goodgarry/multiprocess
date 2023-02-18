# Работа с Pool
# Класс Pool() модуля multiprocessing создает объект,
# управляющий пулом рабочих процессов, в который могут быть отправлены задания.
# Пул рабочих процессов поддерживает асинхронное выполнение задач с тайм-аутами
# и обратными вызовами и имеет параллельную реализацию.
import multiprocessing
import random



def end(response):
    print('Задание завершено!')
    print(response)



def get_value(value):
    name  = multiprocessing.current_process().name
    print(f"[{name}] value: {value}")
    # response - все возвращаемые значения, полученные от потоков
    return value

# Пул помогает выполнять задание асихронно. Каждый процесс выполняет свое задание в собственном порядке.
if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count()*3) as p:
        # Вызов пула без callback
        # p.map(get_value, list(range(50)))
        # Вызов пула с callback
        p.map_async(get_value, list(range(50)),callback=end)
        p.close()
        p.join()