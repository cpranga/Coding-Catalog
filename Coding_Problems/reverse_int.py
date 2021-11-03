'''
Reverses a Signed 32-bit integer
if reversing x causes it to go out of range of [-2^31, 2^31 - 1] return 0
'''
def reverse_int(x):
    is_negative = 1
    if x < 0:
        is_negative = -1
        x *= -1
    reversed = 0
    while x > 0:
        reversed = (reversed * 10) + (x % 10)
        x //= 10
    if reversed >= 2**31 - 1:
        return 0
    return reversed * is_negative

testcases = [100, -100, 123456789, 1534236469]

for case in testcases:
    print(str(case) + " : " + str(reverse_int(case)))