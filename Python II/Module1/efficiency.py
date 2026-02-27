import time
def benchmark() -> None:
    problem_size = 1000000

    print("Benchmarking algorithm runtime")
    print("problem_size,runtime_seconds")

    for counter in range(4):
        start = time.time()
        # Start the algorithm
        work = 1
        for x in range(problem_size):
            work += 5
            work -= 5
        # End of algorithm
        elapsed = time.time() - start
        print(f"{problem_size},{elapsed:.4f}")
        problem_size *= 3

benchmark()