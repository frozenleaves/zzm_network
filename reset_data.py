# -*- coding: utf-8 -*-

import random
import openpyxl as px
import pandas as pd
import numpy as np

raw_path = r"C:\Users\administrator\desktop\5.xlsx"
new_file = r"C:\Users\administrator\desktop\6.xlsx"

book = px.load_workbook(new_file)
sheet = book[book.sheetnames[0]]

MGEs = sheet[2]
Aminoglycoside = sheet[3]
Beta_Lactamase = sheet[4]
Chloramphenicol = sheet[5]
MLSB = sheet[6]
Multidrug = sheet[7]
Tetracycline = sheet[8]
Sulfonamide = sheet[9]
Vancomycin = sheet[10]
Others = sheet[11]
PH = sheet[12]
C_N = sheet[13]


def get_row_data(row):
    rd = [x.value for x in row]
    rd.pop(0)
    rdg = []
    index = 0
    for i in range(int(len(rd) / 3)):
        rdg.append((rd[index], rd[index + 1], rd[index + 2]))
        index += 3
    return rdg


key_list = [x.value for x in sheet['A']]
key_list.pop(0)
key_dict = dict(zip(key_list, [sheet[i] for i in range(2, 14)]))


class Data(object):
    def __init__(self, row, rad1, rad2):
        self.row = row
        self.rad1 = rad1
        self.rad2 = rad2

    def get_group_data(self):
        x1 = self.rad1
        x2 = self.row
        x3 = self.rad2
        return [x1, x2, x3]

    def __str__(self):
        return str(self.get_group_data())

    def __repr__(self):
        return str(self.get_group_data())


def set_dataframe(group_name):
    rdt = get_row_data(group_name)
    gp_list = [Data(x[0], x[1], x[2]).get_group_data() for x in rdt]
    return pd.DataFrame(np.array(gp_list).T)


def get_group_by_name(name):
    try:
        return key_dict[name]
    except:
        raise KeyError("No such Key named %s" % name)


def get_key():
    return key_list


if __name__ == '__main__':
    print(set_dataframe(Others))
