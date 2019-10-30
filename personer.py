# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
from scipy.stats import pearsonr


def get_data():
    """读取Excel，返回数据表"""
    data = pd.read_excel("C:\\users\\administrator\\desktop\\all_data.xlsx")
    row = np.array(data)
    new_ = list()
    for i in row:
        new_.append(list(i[1:]))
    return np.array(new_)


def do_pearson(data, flag=True):
    date = data
    r_coefficient = list()
    p_coefficient = list()
    if flag:
        for i in date:
            for j in date:
                pr = pearsonr(i, j)
                if pr[0] >= 0.9:
                    p_coefficient.append(pr[0])
                else:
                    p_coefficient.append(pr[0])
                if pr[1] <= 0.05:
                    r_coefficient.append(pr[1])
                else:
                    r_coefficient.append(pr[1])
        # if flag:
        r_array = np.array(r_coefficient).reshape(240, 240)
        p_array = np.array(p_coefficient).reshape(240, 240)
    else:
        r_array = np.array(r_coefficient).reshape(10, 10)
        p_array = np.array(p_coefficient).reshape(10, 10)
    return r_array, p_array


def p_g_pearson():
    """calculate phylum and genes pearson data"""

    all_data = get_data()

    g_data = all_data[:228]

    p_data = all_data[228:]

    p = list()
    r = list()

    for phy in p_data:
        for gen in g_data:
            p_, r_ = pearsonr(phy, gen)
            p.append(p_)
            r.append(r_)

    p_ret = np.array(p).reshape(len(p_data), len(g_data))
    r_ret = np.array(r).reshape(len(p_data), len(g_data))

    return  p_ret, r_ret

if __name__ == '__main__':
    d = do_pearson(get_data())
    fin1 = pd.DataFrame(d[0])
    fin2 = pd.DataFrame(d[1])
    #
    fin1.to_excel(r'C:\users\administrator\desktop\rb.xlsx')
    fin2.to_excel(r'C:\users\administrator\desktop\pb.xlsx')

    # ret = p_g_pearson()
    #
    # pd.DataFrame(ret[0]).to_excel('C:\\users\\administrator\\desktop\\p_new.xlsx')
    # pd.DataFrame(ret[1]).to_excel('C:\\users\\administrator\\desktop\\r_new.xlsx')