def maxSubArray(nums):
    subarray_cost = [0] * len(nums)
    subarray_cost[0] = nums[0]
    max_cost = subarray_cost[0]
    for cur_index in range(1, len(nums)):
        subarray_cost[cur_index] = max(nums[cur_index], nums[cur_index] + subarray_cost[cur_index - 1])
        if max_cost < subarray_cost[cur_index]:
            max_cost = subarray_cost[cur_index]
    return max_cost

if __name__ == "__main__":
    testcases = []
    testcases.append(([-2,1,-3,4,-1,2,1,-5,4], 6))
    testcases.append(([1], 1))
    testcases.append(([5,4,-1,7,8], 23))

    test_num = 1
    for test, result in testcases:
        assert maxSubArray(test) == result, "Test " + str(test_num) + " failed"
        test_num += 1