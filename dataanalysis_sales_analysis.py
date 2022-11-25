import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sw
'''
Questions We Ask
-------------------------------------------------------------------------------------
1.Trends (graph between sales and years,months)
2.Top 10 selling products by sales
3.Top 10 selling products by quantity
4.Top 10 selling products by quantity and region
5.most preffered shipping type
6.Top 10 profitable Category and subcategory
--------------------------------------------------------------------------------------
'''
store=pd.read_excel('data/superstore_sales.xlsx')
# top 5 records
top5=store.head(5)
print(top5)
# bottom 5 records
bottoms=store.tail(5)
print(bottoms)
# shape of the dataset
shape=store.shape
print(shape)
# columns of the dataset
cols=store.columns
print(cols)
# info of the dataset
info=store.info()
print(info)
# cleaning and wrangling the data
nulls=store.isnull().sum()
print(nulls)
#for describing the data
desc=store.describe()
print(desc)
# the min date
min_date=store['order_date'].min()
print(min_date)
# the maximum date
max_date=store['order_date'].max()
print(max_date)
# the dates orders
# trends years and sales
store['Month Year']=store['order_date'].apply(lambda  x:x.strftime('%Y-%m'))
trend=store.groupby('Month Year').sum()['sales'].reset_index()
print(trend)
sw.lineplot(data=trend,x='Month Year',y='sales',color='#8B0000')
plt.xlabel('Month Year')
plt.ylabel('Sales')
plt.title('Month Year Vs Sales Lineplot',fontsize=15,color='#000080')
plt.xticks(rotation='vertical',size=8)
plt.show()
# top 10 products for sales
prods=pd.DataFrame(store.groupby('product_name').sum()['sales'])
tops=prods.sort_values('sales',ascending=False)
top_ten=tops.head(10)
#top_ten.to_csv('topten_selling_bysales.csv')
print(top_ten)
# top 10 selling products by quantity
selling=pd.DataFrame(store.groupby('product_name').sum()['quantity'])
sells=selling.sort_values('quantity',ascending=False)
top_ten_sell=sells.head(10)
#top_ten_sell.to_csv('top_tenselling_by_quantity.csv')
print(top_ten_sell)
#top 10 selling products by quantity and region
sellings=pd.DataFrame(store.groupby(['product_name','region']).sum()['quantity'])
sortes=sellings.sort_values('quantity',ascending=False)
topss=sortes[:10]
print(topss)
#most preffered source of shipping
most=store.groupby('ship_mode').max()
print(most)
store=pd.read_excel('data/superstore_sales.xlsx')
sw.countplot(data=store,x='ship_mode')
plt.xlabel('Shipping Type')
plt.ylabel('Sales By diffrent Shipping Type')
plt.show()
#datas=pd.DataFrame(store.groupby('ship_mode').count()['sales'])
# datas.to_csv('shipping.csv')
#sw.barplot(data=datas,x='ship_mode',y='sales')
#plt.show()
shipping=pd.read_csv('shipping.csv')
print(shipping)
#sw.countplot(data=shipping,x='ship_mode')
sw.barplot(data=shipping,x='ship_mode',y='sales')
plt.xlabel('Shipping')
plt.ylabel('Sales by diffrent Shipping Types')
plt.show()
#Most top 10 profitable category and subCategory
profitable_cat=pd.DataFrame(store.groupby(['category','sub_category']).sum()['profit'])
profitable=profitable_cat.sort_values(['category','profit'],ascending=False)
x=profitable.head(10)
print(x)










