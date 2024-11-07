import time
from multiprocessing import Pool
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)
    return all_data

list = ['file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']
start = time.time()
read_info(list[0])
read_info(list[1])
read_info(list[2])
read_info(list[3])
over = time.time()
time_1 = over - start
start_2 = time.time()
if __name__ == '__main__':
    with Pool(processes=4) as pool:
        pool.map(read_info, list)
over_2 = time.time()
time_2 = over_2 - start_2
print(f'Линейный вывод: {time_1}, Мультипроцессорный вывод: {time_2}')
