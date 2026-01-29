import pandas as pd

def Descrips(df):
    df = df.copy()

    # Convert salary column
    if 'salary' in df.columns:
        df['salary'] = (
            df['salary']
            .astype(str)
            .str.replace(',', '')
            .str.extract('(\d+)')[0]
            .astype(float)
        )

    # Convert company_size column
    if 'company_size' in df.columns:
        df['company_size'] = (
            df['company_size']
            .astype(str)
            .str.extract('(\d+)')[0]
            .astype(float)
        )

    # Select numeric columns
    cols = df.select_dtypes(include='number').columns

    if cols.empty:
        print("No numeric columns found for descriptive statistics.")
        return

    for c in cols:
        print(f"\nStatistics for {c}")
        print("Mean   :", df[c].mean())
        print("Median :", df[c].median())
        print("Mode   :", df[c].mode().iloc[0])
        print("Std Dev:", df[c].std())

