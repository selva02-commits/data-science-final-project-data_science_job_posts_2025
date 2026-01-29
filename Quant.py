import pandas as pdks

# Clean numeric columns first
def clean_numeric_columns(df):
    df = df.copy()
    
    # Salary: remove ₹, $, commas
    if 'salary' in df.columns:
        df['salary'] = (
            df['salary']
            .astype(str)
            .str.replace('[₹$,]', '', regex=True)
            .str.extract('(\d+)')[0]
            .astype(float)
        )

    # Company Size: extract numbers
    if 'company_size' in df.columns:
        df['company_size'] = (
            df['company_size']
            .astype(str)
            .str.extract('(\d+)')[0]
            .astype(float)
        )

    # Revenue: extract numbers
    if 'revenue' in df.columns:
        df['revenue'] = (
            df['revenue']
            .astype(str)
            .str.replace('[₹$,]', '', regex=True)
            .str.extract('(\d+)')[0]
            .astype(float)
        )
    
    return df

# -------------------- Outlier Functions --------------------
def salary_outliers(df):
    df = clean_numeric_columns(df)
    qt1 = df['salary'].quantile(0.25)
    qt3 = df['salary'].quantile(0.75)
    iqr = qt3 - qt1
    print(f"\nSalary IQR (Interquartile Range): {iqr}")
    
    Lower_Bound = qt1 - 1.5 * iqr  
    Upper_Bound = qt3 + 1.5 * iqr  
    outliers = df[(df['salary'] < Lower_Bound) | (df['salary'] > Upper_Bound)]
    print("\nSalary Outliers:")
    print(outliers)

def company_outliers(df):
    df = clean_numeric_columns(df)
    qt1 = df['company_size'].quantile(0.25)
    qt3 = df['company_size'].quantile(0.75)
    iqr = qt3 - qt1
    print(f"\nCompany Size IQR (Interquartile Range): {iqr}")
    
    Lower_Bound = qt1 - 1.5 * iqr  
    Upper_Bound = qt3 + 1.5 * iqr  
    outliers = df[(df['company_size'] < Lower_Bound) | (df['company_size'] > Upper_Bound)]
    print("\nCompany Size Outliers:")
    print(outliers)

def revenue_outliers(df):
    if 'revenue' not in df.columns:
        print("\nNo 'revenue' column in dataset.")
        return
    
    df = clean_numeric_columns(df)
    qt1 = df['revenue'].quantile(0.25)
    qt3 = df['revenue'].quantile(0.75)
    iqr = qt3 - qt1
    print(f"\nRevenue IQR (Interquartile Range): {iqr}")
    
    Lower_Bound = qt1 - 1.5 * iqr  
    Upper_Bound = qt3 + 1.5 * iqr  
    outliers = df[(df['revenue'] < Lower_Bound) | (df['revenue'] > Upper_Bound)]
    print("\nRevenue Outliers:")
    print(outliers)
