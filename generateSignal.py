

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0.0, 1.9998e-06, 10000)
trig=np.zeros(np.shape(t))
sig=np.zeros(np.shape(t))
print(len(sig))
plt.plot(t,sig)
plt.show()
writeStr='Time,Trigger,Signal\nsec,V,V\n'
for i, tVal in enumerate(t):
    writeStr=writeStr+str(t[i])+','+str(trig[i]) + ','+ str(sig[i])
    if i != len(t)-1:
        writeStr=writeStr+'\n'
with open('zeroData.txt', 'w+') as f:
    f.write(writeStr)
    



# Time,Trigger,Signal
# sec,V,V