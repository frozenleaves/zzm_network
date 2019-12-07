from sklearn.decomposition import PCA
import pandas as pd
import numpy as np


path1 = r'C:\users\administrator\desktop\zzmpr\堆肥前ARGp.xlsx'
path2 = r'C:\users\administrator\desktop\zzmpr\堆肥后ARGp.xlsx'
path3 = r'C:\users\administrator\desktop\zzmpr\堆肥前MGEp.xlsx'
path4 = r'C:\users\administrator\desktop\zzmpr\堆肥后MGEp.xlsx'
path5 = r'C:\users\administrator\desktop\zzmpr\0p.xlsx'

path = [path1, path2, path3, path4]
# book = px.load_workbook(path)
# sheet = book[book.sheetnames[0]]

def do_pca(data_path):
    p_data = pd.read_excel(data_path)
    row = np.array(p_data)
    new_ = list()
    for i in row:
        new_.append(list(i[1:]))
    # return new_
    pca = PCA(n_components=1, whiten=True)
    reduced_x = pca.fit_transform(np.array(new_))
    print(reduced_x)
    print(pca.explained_variance_ratio_)
    return reduced_x, pca.explained_variance_ratio_

if __name__ == '__main__':
    # do_pca(path2)
    with open("env_before.txt", 'w') as f:
        f.write(str(do_pca(path5)))