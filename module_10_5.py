import time
import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file_1:
        while True:
            line = file_1.readline().strip()
            all_data.append(line)
            if not line:
                break

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

time_start_1 = datetime.now()

for i in files:
    print(i)
    read_info(i)

time_stop_1 = datetime.now()

time_of_line_function = time_stop_1 - time_start_1
print(f'Время работы линейного вызова: {time_of_line_function}')

if __name__ == '__main__':
    time_start_2 = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    time_stop_2 = datetime.now()
    time_of_multiprocessing = time_stop_2 - time_start_2
    print(f'Время работы мультипроцесса: {time_of_multiprocessing}')