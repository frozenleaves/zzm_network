# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import reset_data

path = r"C:\users\administrator\desktop\anova.xlsx"


def read_data(file=r"C:\users\administrator\desktop\7.xlsx") -> 'a tuple with pd.DataFrame':
    """read data file, return DataFrame"""
    import openpyxl as px
    book = px.load_workbook(file)
    sheet = book[book.sheetnames[0]]
    phs = sheet[2]
    cns = sheet[3]
    phu = [x.value for x in phs[0: int(len(phs) / 2)]]
    phc = [y.value for y in phs[int(len(phs) / 2):]]
    cnu = [x.value for x in cns[0: int(len(cns) / 2)]]
    cnc = [y.value for y in cns[int(len(cns) / 2):]]

    phu1 = [phu[:3], phu[3:6], phu[6:9], phu[9:12]]
    phc1 = [phc[:3], phc[3:6], phc[6:9], phc[9:12]]
    cnu1 = [cnu[:3], cnu[3:6], cnu[6:9], cnu[9:12]]
    cnc1 = [cnc[:3], cnc[3:6], cnc[6:9], cnc[9:12]]
    ph = pd.DataFrame(np.array([phu, phc]).T)
    cn = pd.DataFrame(np.array([cnu, cnc]).T)
    return pd.DataFrame(np.array(phu1).T), pd.DataFrame(np.array(phc1).T), \
           pd.DataFrame(np.array(cnu1).T), pd.DataFrame(np.array(cnc1).T),ph, cn


def do_anove(ary: 'pd.DataFrame'):
    """anove,return a table"""

    df_melt = ary.melt()
    df_melt.columns = ['Sample', 'Target']
    from statsmodels.formula.api import ols
    from statsmodels.stats.anova import anova_lm

    model = ols('Target~C(Sample)', data=df_melt).fit()
    anova_table = anova_lm(model, typ=2)
    return anova_table


def draw(data: 'pd.DataFrame'):
    import matplotlib.pyplot as plt
    data.boxplot(grid=False)
    plt.show()


def compare(group_name) -> 'list':
    group = reset_data.get_group_by_name(group_name)
    gp_data = reset_data.set_dataframe(group)
    d_list = list()
    d_list.append(pd.DataFrame(np.array([list(gp_data[0]), list(gp_data[1])]).T))
    d_list.append(pd.DataFrame(np.array([list(gp_data[2]), list(gp_data[3])]).T))
    d_list.append(pd.DataFrame(np.array([list(gp_data[4]), list(gp_data[5])]).T))
    d_list.append(pd.DataFrame(np.array([list(gp_data[6]), list(gp_data[7])]).T))

    return d_list


def write_result(group_name, file):
    data = compare(group_name)
    cm = do_anove(data[0])
    ec = do_anove(data[1])
    cd = do_anove(data[2])
    sm = do_anove(data[3])
    with open(file, 'w') as f:
        content = """"""
        content += "CMU-CMC\n"
        content += str(cm) + '\n'
        content += "ECU-ECC\n"
        content += str(ec) + '\n'
        content += "CDU-CDC\n"
        content += str(cd) + '\n'
        content += "SMU-SMC\n"
        content += str(sm) + '\n'
        f.write(content)


if __name__ == '__main__':
    # for k in reset_data.key_list:
    #     write_result(k, './result/' + k + '.txt')
    dt = read_data()
    # ph_u = dt[0]
    # ph_c = dt[1]
    # cn_u = dt[2]
    # cn_c = dt[3]
    print("PH U")
    print(do_anove(dt[0]), '\n')
    print('PH C')
    print(do_anove(dt[1]), '\n')
    print("CN U")
    print(do_anove(dt[2]), '\n')
    print('CN C')
    print(do_anove(dt[3]), '\n')
    print("PH 前后比较")
    print(do_anove(dt[4]), '\n')
    print("C/N 前后比较")
    print(do_anove(dt[5]), '\n')


