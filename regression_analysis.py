import openpyxl as px
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

book = px.load_workbook(r"C:\Users\Administrator\Desktop\周泽明\analysis_data.xlsx")
sheet = book[book.sheetnames[0]]

arg = list(map(lambda i: i.value, sheet[2]))
mge = list(map(lambda i: i.value, sheet[3]))


def get_data(index, flag=1):
    data = list(map(lambda i: i.value, sheet[index]))
    data.pop(0)
    if flag == 1:
        return data[:4]
    if flag == 2:
        return data[4:]


ap = []

for i in range(3, 13):
    ap.append(pearsonr(get_data(2, flag=2), get_data(i, flag=2))[0])

mge_percent = ap[0]
env_percent = sum(list(map(lambda x: abs(x), ap[1:]))) / len(ap[1:])

bp = []

for i in range(3, 13):
    bp.append(pearsonr(get_data(2), get_data(i))[0])

mge_percent_b = bp[0]
env_percent_b = sum(list(map(lambda x: abs(x), bp[1:]))) / len(bp[1:])

print("before: ", mge_percent_b / (mge_percent_b + env_percent_b))
print("after: ", mge_percent / (mge_percent + env_percent))
