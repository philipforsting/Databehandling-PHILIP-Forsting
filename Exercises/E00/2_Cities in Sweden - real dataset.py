import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns # used for plotting 
import os

df_cities = pd.read_excel(io="Exercises/Data/komtopp50_2020.xlsx", sheet_name="Totalt", header=[5,6])
print(f"df_cities.head() \n{df_cities.head()}")
print(f"df_cities.info() \n{df_cities.info()}")
print(f"df_cities.describe() \n{df_cities.describe()}")
print(f"df_cities \n{df_cities}")


print(os.getcwd())  # visar var du "är" just nu