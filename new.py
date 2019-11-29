# x = {'1': [2000, 10000000], '2': [2350, 10000000], '3': [2000, 10000000], '4': [3100, 150000400], '5': [3100, 15000000], '7': [3100, 15000000]}


cablink = {'1': ['cablink1', 'cablink1'], '2': ['cablink1', 'cablink1'], '3': ['cablink1', 'cablink1'], '4': ['cablink4', 'cablink4'], '5': ['cablink5', 'cablink5'], '7': ['cablink6', 'cablink5']}


x = {'1': [2000, 10000000], '2': [2000, 10000000], '3': [2000, 10000000], '4': [3100, 150000400], '5': [3100, 15000000], '7': [3100, 15000000]}
y = {}



def FIND_KEYS_WITH_THE_SAME_VALUES_IN_DIC_AND_RETURN_LISTS_OF_KEYS():
    for cell, cell_info in x.items():
        y.setdefault(repr(cell_info), []).append(cell)
    identical_cells = [item for item in list(y.values()) if len(item) > 1]
    return identical_cells

identical_cells = FIND_KEYS_WITH_THE_SAME_VALUES_IN_DIC_AND_RETURN_LISTS_OF_KEYS()

def CHECK_IF_IDENTICAL_CELLS_HAVE_THE_SAME_CABLINK_IN_CHANELL():
    for cell_group in identical_cells:
        if len(cell_group) == 3:
            x = cablink.get(str(cell_group[0]))
            y = cablink.get(str(cell_group[1]))
            z = cablink.get(str(cell_group[2]))
            if x ==y ==z:
                assert True == True
            else:
                print('Different cablinks!' + str(x) + str(y) + str(z))
                assert True == False
        elif len(cell_group) == 2:
            x = cablink.get(str(cell_group[0]))
            y = cablink.get(str(cell_group[1]))
            if x ==y:
                assert True == True
            else:
                print('Different cablinks for cells: ' +str(cell_group) + " Cablinks: " + str(x) + str(y))
                assert True == False



CHECK_IF_IDENTICAL_CELLS_HAVE_THE_SAME_CABLINK_IN_CHANELL()













# for cell_group in identical_cells:
#     if len(cell_group) == 3:
#         x = cablink.get(str(cell_group[0]))
#         y = cablink.get(str(cell_group[1]))
#         z = cablink.get(str(cell_group[2]))
#         if x ==y == z:
#             print("TEST PASSED")
#         else:
#             print("TEST FAILED")
#     elif len(cell_group) == 2:
#         x = cablink.get(str(cell_group[0]))
#         y = cablink.get(str(cell_group[1]))
#         if x == y:
#             print("TEST PASSED")
#         else:
#             print("TEST FAILED")








# def create_cell_key_value(x):
#     cell_values = list(x.values())
#     cell_keys = list(x.keys())
#     return cell_values, cell_keys
#
# cell_values, cell_keys = create_cell_key_value(x)
#
# def create_mapping(cell_keys):
#     mapping = {}
#     for c, index in enumerate(cell_keys, 1):
#         dic = {c: index}
#         mapping.update(dic)
#     return mapping
#
# def find_indentical_cells(cell_values):
# #     length = len(cell_values)
# #     identicalCells = []
# #     for i in range(length):
# #         y = i+1
# #         while y < length:
# #             if cell_values[i] == cell_values[y]:
# #                 identicalCells.append([i+1, y+1])
# #             y= y+1
# #     return identicalCells
#
# def create_identical_cells_list():
#     mapping = create_mapping(cell_keys)
#     identicalCells = find_indentical_cells(cell_values)
#     for item in identicalCells:
#         item[0]= mapping[item[0]]
#         item[1]= mapping[item[1]]
#     return identicalCells
#
# identicalCells = create_identical_cells_list()
#
#
# print("Pary celek o takim samym earfcn: " + str(identicalCells))
#
# for cells in identicalCells:
#     x = cablink.get(str(cells[0]))
#     print(cells)
#     print(str(cells[0]))
#     print(x)
#     y = cablink.get(str(cells[1]))
#     if x == y:
#         print("TEST PASSED")
#     else:
#         print("TEST FAILED")











# y = {}
# for cell, cell_info in x.items():
#     if repr(cell_info) in y:
#         y[repr(cell_info)].append(cell)
#     else:
#         y[repr(cell_info)] = [cell]
# x = list(y.values())
# print(x)