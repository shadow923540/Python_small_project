x = {'1': [2000, 10000000], '2': [2350, 10000000], '3': [2000, 10000000], '4': [3100, 150000400], '5': [3100, 15000000], '7': [3100, 15000000]}

def create_cell_key_value(x):
    cell_values = list(x.values())
    cell_numbers = list(x.keys())
    return cell_values, cell_numbers

cell_values, cell_numbers = create_cell_key_value(x)

def create_mapping(cell_numbers):
    mapping = {}
    for c, index in enumerate(cell_numbers, 1):
        dic = {c: index}
        mapping.update(dic)
    return mapping

def find_indentical_cells(cell_values):
    length = len(cell_values)
    identicalCells = []
    for i in range(length):
        y = i+1
        while y < length:
            if cell_values[i] == cell_values[y]:
                identicalCells.append([i+1, y+1])
            y= y+1
    return identicalCells

def create_identical_cells_list():
    mapping = create_mapping(cell_numbers)
    identicalCells = find_indentical_cells(cell_values)
    for item in identicalCells:
        item[0]= mapping[item[0]]
        item[1]= mapping[item[1]]
    return identicalCells

identicalCells = create_identical_cells_list()


cablink = {'1': ['cablink1', 'cablink1'], '2': ['cablink2', 'cablink2'], '3': ['cablink1', 'cablink1'], '4': ['cablink4', 'cablink4'], '5': ['cablink5', 'cablink5'], '7': ['cablink6', 'cablink5']}
print("Pary celek o takim samym earfcn: " + str(identicalCells))

for cells in identicalCells:
    x = cablink.get(str(cells[0]))
    y = cablink.get(str(cells[1]))
    if x == y:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
