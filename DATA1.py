import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path_to_file = "/Users/mariapapadopoulou/Downloads/DATA.xml.csv"
df = pd.read_csv(path_to_file)
product = df.groupby(['zip_code', 'item_description', 'store_number']).aggregate({'bottles_sold': 'sum'})
print(product)
product_prc = product.groupby(level=['store_number']).apply(lambda x:
                                                            100 * x / float(x.sum()))
print(product_prc)
