from datetime import datetime

def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    date1 = datetime(year=a[0], month=a[1], day=a[2])
    date2 = datetime(year=b[0], month=b[1], day=b[2])
    #print((date2 - date1).days)
    return abs((date2 - date1).days)


print("Example:")
print(days_diff((1982, 4, 19), (1982, 4, 22)))

assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

print("The mission is done! Click 'Check Solution' to earn rewards!")
