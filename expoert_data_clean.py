def export_cleaned_job_data(exp):
    cleaned_data = exp.dropna()
    cleaned_data.to_csv('job_data_cleaned.csv', index=False)
   
