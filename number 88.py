import sys
for line in sys.stdin:
    num = int(line.strip())
    digit_sum = 0
    while num > 0:
        digit_sum += num %10
        num //=10
        print(digit_sum)