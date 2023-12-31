def permute(arr):
    result = []

    # base case
    if len(arr) == 1:
        return [arr.copy()]
    
    # recursion
    for i in range(len(arr)):
        n = arr.pop(0)
        perms = permute(arr)
        
        for perm in perms:
            perm.append(n)
        
        result.extend(perms)
        arr.append(n)
    
    return result

for p in permute([1, 2, 3]):
    print(p)

'''
This is basically a divide and conquer algorithm.
We divide the sequence up by removing the first element (then appending it back to get a different sequence).
We do this until there's 1 element left, then we will just append the removed element back to the array.
We use result as the final result array but during the recursion calls, it can act as a carrier that carries the values
of the previous call to the next call.

Since we're doing O(n) work per recursive call, and the number of permutations for a sequence will be n!, 
the time complexity will be O(n * n!)
'''
