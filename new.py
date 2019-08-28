# x = {'1': [2000, 10000000], '2': [2350, 10000000], '3': [2000, 10000000], '4': [3100, 150000400], '5': [3100, 15000000], '7': [3100, 15000000]}
# #
# #
# cell_numbers = list(x.keys())
# print(cell_numbers)
# cell_values = list(x.values())
#
#
#
# x = len(cell_values)
#
# identicalCells = []
# for i in range(x):
#     y = i+1
#     while y < x:
#         if cell_values[i] == cell_values[y]:
#             identicalCells.append([i+1, y+1])
#         y= y+1
# print(identicalCells)


















x = {'1': [2000, 10000000], '2': [2350, 10000000], '3': [2000, 10000000], '4': [3100, 150000400], '5': [3100, 15000000], '7': [3100, 15000000]}
#
#

cell_values = list(x.values())




def getList(dict):
    list_value = []
    x = list(dict.keys())
    for value in x:
        list_value.append(int(value))
    return list_value

def create_mapping():
    mapping = {}
    cell_numbers = getList(x)
    for c, index in enumerate(cell_numbers, 1):
        dic = {c: index}
        mapping.update(dic)
    return mapping

mapping = create_mapping()



x = len(cell_values)

identicalCells = []
for i in range(x):
    y = i+1
    while y < x:
        if cell_values[i] == cell_values[y]:
            identicalCells.append([i+1, y+1])
        y= y+1

for item in identicalCells:
    item[0]= mapping[item[0]]
    item[1] = mapping[item[1]]


print(identicalCells)

