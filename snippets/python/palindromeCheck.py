def is_palindrome(s):
    """
    Check if a string is a palindrome.
    Ignores case, spaces, and special characters.
    
    Args:
        s (str): The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the string reads the same forwards and backwards
    return cleaned == cleaned[::-1]


def is_palindrome_simple(s):
    """
    Simple palindrome check (case-sensitive, includes spaces/punctuation)
    
    Args:
        s (str): The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    return s == s[::-1]


# Test Cases
print("=" * 60)
print("PALINDROME CHECKER - TEST CASES")
print("=" * 60)

# Test cases for advanced palindrome checker (ignores case, spaces, punctuation)
print("\n1. Advanced Palindrome Checker (ignores case, spaces, punctuation):")
print("-" * 60)

test_cases_advanced = [
    "racecar",
    "A man a plan a canal Panama",
    "race a car",
    "Was it a car or a cat I saw",
    "Madam",
    "hello",
    "A Santa at NASA",
    "No 'x' in Nixon",
    "12321",
    "12345",
    ""
]

for test in test_cases_advanced:
    result = is_palindrome(test)
    print(f"'{test}' → {result}")

# Test cases for simple palindrome checker (exact match)
print("\n2. Simple Palindrome Checker (exact match):")
print("-" * 60)

test_cases_simple = [
    "racecar",
    "Racecar",
    "noon",
    "hello",
    "12321",
    "abcba",
    "abccba",
    "a",
    ""
]

for test in test_cases_simple:
    result = is_palindrome_simple(test)
    print(f"'{test}' → {result}")

# Additional demonstration
print("\n3. Step-by-step example:")
print("-" * 60)
example = "A man a plan a canal Panama"
cleaned = ''.join(char.lower() for char in example if char.isalnum())
print(f"Original: '{example}'")
print(f"Cleaned:  '{cleaned}'")
print(f"Reversed: '{cleaned[::-1]}'")
print(f"Is palindrome? {is_palindrome(example)}")
