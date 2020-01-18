# -*- coding: utf-8 -*-

import numpy as np
df = {'ctl':list(np.random.normal(10,5,100)),
      'treat1':list(np.random.normal(15,5,100)),
      'treat2':list(np.random.normal(20,5,100)),
      'treat3':list(np.random.normal(30,5,100)),
      'treat4':list(np.random.normal(31,5,100))}
#组合成数据框
import pandas as pd
df = pd.DataFrame(df)
print(df.head())

df_melt = df.melt()
print(df_melt.head())

df_melt.columns = ['Treat','Value']
df_melt.head()

from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
model = ols('Value~C(Treat)',data=df_melt).fit()
anova_table = anova_lm(model, typ = 2)
print(anova_table)
