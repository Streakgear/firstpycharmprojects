import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import cm as cm



data = pd.read_csv("middle_tn_schools.csv")




df = pd.DataFrame(data)
cols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
df = df[df.columns[cols]]
fd = pd.DataFrame(data)
cols1 = [1,3]
fd = fd[df.columns[cols1]]

fd.groupby(['school_rating'])

fd.describe()

df.groupby(['school_rating'])

df.describe()


print(fd.corr())



# ax1 = plt.scatter(df.school_rating,df.reduced_lunch,c='species',colormap='viridis')
ax1 = df.plot.scatter(x=3,y=6,c=2,colormap='viridis')

plt.show()
sns.heatmap(df.corr(),cmap='RdBu',vmax=-1,vmin=1)
plt.show()

