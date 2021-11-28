def pavlov_triangle(numRows):
    pavlov = []
    pavlov.append([1])
    prev_row = pavlov
    for row in range(2, numRows + 1):
        new_row = [1] * row
        for index in range(1, row - 1):
            new_row[index] = prev_row[index] + prev_row[index - 1]
        pavlov.append(new_row)
        prev_row = new_row
    print(pavlov)
    return pavlov

if __name__ == "__main__":
    testcases = []
    testcases.append((5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]))
    testcases.append((1, [[1]]))

    for test, result in testcases:
        assert pavlov_triangle(test) == result