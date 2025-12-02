from multiprocessing import Process
import time


def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**8):
        total += 1
    print("DONE ✅")

if __name__ == "__main__":
    start = time.perf_counter()

    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    end = time.perf_counter()
    print(f"time taken: {end-start:.2f}")
    