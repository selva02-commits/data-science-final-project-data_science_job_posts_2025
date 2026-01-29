# Display basic structure and sample job records
def explore_job_dataset(des):
    find_heads = des.head()
    print(f"\nFirst Five Job Records:\n{find_heads}") 
    informations = des.info()
    print(f"\nJob Dataset Information:\n{informations}")
# Generate statistical summary for numerical job attributes (salary)
def summarize_job_statistics(des):
    details = des.describe()
    print(f"\nStatistical Summary of Job Dataset:\n{details}")
# Identify missing values in job-related columns
def check_missing_job_values(des):
    miss1 = des.isnull().sum()
    print(f"\nMissing Values in Job Dataset:\n{miss1}")
# Remove incomplete and duplicate job postings
def clean_duplicate_and_missing_jobs(des):
    drops_values = des.dropna().drop_duplicates().isnull().sum()
    print(f"\nMissing Values After Cleaning Job Dataset:\n{drops_values}")
