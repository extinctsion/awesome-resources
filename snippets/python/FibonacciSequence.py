def fibonacci_iterative(n):
    """
    Generate Fibonacci sequence up to n terms using iteration.
    
    Args:
        n (int): Number of terms to generate
        
    Returns:
        list: List of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    Note: This is inefficient for large n.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_memoization(n, memo={}):
    """
    Calculate the nth Fibonacci number using memoization (optimized recursion).
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        memo (dict): Dictionary to store computed values
        
    Returns:
        int: The nth Fibonacci number
    """
    if n in memo:
        return memo[n]
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]


def fibonacci_generator(n):
    """
    Generate Fibonacci sequence using a generator (memory efficient).
    
    Args:
        n (int): Number of terms to generate
        
    Yields:
        int: Next Fibonacci number
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# Test Cases
print("=" * 70)
print("FIBONACCI SEQUENCE - TEST CASES")
print("=" * 70)

# Test 1: Iterative approach
print("\n1. Iterative Approach (generates sequence):")
print("-" * 70)
test_values = [0, 1, 5, 10, 15]

for n in test_values:
    result = fibonacci_iterative(n)
    print(f"First {n} terms: {result}")

# Test 2: Recursive approach
print("\n2. Recursive Approach (finds nth number):")
print("-" * 70)
test_positions = [0, 1, 5, 10, 15, 20]

for pos in test_positions:
    result = fibonacci_recursive(pos)
    print(f"Fibonacci({pos}) = {result}")

# Test 3: Memoization approach
print("\n3. Memoization Approach (optimized recursion):")
print("-" * 70)
test_positions_memo = [0, 1, 10, 20, 30, 50]

for pos in test_positions_memo:
    result = fibonacci_memoization(pos)
    print(f"Fibonacci({pos}) = {result}")

# Test 4: Generator approach
print("\n4. Generator Approach (memory efficient):")
print("-" * 70)
print(f"First 12 terms using generator: {list(fibonacci_generator(12))}")

# Test 5: Large number demonstration
print("\n5. Large Number Test (comparing methods):")
print("-" * 70)
n_large = 30
print(f"Iterative - First {n_large} terms:")
print(fibonacci_iterative(n_large))
print(f"\nMemoization - Fibonacci({n_large}) = {fibonacci_memoization(n_large)}")
print(f"Generator - First {n_large} terms:")
print(list(fibonacci_generator(n_large)))

# Test 6: Edge cases
print("\n6. Edge Cases:")
print("-" * 70)
edge_cases = [0, 1, 2]
for n in edge_cases:
    print(f"n={n}:")
    print(f"  Iterative: {fibonacci_iterative(n)}")
    print(f"  Recursive: {fibonacci_recursive(n)}")
    print(f"  Generator: {list(fibonacci_generator(n))}")

# Test 7: Performance comparison note
print("\n7. Method Comparison:")
print("-" * 70)
print("Iterative:    Fast, simple, returns sequence")
print("Recursive:    Slow for large n (exponential time)")
print("Memoization:  Fast, optimized recursion")
print("Generator:    Memory efficient, good for large sequences")
print("\nRecommended: Use iterative or memoization for best performance")
