import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def KMeans_clustering(data):
    # Convert input data to DataFrame
    df = pd.DataFrame(data)

    # ------------------- Clean numeric columns -------------------
    # Clean company_size
    df['company_size_clean'] = (
        df['company_size']
        .astype(str)
        .str.replace(',', '', regex=True)
        .str.extract(r'(\d+)')[0]
        .astype(float)
    )

    # Clean revenue (convert B/M to numeric)
    df['revenue_clean'] = (
        df['revenue']
        .astype(str)
        .str.replace('[€,]', '', regex=True)
        .str.replace('B', 'e9', regex=True)
        .str.replace('M', 'e6', regex=True)
        .str.extract(r'(\d+\.?\d*(?:e\d+)?)')[0]
        .astype(float)
    )

    # Clean salary (take average if range is given)
    def parse_salary(s):
        s = str(s).replace('€', '').replace(',', '')
        if '-' in s:
            low, high = s.split('-')
            return (float(low) + float(high)) / 2
        else:
            return float(s) if s.replace('.', '').isdigit() else None

    df['salary_clean'] = df['salary'].apply(parse_salary)

    # ------------------- Select features for clustering -------------------
    X = df[['company_size_clean', 'revenue_clean', 'salary_clean']].fillna(0)

    # Standardize the data
    scaler = StandardScaler()
    scaled = scaler.fit_transform(X)

    # Apply k-Means clustering
    kmeans = KMeans(n_clusters=3, random_state=98)
    df['Cluster'] = kmeans.fit_predict(scaled)

    # ------------------- Scatter Plot -------------------
    plt.figure(figsize=(8, 6))
    plt.scatter(
        df['company_size_clean'],
        df['salary_clean'],
        c=df['Cluster'],
        cmap='viridis',
        s=100
    )

    plt.xlabel("Company Size")
    plt.ylabel("Average Salary")
    plt.title("k-Means Clustering of Jobs (Scatter Plot)")
    plt.colorbar(label="Cluster")
    plt.tight_layout()
    plt.show()
    # ----------------------------------------------------

    # Display Cluster-wise Data
    print("Cluster 1 Data (Small companies / lower salaries):")
    print(df[df['Cluster'] == 0])

    print("\nCluster 2 Data (Mid-range companies / salaries):")
    print(df[df['Cluster'] == 1])

    print("\nCluster 3 Data (Large companies / high salaries):")
    print(df[df['Cluster'] == 2])

    print("\nComplete Data with Cluster Labels:")
    print(df)

    return df