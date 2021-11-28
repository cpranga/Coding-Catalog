def pavlov_triangle(rowIndex):
    new_row = []
    for row in range(0, rowIndex + 2):
        new_row = [1] * row
        for index in range(1, row - 1):
            new_row[index] = prev_row[index] + prev_row[index - 1]
        prev_row = new_row
    print(new_row)
    return new_row

if __name__ == "__main__":
    testcases = []
    testcases.append((3, [1,3,3,1]))
    testcases.append((1, [1,1]))

    test_num = 1
    for test, result in testcases:
        assert pavlov_triangle(test) == result, "Test " + str(test_num) + " failed!"
        test_num += 1