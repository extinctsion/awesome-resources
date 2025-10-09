import math


def factorial_iterative(n):
    """
    Calculate factorial using iteration.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)


def factorial_math_library(n):
    """
    Calculate factorial using Python's math library.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
    """
    return math.factorial(n)


def factorial_with_steps(n):
    """
    Calculate factorial and show calculation steps.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        tuple: (result, steps_string)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return (1, f"{n}! = 1")
    
    steps = []
    result = 1
    
    for i in range(1, n + 1):
        result *= i
        steps.append(str(i))
    
    steps_string = f"{n}! = " + " × ".join(steps) + f" = {result}"
    
    return (result, steps_string)


# Test Cases
print("=" * 70)
print("FACTORIAL CALCULATOR - TEST CASES")
print("=" * 70)

# Test 1: Basic factorial calculations
print("\n1. Basic Factorial Calculations (Iterative):")
print("-" * 70)
test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in test_values:
    result = factorial_iterative(n)
    print(f"{n}! = {result}")

# Test 2: Recursive approach
print("\n2. Recursive Approach:")
print("-" * 70)
test_recursive = [0, 1, 5, 10, 12]

for n in test_recursive:
    result = factorial_recursive(n)
    print(f"{n}! = {result}")

# Test 3: Using math library
print("\n3. Using Math Library:")
print("-" * 70)
test_math = [0, 5, 10, 15, 20]

for n in test_math:
    result = factorial_math_library(n)
    print(f"{n}! = {result}")

# Test 4: Large numbers
print("\n4. Large Number Calculations:")
print("-" * 70)
large_numbers = [15, 20, 25, 30]

for n in large_numbers:
    result = factorial_iterative(n)
    print(f"{n}! = {result}")

# Test 5: Factorial with steps
print("\n5. Factorial with Calculation Steps:")
print("-" * 70)
step_tests = [0, 1, 4, 6, 8]

for n in step_tests:
    result, steps = factorial_with_steps(n)
    print(steps)

# Test 6: Comparing all methods
print("\n6. Method Comparison (n=10):")
print("-" * 70)
n = 10
print(f"Iterative:  {n}! = {factorial_iterative(n)}")
print(f"Recursive:  {n}! = {factorial_recursive(n)}")
print(f"Math lib:   {n}! = {factorial_math_library(n)}")

# Test 7: Edge cases and error handling
print("\n7. Edge Cases and Error Handling:")
print("-" * 70)
print(f"0! = {factorial_iterative(0)} (by definition)")
print(f"1! = {factorial_iterative(1)}")

# Test negative number
try:
    result = factorial_iterative(-5)
except ValueError as e:
    print(f"(-5)! → Error: {e}")

# Test 8: Practical applications
print("\n8. Practical Applications:")
print("-" * 70)
print("Permutations of 5 items: 5! =", factorial_iterative(5))
print("Combinations: C(10,3) = 10!/(3!×7!) =", 
      factorial_iterative(10) // (factorial_iterative(3) * factorial_iterative(7)))
print("Number of ways to arrange 'PYTHON': 6! =", factorial_iterative(6))

# Test 9: Performance note
print("\n9. Performance Notes:")
print("-" * 70)
print("Iterative:  Fast, no recursion limit, recommended")
print("Recursive:  Clean code, but stack overflow for large n")
print("Math lib:   Optimized C implementation, fastest")
print("\nRecommended: Use math.factorial() for production code")

# Test 10: Interesting factorial facts
print("\n10. Interesting Facts:")
print("-" * 70)
print(f"5! = {factorial_iterative(5)} (seconds in 2 minutes)")
print(f"7! = {factorial_iterative(7)} (days in ~13.8 years)")
print(f"10! = {factorial_iterative(10)} (seconds in ~6 weeks)")
print(f"13! = {factorial_iterative(13)} (roughly seconds in 2 centuries)")
