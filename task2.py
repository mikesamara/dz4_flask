import random
import multiprocessing
import time

arr = [random.randint(1, 100) for _ in range(1000000)]

def sum_array(start, end):
    global arr
    total = 0
    for i in range(start, end):
        total += arr[i]
    return total

def main():
    start_time = time.time()
    num_threads = 4
    chunk_size = len(arr) // num_threads
    process = []
    results = []


    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size
        t = multiprocessing.Process(target=lambda: results.append(sum_array(start, end)))
        process.append(t)

        t.start()


    for t in process:
        t.join()


    total_sum = sum(results)
    print(f"Сумма элементов массива: {total_sum}")
    print(f"Время выполнения: {time.time() - start_time}")

if __name__ == "__main__":
    main()