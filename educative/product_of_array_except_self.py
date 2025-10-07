# Optimized solution -> T: O(n) Solution, S: O(n) counting output, S: O(1) auxiliary space
def find_product3(nums):
    n = len(nums)
    product = [1] * n

    # Create list of product to the left except self
    left_prod = 1
    for curr_idx in range(n):
        product[curr_idx] = left_prod 
        left_prod *= nums[curr_idx]
   
    # Multiply product to the right except self to each num in 
    # product list
    right_prod = 1
    for curr_idx in range(n-1,-1,-1):
        product[curr_idx] *= right_prod
        right_prod *= nums[curr_idx]
    
    return product

# T: O(n) Solution, S: O(n)
def find_product2(nums):
    product = []

    # Create list of product to the left except self
    left_prod = 1
    for curr_num in nums:
        product.append(left_prod)
        left_prod *= curr_num
   
    # Multiply product to the right except self to each num in 
    # product list
    right_prod = 1
    for i in range(len(nums)-1,-1,-1):
        product[i] *= right_prod
        right_prod *= nums[i]
    
    return product


# T: O(n^2) Solution, S: O(n)
def find_product(nums):
    product = []
    left_product = 1

    for curr_idx in range(len(nums)):
        right_product = 1

        for num_to_right in nums[curr_idx + 1:]:
            right_product *= num_to_right
        product.append(right_product * left_product)

        left_product *= nums[curr_idx]

    return product

# Testing
print(find_product([2,4,0,6]))
print(find_product2([2,4,0,6]))
print(find_product3([2,4,0,6]))
print(find_product3([0])) # multiplicative identity

# Testing of optimized solution
assert find_product3([1, 2, 3, 0]) == [0, 0, 0, 6] # Handles zeroes
assert find_product3([]) == [] # Empty list
assert find_product3([0]) == [1] # One item -> Product of an empty list is 1
assert find_product3([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0] # Negative numbers
