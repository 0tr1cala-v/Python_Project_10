from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        self.knight_name = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.knight_name}, на нас напали!')
        warriors = 100
        days = 0
        while warriors > 0:
            warriors -= self.power
            days += 1
            sleep(1)
            print(f'{self.knight_name} сражается {days} дней, осталось {warriors} воинов.')
        print(f'{self.knight_name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')