import multiprocessing
import time


def withdraw(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


def deposit(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def perform_transactions():
    balance = multiprocessing.Value('i', 100)



    p1 = multiprocessing.Process(target=withdraw, args=(balance, lock))
    p2 = multiprocessing.Process(target=deposit, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final balance = {}".format(balance.value))


if __name__ == "__main__":
    t = time.time()
    for _ in range(10):
        perform_transactions()
    print(f"Done it takes {time.time() - t}")
