def isPalindrome(val):
    if val < 0:
        return False
    stack = []
    queue = []
    while val > 0:
        pop = val % 10
        val = val // 10
        stack.append(pop)
        queue.append(pop)
    
    while stack or queue:
        if stack.pop(0) != queue.pop():
            return False
    return (not stack) == (not queue)

if __name__ == "__main__":
    testcases = [(123, False)]
    testcases.append((12321, True))
    testcases.append((-12321, False))
    testcases.append((111111111111111111111111111111111111111111111111111111111111111111111111111111, True))

    test_num = 1
    for test, result in testcases:
        assert isPalindrome(test) == result, "Test " + str(test_num) + " failed!"
        test_num+= 1