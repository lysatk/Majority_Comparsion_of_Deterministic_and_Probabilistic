import random
import collections
import tracemalloc  # Importing the tracemalloc module for memory tracking

# Algorytm deterministyczny (Boyer-Moore)
def majority_element_deterministic(a):
    candidate = None
    count = 0

    # Faza 1: Znalezienie kandydata
    for num in a:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Faza 2: Weryfikacja kandydata
    if a.count(candidate) > len(a) // 2:
        return candidate
    return None

# Algorytm losowy
def majority_element_randomized(a, num_trials=10):
    n = len(a)
    for _ in range(num_trials):
        candidate = random.choice(a)
        if a.count(candidate) > n // 2:
            return candidate

    return None

#test memory usage
def measure_memory(func, *args, **kwargs):
    tracemalloc.start()  
    result = func(*args, **kwargs)  
    current, peak = tracemalloc.get_traced_memory()  # Get memory usage
    tracemalloc.stop()  # Stop tracking
    return result, current, peak

def test_algorithms_with_memory():
    test_cases = [
        ([3, 3, 4, 2, 4, 4, 2, 4, 4], 4),
        ([3, 3, 4, 2, 4, 4, 2, 4], None),
        ([1, 1, 1, 1, 2, 3, 4], 1),
        ([1, 2, 3, 4, 5], None),
        ([1, 1, 2, 2, 1, 1], 1),
    ]

    print("Testing Deterministic Algorithm with Memory Usage:")
    for a, expected in test_cases:
        result, current, peak = measure_memory(majority_element_deterministic, a)
        print(f"Array: {a}, Expected: {expected}, Result: {result}, "
              f"Current Memory: {current / 1024:.2f} KB, Peak Memory: {peak / 1024:.2f} KB")

    print("\nTesting Randomized Algorithm with Memory Usage:")
    for a, expected in test_cases:
        result, current, peak = measure_memory(majority_element_randomized, a)
        print(f"Array: {a}, Expected: {expected}, Result: {result}, "
              f"Current Memory: {current / 1024:.2f} KB, Peak Memory: {peak / 1024:.2f} KB")

# Porównanie złożoności obliczeniowej i pamięciowej
def compare_complexity_and_memory():
    import time

    sizes = [10**3, 10**4, 10**5]  # Adjusted sizes for practical runtime
    print("\nComplexity and Memory Comparison:")
    for size in sizes:
        a = [random.randint(1, 5) for _ in range(size)]  # Generowanie losowego wejścia

        # Test algorytmu deterministycznego
        start = time.time()
        _, current_d, peak_d = measure_memory(majority_element_deterministic, a)
        deterministic_time = time.time() - start

        # Test algorytmu losowego
        start = time.time()
        _, current_r, peak_r = measure_memory(majority_element_randomized, a, num_trials=3)
        randomized_time = time.time() - start

        print(f"Size: {size}, "
              f"Deterministic Time: {deterministic_time:.6f}s, "
              f"Deterministic Memory: Current {current_d / 1024:.2f} KB, Peak {peak_d / 1024:.2f} KB, "
              f"Randomized Time: {randomized_time:.6f}s, "
              f"Randomized Memory: Current {current_r / 1024:.2f} KB, Peak {peak_r / 1024:.2f} KB")

if __name__ == "__main__":
    # test_algorithms_with_memory()
    compare_complexity_and_memory()
