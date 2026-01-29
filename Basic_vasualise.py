import matplotlib.pyplot as pls
import pandas as pdks
import re

def Line_plot(df):
    # Filter relevant skills
    filtered = df[df["skills"].str.contains(
        'Go|Python|Rust|Ruby|Kotlin',
        case=False,
        na=False
    )].copy()

    # Drop rows with missing salary before processing
    filtered = filtered.dropna(subset=['salary'])

    # Clean and convert salary to float
    filtered['salary'] = (
        filtered['salary']
        .astype(str)
        .str.replace('[₹$,]', '', regex=True)
        .str.extract(r'(\d+(?:\.\d+)?)')[0]
        .astype(float)
    )

    # Capitalize skill names for better display
    filtered['skills'] = filtered['skills'].str.title()

    # Compute average salary per skill
    avg_salary = filtered.groupby('skills')['salary'].mean().sort_values()

    # Plotting
    pls.figure(figsize=(10, 6))
    pls.plot(
        avg_salary.index,
        avg_salary.values,
        marker='o',
        linestyle='-',
        color='teal'
    )
    pls.title('Line Plot: Average Salary Trend by Skill')
    pls.xlabel('Skills / Programming Language')
    pls.ylabel('Average Salary')
    pls.xticks(rotation=45, ha='right')
    pls.grid(True)
    pls.tight_layout()
    pls.show()

def Bar_plot(df):
    filtered = df[df["industry"].isin([
        'IT Services', 'Software', 'Technology', 'AI', 'Data'
    ])].copy()

    # Clean company_size column
    filtered['company_size'] = (
        filtered['company_size']
        .astype(str)
        .str.extract('(\d+)')[0]
        .astype(float)
    )

    # Remove missing values
    filtered = filtered.dropna(subset=['company_size'])

    industry_avg = (
        filtered
        .groupby('industry')['company_size']
        .mean()
        .sort_values()
    )

    pls.figure(figsize=(8, 5))
    pls.bar(
        industry_avg.index,
        industry_avg.values
    )

    pls.title('Bar Plot: Average Company Size by Industry')
    pls.xlabel('Industry')
    pls.ylabel('Average Company Size')
    pls.xticks(rotation=45)
    pls.show()


def hist_plot(df):
    df = df.copy()

    # Extract number of days from post_date
    days = (
        df['post_date']
        .astype(str)
        .str.extract(r'(\d+)')[0]
        .astype(float)
    )

    days = days.dropna()

    if days.empty:
        print("No valid posting-age data found.")
        return

    pls.figure(figsize=(8, 5))
    pls.hist(days, bins=10, edgecolor='black')

    pls.title('Histogram: Job Posting Age (Days)')
    pls.xlabel('Days Since Job Posted')
    pls.ylabel('Number of Job Posts')
    pls.show()