import threading
from threading import Thread, Lock
from random import randint
from time import sleep


class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            receipt = randint(50, 500)
            self.balance += receipt
            print(f'Пополнение: {receipt}. Баланс: {self.balance}\n')
            sleep(0.001)

    def take(self):
        for i in range(100):
            write_off = randint(50, 500)
            print(f'Запрос на {write_off}\n')
            if write_off <= self.balance:
                self.balance -= write_off
                print(f'Снятие: {write_off}. Баланс: {self.balance}\n')
            else:
                print('Запрос отклонён, недостаточно средств\n')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
