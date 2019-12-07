import os
import warnings
import math
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
from sklearn.decomposition import PCA

warnings.filterwarnings("ignore")

arg_path = r'C:\Users\Administrator\Desktop\zzmpr\ARG.xlsx'
mge_path = r'C:\Users\Administrator\Desktop\zzmpr\MGE.xlsx'
phylum_path = r'C:\Users\Administrator\Desktop\zzmpr\Phylum.xlsx'
env_path = r'C:\Users\Administrator\Desktop\zzmpr\environment.xlsx'


def read_data(path, sheet: int or str):
    """
    read data for Excel,and return the data array,
    not include title
    """
    if not os.path.isfile(path):
        print("path error!")
        return None

    data = pd.read_excel(path, sheet)
    row = np.array(data)
    new_ = list()
    for i in row:
        new_.append(list(i[1:]))
    return np.array(new_)


def correlation(x, y, correlation_type=1, p_index=0, s_index=0):
    """
    calculate correlation coefficient,return the average value
    """
    p = []
    result = []
    for i in x:
        for j in y:
            if correlation_type == 1:
                p.append(pearsonr(i, j)[p_index])
            if correlation_type == 2:
                p.append(spearmanr(i, j)[s_index])
    for i in p:
        try:
            int(i)
            # result.append(abs(i))
            result.append(i)
        except:
            pass
    return abs(np.average(result))


def do_pca(array):
    pca = PCA(n_components=1, whiten=True)
    reduce = pca.fit_transform(array)
    # print(np.average(list(map(lambda x: abs(x), reduce))))
    return pca.explained_variance_ratio_


def re_correlation(x, y, correlation_type=1, p_index=0, s_index=0):
    p = []
    result = []
    for i in x:
        for j in y:
            if correlation_type == 1:
                p.append(pearsonr(i, j)[p_index])
            if correlation_type == 2:
                p.append(spearmanr(i, j)[s_index])
    p_matrix = np.array(p).reshape(len(x), len(y))

    for j in p_matrix:
        for i in j:
            try:
                int(i)
                # result.append(abs(i))
                result.append(i)
            except:
                pass
    try:
        p_new = np.array(result).reshape(len(p_matrix), int(len(result) / len(p_matrix)))
    except:
        p_new = np.array(result).reshape(len(p_matrix) - 1, int(len(result) / (len(p_matrix) - 1)))
    return do_pca(p_new)[0]


