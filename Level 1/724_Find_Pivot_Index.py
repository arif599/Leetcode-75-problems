"""
Understand:
	Problem Statement: 
		- given an array, find the running sum
		- runningSum[i] = sum(nums[0]...nums[i])

	Questions:
		1. what if the array is empty?
		2. can there be negative numbers?
		3. can there be duplicate numbers?
		4. Are we allowed use/modify the original array?

	Test Cases:
		input: [1,2,3,4]
		output: [1,3,6,10]

		input: [1,1,1,1]
		output: [1,2,3,4]

Match:
	- hashmap problem
	- summation problem

Plan:
	- use hashmap to store the running sum where key = index and value = running sum
	- iterate over the list and update the current position with running sum + current value
	- return the list
	- analysis:
		time complexity: O(n)
		space complexity: O(n)

Optimizations:
	- space complexity is O(n) due to the hashmap, can we reduce this to O(1)?
	- use a single variable to store the running sum and update it as we iterate over the list
	- analysis:
		time complexity: O(n)
		space complexity: O(1)

"""

def runningSum(nums):
	storedSum = {}
	storedSum[0] = nums[0]

	for i in range(1, len(nums)):
		storedSum[i] = storedSum[i-1]+nums[i]
		nums[i] = storedSum[i]

	return nums

def optimized_runningSum(nums):
	currSum = nums[0]
	for i in range(1, len(nums)):
		nums[i] += currSum
		currSum = nums[i]
	return nums

if __name__ == "__main__":
	print(runningSum([1,2,3,4]))
	print(runningSum([1,1,1,1]))
	print(optimized_runningSum([1,2,3,4]))
	print(optimized_runningSum([1,1,1,1]))