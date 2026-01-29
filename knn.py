def knn_modeling(df):
    # DO NOT read CSV again
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.metrics import accuracy_score, classification_report

    # Encode target (seniority_level)
    label_encoder = LabelEncoder()
    df['seniority_level'] = label_encoder.fit_transform(df['seniority_level'].astype(str))

    # Clean numeric-like columns (company_size, revenue, salary)
    def parse_salary(s):
        s = str(s).replace('€', '').replace(',', '')
        if '-' in s:
            low, high = s.split('-')
            return (float(low) + float(high)) / 2
        else:
            return float(s) if s.replace('.', '').isdigit() else None

    df['salary_clean'] = df['salary'].apply(parse_salary)

    df['company_size_clean'] = (
        df['company_size']
        .astype(str)
        .str.replace(',', '', regex=True)
        .str.extract(r'(\d+)')[0]
        .astype(float)
    )

    df['revenue_clean'] = (
        df['revenue']
        .astype(str)
        .str.replace('[€,]', '', regex=True)
        .str.replace('B', 'e9', regex=True)
        .str.replace('M', 'e6', regex=True)
        .str.extract(r'(\d+\.?\d*(?:e\d+)?)')[0]
        .astype(float)
    )

    # Features (X) and Target (y)
    X = df[['company_size_clean', 'revenue_clean', 'salary_clean']]
    y = df['seniority_level']

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X.fillna(0))

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # KNN classifier
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    # Predictions
    y_pred = knn.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))