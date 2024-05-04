import threading


def myTask(start, end):
    for i in range(start, end):
        print(i)


def print_numbers_in_threads(n):
    thread_list = []
    numbers_per_thread = 100 // n 

    for i in range(n):
        start = i * numbers_per_thread + 1
        end = (i + 1) * numbers_per_thread + 1 if i < n - 1 else 101
        thread = threading.Thread(target=myTask, args=(start, end))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

# Example usage with 5 threads
print_numbers_in_threads(20)
