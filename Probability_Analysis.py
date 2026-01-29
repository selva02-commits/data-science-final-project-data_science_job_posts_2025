import pandas as pd
import matplotlib.pyplot as plt

def preprocess_dataset(df):
    """
    Cleans and converts company_size, revenue, and salary into numeric values.
    """
    # Clean company_size (remove commas, convert to float)
    df['company_size'] = (
        df['company_size']
        .astype(str)
        .str.replace(',', '', regex=True)
        .str.extract(r'(\d+)')[0]
        .astype(float)
    )

    # Clean revenue (remove €, B, M, convert to float in billions)
    df['revenue'] = (
        df['revenue']
        .astype(str)
        .str.replace('[€,]', '', regex=True)
        .str.replace('B', 'e9', regex=True)
        .str.replace('M', 'e6', regex=True)
        .str.extract(r'(\d+\.?\d*(?:e\d+)?)')[0]
        .astype(float)
    )

    # Clean salary (handle ranges, take average)
    def parse_salary(s):
        s = str(s).replace('€', '').replace(',', '')
        if '-' in s:
            low, high = s.split('-')
            return (float(low) + float(high)) / 2
        else:
            return float(s) if s.replace('.', '').isdigit() else None

    df['salary'] = df['salary'].apply(parse_salary)

    return df
def range_stats(datasets):
    """
    Calculates Range and Variance for cleaned numeric features.
    """
    numeric_cols = ['company_size', 'revenue', 'salary']  # explicitly use your dataset columns
    
    for col in numeric_cols:
        rng = datasets[col].max() - datasets[col].min()
        var = datasets[col].var()
        
        print(f"\nStatistics for '{col}':")
        print(f"  Range    : {rng:.2f}")
        print(f"  Variance : {var:.2f}")


def hist_rang(datasets):
    """
    Visualizes probability distributions for numeric features using histograms.
    """
    numeric_cols = ['company_size', 'revenue', 'salary']  # explicitly use your dataset columns
    
    for col in numeric_cols:
        plt.figure(figsize=(8, 5))
        plt.hist(datasets[col].dropna(), bins=10, density=True, edgecolor='black', color='skyblue')
        plt.title(f"Probability Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Probability Density")
        plt.grid(True)
        plt.tight_layout()
        plt.show()