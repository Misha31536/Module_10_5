from time import perf_counter
import multiprocessing

def read_info(name):
    with open(name, 'r') as file:
        all_data = [all_data.rstrip() for all_data in file]
        return all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]
# 1 способ линейный через for
start = perf_counter()
for i in filenames:
    read_info(i)
finish = perf_counter()
print(f'{finish - start:0.4f} сек линейный')
# 2й способ мультипроцессорный
# if __name__ == '__main__':
#     start = perf_counter()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     finish = perf_counter()
#     print(f'{finish - start} сек линейный')
#3й способ через map
start = perf_counter()
data = list(map(read_info, filenames))
finish = perf_counter()
print(f'{finish - start:0.4f} сек линейный через map')