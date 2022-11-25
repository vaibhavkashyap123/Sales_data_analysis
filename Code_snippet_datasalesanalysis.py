import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sw
store=pd.read_excel('data/superstore_sales.xlsx')
'''#sw.countplot(data=store,x='ship_mode')
#plt.show()
#datas=pd.DataFrame(store.groupby('ship_mode').count()['sales'])
# datas.to_csv('shipping.csv')
#sw.barplot(data=datas,x='ship_mode',y='sales')
#plt.show()
shipping=pd.read_csv('shipping.csv')
print(shipping)
#sw.countplot(data=shipping,x='ship_mode')
sw.barplot(data=shipping,x='ship_mode',y='sales')
plt.show()
'''
# most profitable Category
profitable_cat=pd.DataFrame(store.groupby(['category','sub_category']).sum()['profit'])
profitable=profitable_cat.sort_values(['category','profit'],ascending=False)
x=profitable.head(5)
print(x)



