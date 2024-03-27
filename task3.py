import random
import asyncio
import time

arr = []
arr = [random.randint(1, 100) for _ in range(1000000)]
async def async_sum(arr):
    total = 0

    for num in arr:
        total += num

    return total

async def main():
    result = await async_sum(arr)
    print(f"Сумма элементов массива: {result}")


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Время выполнения: {time.time() - start_time}")