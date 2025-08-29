#Implementation of Jump search in Python 
import math
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))   
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1   
    
    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1

    return -1   
arr = [2,4,6,8,10,12,14,16,18,20]
target = 16
result = jump_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Element not found")
    
#Implementation of Jump Search in OOP

import math

class JumpSearch:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def search(self, target):
        step = int(math.sqrt(self.n))   
        prev = 0

        # Jump until we reach a block where target could be
        while prev < self.n and self.arr[min(step, self.n) - 1] < target:
            prev = step
            step += int(math.sqrt(self.n))
            if prev >= self.n:
                return -1   # target not found

        # Linear search within the block
        while prev < min(step, self.n):
            if self.arr[prev] == target:
                return prev
            prev += 1

        return -1   # not found

        
