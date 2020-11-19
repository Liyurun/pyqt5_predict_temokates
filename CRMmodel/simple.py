import pandas as pd
from CRM import CRM
import numpy as np
import time

t1 = time.time()
df = pd.read_excel('./data/test2.xlsx')
time1 = df.iloc[:,0].values
prod1 = df.iloc[:,2:].values
inj1 = df.iloc[:,1].values.reshape([-1,1])
# xx = np.array(list(range(len(time1))))
# inj1 = np.column_stack((inj1,xx))



crm = CRM(tau_selection='per-pair', constraints='up-to one')
crm.fit(prod1, inj1, time1,num_cores=1,options={'maxiter':1000,'gtol': 1e-7})
q_hat = crm.predict()
residuals = crm.residual()
crm.to_excel('res.xlsx')
crm.to_fig(q_hat)
t2 = time.time()
print('time used ',t2-t1)