from dataset_import import dataload
from Data_Clean import explore_job_dataset, summarize_job_statistics, check_missing_job_values,clean_duplicate_and_missing_jobs
from expoert_data_clean import export_cleaned_job_data
from MinMaxScaler_Normalizer import Standard_Scaler, Min_Max_Values, normalizer_values
from Quant import salary_outliers,  company_outliers, revenue_outliers
from Statitics import Descrips
from Basic_vasualise import Line_plot, Bar_plot, hist_plot
from advanced_visual import Pair_plot, Heat_plot, Heat_cov
from dashboard import Dash_board
from Probability_Analysis import range_stats, hist_rang
from knn import knn_modeling
from k_means import KMeans_clustering

datas = dataload()
explore_job_dataset(datas)
summarize_job_statistics(datas)
check_missing_job_values(datas)
clean_duplicate_and_missing_jobs(datas)
Standard_Scaler(datas)
Min_Max_Values(datas)
normalizer_values(datas)
salary_outliers(datas)
company_outliers(datas)
revenue_outliers(datas)
Descrips(datas)
export_cleaned_job_data(datas)
Line_plot(datas)
Bar_plot(datas)
hist_plot(datas)
Pair_plot(datas)
Heat_plot(datas)
Heat_cov(datas)
Dash_board(datas)
range_stats(datas)
hist_rang(datas)
knn_modeling(datas)
KMeans_clustering(datas)