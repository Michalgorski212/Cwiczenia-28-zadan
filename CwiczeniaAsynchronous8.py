def exercise1():
    import asyncio
    import unittest

    async def print_with_delay():
        await asyncio.sleep(2)
        print("Python Exercises!")

    class TestAsyncFunction(unittest.TestCase):
        def test_print_with_delay(self):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(print_with_delay())
            # There is no return value to assert; we rely on the print statement for manual verification.

    if __name__ == '__main__':
        unittest.main()


def exercise2():
    import asyncio
    import unittest

    async def print_with_delay(name, delay):
        await asyncio.sleep(delay)
        print(name)

    async def main():
        await asyncio.gather(
            print_with_delay("Task 1", 1),
            print_with_delay("Task 2", 2),
            print_with_delay("Task 3", 3)
        )

    class TestAsyncFunctions(unittest.TestCase):
        def test_async_functions(self):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
            # There is no return value to assert; we rely on the print statements for manual verification.

    if __name__ == '__main__':
        unittest.main()

def exercise3():
    import asyncio
    import unittest

    async def print_numbers():
        for i in range(1, 8):
            print(i)
            await asyncio.sleep(1)

    async def main():
        await print_numbers()

    class TestAsyncNumbers(unittest.TestCase):
        def test_print_numbers(self):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
            # There is no return value to assert; we rely on the print statements for manual verification.

    if __name__ == '__main__':
        unittest.main()

def exercise4():
    import aiohttp
    import asyncio
    import unittest

    async def fetch(url, session):
        async with session.get(url) as response:
            return await response.text()

    async def fetch_from_urls(url1, url2):
        async with aiohttp.ClientSession() as session:
            result1 = await fetch(url1, session)
            result2 = await fetch(url2, session)
            return result1, result2

    class TestFetchFromUrls(unittest.TestCase):
        def test_fetch(self):
            url1 = 'https://jsonplaceholder.typicode.com/todos/1'
            url2 = 'https://jsonplaceholder.typicode.com/todos/2'
            loop = asyncio.get_event_loop()
            result1, result2 = loop.run_until_complete(fetch_from_urls(url1, url2))

            self.assertIn("userId", result1)
            self.assertIn("userId", result2)

    if __name__ == '__main__':
        unittest.main()

def exercise5():
    import asyncio
    import time
    import unittest

    async def async_task(name, delay):
        await asyncio.sleep(delay)
        return f"Task {name} completed after {delay} seconds"

    async def run_multiple_tasks():
        tasks = [
            async_task("A", 2),
            async_task("B", 3),
            async_task("C", 1)
        ]
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        total_time = end_time - start_time
        return results, total_time

    class TestAsyncTasks(unittest.TestCase):
        def test_run_multiple_tasks(self):
            loop = asyncio.get_event_loop()
            results, total_time = loop.run_until_complete(run_multiple_tasks())

            self.assertTrue(any("Task A" in result for result in results))
            self.assertTrue(any("Task B" in result for result in results))
            self.assertTrue(any("Task C" in result for result in results))
            self.assertGreaterEqual(total_time, 3)  # Since the longest task takes 3 seconds

    if __name__ == '__main__':
        unittest.main()

def exercise6():
    import asyncio
    import unittest

    async def time_consuming_task():
        print("Task started")
        try:
            for i in range(10):
                print(f"Working... {i + 1}")
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            print("Task was cancelled")
            raise
        print("Task completed")

    async def main():
        task = asyncio.create_task(time_consuming_task())
        await asyncio.sleep(3)
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print("Main caught task cancellation")

    class TestTaskCancellation(unittest.TestCase):
        def test_task_cancellation(self):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())

    if __name__ == '__main__':
        unittest.main()

def exercise7():
    import asyncio
    import unittest

    async def long_running_task():
        print("Task started")
        await asyncio.sleep(10)
        return "Task completed"

    async def main():
        try:
            result = await asyncio.wait_for(long_running_task(), timeout=5)
            print(result)
        except asyncio.TimeoutError:
            print("Task timed out")

    class TestTimeout(unittest.TestCase):
        def test_timeout(self):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())

    if __name__ == '__main__':
        unittest.main()

def exercise8():
    import asyncio
    import unittest

    async def producer(queue, name, n):
        for i in range(1, n + 1):
            await asyncio.sleep(1)
            item = f'{name} item {i}'
            await queue.put(item)
            print(f'Produced {item}')

    async def consumer(queue):
        while True:
            item = await queue.get()
            if item is None:
                break
            print(f'Consumed {item}')
            queue.task_done()

    async def main():
        queue = asyncio.Queue()
        producers = [
            producer(queue, 'Producer A', 5),
            producer(queue, 'Producer B', 5),
            producer(queue, 'Producer C', 5)
        ]
        consumer_task = asyncio.create_task(consumer(queue))

        await asyncio.gather(*producers)

        await queue.put(None)
        await consumer_task

    class TestProducerConsumer(unittest.TestCase):
        def test_producer_consumer(self):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())

    if __name__ == '__main__':
        unittest.main()

def get_exercise_function(name):
    exercises = {
        'exercise1': exercise1,
        'exercise2': exercise2,
        'exercise3': exercise3,
        'exercise4': exercise4,
        'exercise5': exercise5,
        'exercise6': exercise6,
        'exercise7': exercise7,
        'exercise8': exercise8,
    }
    return exercises.get(name)

def main():
    while True:
        exercise_name = input("Enter the exercise name (e.g., 'exercise1') or 'exit' to quit: ")
        if exercise_name == 'exit':
            break

        exercise_function = get_exercise_function(exercise_name)
        if exercise_function:
            exercise_function()
        else:
            print("No exercise found with that name.")

if __name__ == "__main__":
    main()
