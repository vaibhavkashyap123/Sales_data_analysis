Sales Analysis of An Supermarket by python tools and libraries
Questions We Ask

Trends (graph between sales and years,months)
Top 10 selling products by sales
Top 10 selling products by quantity
Top 10 selling products by quantity and region
most preffered shipping type
Top 10 profitable Category and subcategory

Libraries We used
Seaborn --for plotting techniques
matplotlib.pyplot---for also plotting 
pandas ---for reading the csv and makes dataframes

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sw
#import the data
store=pd.read_excel('data/superstore_sales.xlsx')
