def subsets(nums):
    """
    Generates all possible subsets (the power set) of a given list of numbers.

    Args:
        nums: A list of integers.

    Returns:
        A list of lists, where each inner list is a unique subset of nums.
    """
    results = []
    
    # We use a helper function to manage the state (index and current subset)
    # index: The index of the number we are currently considering.
    # current_subset: The list of numbers we have included so far in this path.
    def backtrack(index, current_subset):
        
        # Base Case: We've run out of numbers to consider.
        # This means 'current_subset' is now a complete subset.
        if index == len(nums):
            # We add a *copy* of current_subset to the results.
            # If we just add current_subset, it will be modified
            # by other recursive calls.
            results.append(list(current_subset))
            return

        # --- The two recursive choices ---

        # Choice 1: EXCLUDE the number at nums[index]
        # We don't add the number to our subset, and we
        # move on to consider the next number.
        backtrack(index + 1, current_subset)

        # Choice 2: INCLUDE the number at nums[index]
        # 1. Add the number to our current subset.
        current_subset.append(nums[index])
        
        # 2. Move on to consider the next number.
        backtrack(index + 1, current_subset)
        
        # 3. Backtrack: After the recursive call returns, we
        #    remove the number. This cleans up the list so it's
        #    correct for the "Exclude" path of the parent call.
        current_subset.pop()

    # Start the recursive process at the first index (0)
    # with an empty subset.
    backtrack(0, [])
    
    return results

# --- Example ---
my_nums = [1, 2, 3]
all_subsets = subsets(my_nums)
print(f"Subsets of {my_nums}:")
print(all_subsets)

# Example 2:
# my_nums = [1, 2]
# print(subsets(my_nums))
# Output: [[], [2], [1], [1, 2]] 
# (Order may vary depending on implementation)
