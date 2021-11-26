def isPalindrome(val):
    if val < 0:
        return False
    val = str(val)
    len_val = len(val)
    for i in range(len_val // 2):
        if val[i] != val[len_val - 1 - i]:
            return False
    return True

if __name__ == "__main__":
    testcases = [(123, False)]
    testcases.append((12321, True))
    testcases.append((-12321, False))
    testcases.append((111111111111111111111111111111111111111111111111111111111111111111111111111111, True))

    test_num = 1
    for test, result in testcases:
        assert isPalindrome(test) == result, "Test " + str(test_num) + " failed!"
        test_num+= 1