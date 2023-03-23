import time

list = []

start = time.time()
for i in range(100000000):
	list.append('a')
end = time.time()
time_build = (end - start)*1000
print(f'time to build list: {time_build}')

start = time.time()
list.pop()
end = time.time()
time_remove_end = (end - start)*1000
print(f'time - {time_remove_end}')

start = time.time()
list.pop(0)
end = time.time()
time_remove_start = (end - start)*1000
print(f'time - {time_remove_start}')

# print(f'difference: {time_remove_start-time_remove_end}')



