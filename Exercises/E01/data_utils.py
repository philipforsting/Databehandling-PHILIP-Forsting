import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns # used for plotting 

def NanPlotter(df):
    df_NaN = df.loc[:, df.isna().any()].isnull().sum()
    df_NaN = df_NaN.reset_index()
    df_NaN.columns = ["Column", "Count"]
    sns.barplot(data=df_NaN, x="Column", y="Count", palette='pastel', hue="Column")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.title("Null values:")
    plt.show()