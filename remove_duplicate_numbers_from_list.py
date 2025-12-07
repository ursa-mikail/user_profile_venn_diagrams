"""
Monotonic increase: The list always increases, with random increments between 1-5 (configurable)
Random repetition: Each number has a 30% chance of being repeated 1-3 times (configurable)
Order preservation: When removing duplicates, the first occurrence is kept
Statistics: Shows which numbers were removed and how many times each appeared
Flexible parameters: All random ranges and probabilities are configurable
"""

import random

def generate_monotonic_list(start=1, min_increment=1, max_increment=10, 
                           min_length=10, max_length=30, 
                           repetition_chance=0.3, max_repeats=5):
    """
    Generate a list of numbers that monotonically increases with possible repetitions.
    
    Parameters:
    - start: Starting value
    - min_increment, max_increment: Range for random increments
    - min_length, max_length: Range for list length
    - repetition_chance: Probability (0-1) that a value will be repeated
    - max_repeats: Maximum number of times a value can be repeated
    
    Returns:
    - List of integers
    """
    result = []
    current = start
    
    target_length = random.randint(min_length, max_length)
    
    while len(result) < target_length:
        # Add current value
        result.append(current)
        
        # Randomly decide if we should repeat this value
        if random.random() < repetition_chance and len(result) < target_length:
            repeats = random.randint(1, min(max_repeats, target_length - len(result)))
            result.extend([current] * repeats)
        
        # Increment for next value
        increment = random.randint(min_increment, max_increment)
        current += increment
    
    return result

def find_and_remove_duplicates(numbers):
    """
    Find repeated numbers in a list, remove them, and report statistics.
    
    Parameters:
    - numbers: List of integers
    
    Returns:
    - unique_list: List with duplicates removed (order preserved)
    - removed_stats: Dictionary with removed numbers and their occurrences
    """
    if not numbers:
        return [], {}
    
    # Track first occurrences and counts
    first_occurrence = {}
    counts = {}
    
    # First pass: count occurrences
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    # Second pass: build unique list (preserving order of first occurrence)
    unique_list = []
    seen = set()
    
    for num in numbers:
        if num not in seen:
            unique_list.append(num)
            seen.add(num)
    
    # Find numbers that were removed (had duplicates)
    removed_stats = {num: count for num, count in counts.items() if count > 1}
    
    return unique_list, removed_stats

def main():
    """Main function to demonstrate the functionality."""
    # Generate a random monotonic list
    print("Generating random monotonic list...")
    numbers = generate_monotonic_list(
        start=random.randint(1, 100),
        min_increment=1,
        max_increment=5,
        min_length=15,
        max_length=30,
        repetition_chance=0.4,
        max_repeats=3
    )
    
    print(f"Original list ({len(numbers)} elements):")
    print(numbers)
    print()
    
    # Find and remove duplicates
    unique_list, removed_stats = find_and_remove_duplicates(numbers)
    
    print(f"List with duplicates removed ({len(unique_list)} elements):")
    print(unique_list)
    print()
    
    if removed_stats:
        print("Removed numbers and their occurrences:")
        for num, count in sorted(removed_stats.items()):
            print(f"  {num}: appeared {count} times (removed {count-1} duplicates)")
        
        total_removed = sum(count-1 for count in removed_stats.values())
        print(f"\nTotal duplicates removed: {total_removed}")
    else:
        print("No duplicates found in the list.")

if __name__ == "__main__":
    main()

"""
Generating random monotonic list...
Original list (15 elements):
[89, 91, 91, 92, 96, 96, 96, 96, 97, 97, 102, 104, 104, 104, 104]

List with duplicates removed (7 elements):
[89, 91, 92, 96, 97, 102, 104]

Removed numbers and their occurrences:
  91: appeared 2 times (removed 1 duplicates)
  96: appeared 4 times (removed 3 duplicates)
  97: appeared 2 times (removed 1 duplicates)
  104: appeared 4 times (removed 3 duplicates)

Total duplicates removed: 8

"""