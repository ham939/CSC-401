

import random

def randomize_in_place(A):
    n = len(A)
    for i in range(n):
        # Random(i, n) - getting a random index between i and n
        rand_index = random.randint(i, n-1) 
        # Swap A[i] with A[rand_index]
        A[i], A[rand_index] = A[rand_index], A[i]
        print(f"Iteration {i+1}:")
        print(f"Swapping elements at indices {i} and {rand_index}.")
        print(f"Random({i},{n-1}) = {rand_index}")
        print("Current Array:", A)
        print()

# Example array of length 10
A = [3, 5, 2, 4, 1, 6, 9, 8, 7, 0]
print("Original Array:", A)
print()
randomize_in_place(A)
print("Final Array:", A)
