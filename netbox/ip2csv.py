from openpyxl import load_workbook
import sys

sys.stdout = open('out.log', 'w')

wb = load_workbook('1.xlsx')
sheet = wb['2']

def getvalue(x):
    return x.value

list_1 = list(map(getvalue, sheet['A'][2:]))
list_2 = list(map(getvalue, sheet['C'][2:]))
list_3 = list(map(getvalue, sheet['D'][2:]))
list_4 = list(map(getvalue, sheet['E'][2:]))
list_5 = list(map(getvalue, sheet['F'][2:]))

print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_5)