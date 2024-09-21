import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = datetime.datetime.now()
    for i in filenames:
        read_info(i)
    end = datetime.datetime.now()
    print(f'Линейный вызов: {end - start}')

    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'Многопроцессный вызов: {end - start}')


