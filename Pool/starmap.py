# Работа с Pool
# Starmap Async используется в случае, когда callback должен состоять из нескольких значений
# Существует и обычный starmap без callback, работает так же.
import multiprocessing
import random


def end(response):
    print(response)

def out(x,y,z):
    print(f"value: {x} {y} {z}")
    return x,y,z
if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count()*3) as p:
        p.starmap_async(out, [(1,2,3 ),(4,5,6)],callback = end)
        p.close()
        p.join()