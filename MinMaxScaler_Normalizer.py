from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer

def Standard_Scaler(df):
    numerics = df.select_dtypes(include='number')
    if numerics.empty:
        print("No numeric columns found to scale!")
        return df
    scaler = StandardScaler()
    df[numerics.columns] = scaler.fit_transform(numerics)
    print("\nStandard Scaler Applied Successfully")
    print(df[numerics.columns].head())
    return df


def Min_Max_Values(df):
    numerics = df.select_dtypes(include='number')
    if numerics.empty:
        print("No numeric columns found to scale!")
        return df
    scaler = MinMaxScaler()
    df[numerics.columns] = scaler.fit_transform(numerics)
    print("\nMin Max Scaler Applied Successfully")
    print(df[numerics.columns].head())
    return df


def normalizer_values(df):
    numerics = df.select_dtypes(include='number')
    if numerics.empty:
        print("No numeric columns found to normalize!")
        return df
    scaler = Normalizer()
    df[numerics.columns] = scaler.fit_transform(numerics)
    print("\nNormalizer Applied Successfully")
    print(df[numerics.columns].head())
    return df
