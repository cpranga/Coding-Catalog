def shuffle(nums, n):
    shuffled = []
    for i in range(0, n):
        shuffled.append(nums[i])
        shuffled.append(nums[i + n])
    return shuffled

if __name__ == "__main__":
    testcases = []
    testcases.append(([2,5,1,3,4,7], [2,3,5,4,1,7]))
    testcases.append(([1,2],[1,2]))

    for test, result in testcases:
        assert shuffle(test, len(test)/2) == result