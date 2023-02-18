# Работа с Pool
# Apply Async  - работает так же, как и стандартный Pool, но
# callback происходит по завершению каждого задания, а не по завершению всех заданий.
import multiprocessing
import random


def end(response):
    print(response)

def out(x):
    print(f"value: {x}")
    return x
if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count()*3) as p:
        for i in range(10):
            p.apply_async(out, args = (i,), callback = end)
        p.close()
        p.join()