def isPalindrome(x):
    if x < 0:
        return False
    reversed = 0
    copy = x
    while copy > 0:
        reversed *= 10
        reversed += (copy % 10)
        copy //= 10
    return reversed == x

if __name__ == "__main__":
    testcases = [(123, False)]
    testcases.append((12321, True))
    testcases.append((-12321, False))
    testcases.append((111111111111111111111111111111111111111111111111111111111111111111111111111111, True))

    test_num = 1
    for test, result in testcases:
        assert isPalindrome(test) == result, "Test " + str(test_num) + " failed!"
        test_num+= 1