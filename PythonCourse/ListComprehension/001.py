temps = [221.0, 234.4, 340.5, 230.6]


def foo(lst):
    return sum([float(i) for i in lst])


sum = foo(temps)
print(sum)

# new_temps = []
#
# print(new_temps)