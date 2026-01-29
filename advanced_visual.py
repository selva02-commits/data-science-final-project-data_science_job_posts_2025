import pandas as pd
import numpy as np

import seaborn as sdm
import matplotlib.pyplot as plt

def clean_numeric_columns(df):
    # Clean salary
    df['salary'] = (
        df['salary']
        .astype(str)
        .str.replace('[₹$,]', '', regex=True)
        .str.extract('(\d+)')[0]
        .astype(float)
    )

    # Convert company_size to approximate numeric
    df['company_size'] = (
        df['company_size']
        .astype(str)
        .str.extract('(\d+)')[0]
        .astype(float)
    )

    # Convert revenue to numeric
    df['revenue'] = (
        df['revenue']
        .astype(str)
        .str.replace('[₹$,]', '', regex=True)
        .str.extract('(\d+)')[0]
        .astype(float)
    )

    return df

# 1️ PAIR PLOT
def Pair_plot(df):
    df = clean_numeric_columns(df)
    df = df.dropna(subset=['salary', 'company_size', 'revenue'])

    sorted_df = df.sort_values(by='salary')

    sdm.pairplot(
        sorted_df[['salary', 'company_size', 'revenue']]
    )

    plt.suptitle(
        'Pair Plot of Salary, Company Size, and Revenue',
        y=1.02
    )
    plt.show()


# 2️ CORRELATION HEATMAP
def Heat_plot(df):
    df = clean_numeric_columns(df)

    plt.figure(figsize=(4, 6))
    sdm.heatmap(
        df[['salary', 'company_size', 'revenue']].corr(),
        annot=True,
        cmap='coolwarm'
    )

    plt.title('Heatmap of Correlations')
    plt.show()


# 3️ COVARIANCE HEATMAP
def Heat_cov(df):
    df = clean_numeric_columns(df)

    plt.figure(figsize=(4, 6))
    sdm.heatmap(
        df[['salary', 'company_size', 'revenue']].cov(),
        annot=True,
        cmap='coolwarm',
        fmt=".2f"
    )

    plt.title('Heatmap of Covariance')
    plt.show()
