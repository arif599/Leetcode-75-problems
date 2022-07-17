"""
Understand:
	Problem Statement:
		- find pivot index where sum of left side is equal to sum of right side

	Questions:
		- what if there is no pivot index? return -1
		- is the nums array always guaranteed to be non-empty?
		- will there be more than one pivot index?

	Test Cases:
		input: [1,7,3,6,5,6]
		output: 3

		input: [1,2,3]
		output: -1

Match:
	- prefix sum
	- hashmap

Plan:
	- create a hashmap to store the running sum of the array
	- iterate through the array and at each index location compare the left sum and right sum
	- left sum = hashmap[index]
	- right sum = hashmap[len(nums)-1]-hashmap[index]
	- if left sum == right sum return index
	- else return -1
	- analysis:
		time complexity: O(n)
		space complexity: O(n)

Optimization:
	- space complexity is O(n) due to the hashmap, can we reduce this to O(1)?
	- find the sum of the given array
	- find left sum and right sum at each index
	- if left sum == right sum return index
	- else return -1
	- analysis:
		time complexity: O(n)
		space complexity: O(1)
"""

def findPivotIndex(nums):
	prefixSum = {}
	prefixSum[0] = nums[0]

	for i in range(1, len(nums)):
		prefixSum[i] = prefixSum[i-1] + nums[i]

	for i in range(len(nums)):
		leftSum = prefixSum[i]
		rightSum = prefixSum[len(nums)-1]-prefixSum[i]-nums[i+1]
		if leftSum == rightSum:
			return nums[i]
	
	return -1

def optimized_findPivotIndex(nums):
	totalSum = sum(nums)
	leftSum = 0
	for i in range(len(nums)):
		rightSum = totalSum - leftSum - nums[i]
		if leftSum == rightSum:
			return i
		leftSum += nums[i]
	return -1

if __name__ == "__main__":
	print(findPivotIndex([1,7,3,6,5,6]))
	print(optimized_findPivotIndex([1,7,3,6,5,6]))