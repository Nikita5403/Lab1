nums = list(map(int, input("enter numbers separated by spaces: ").split()))
for n in nums:
    tens_digit = (n // 10) % 10
    print(tens_digit)