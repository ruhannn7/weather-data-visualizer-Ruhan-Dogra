import pandas as pd
import numpy as np


df = pd.read_csv("weather_data.csv", sep=',')

print("---DataFrame Loaded---")

print("\n---DataFrame Head---")
print(df.head())

print("\n---DataFrame Info---")
df.info()

print("\n---DataFrame Describe---")
print(df.describe())

print("\n---Task 2: Data Cleaning and Processing---")
missing_values=df.isnull().sum()
if missing_values.any():
    print("WARNING: Missing values found.")
else:
    print("SUCCESS: No missing values(NaNs found. No action required.")

print("\n---Converting Date Column---")
df['Date_Time'] = pd.to_datetime(df['Date_Time'])
print("Date_Time column converted to DateTime format.")

relevant_cols = ['Date_Time', 'Temperature_C', 'Humidity_pct', 'Precipitation_mm']
df_cleaned = df[relevant_cols].copy()
df_cleaned.set_index('Date_Time', inplace=True)
print("Filtered for relevant columns and set Date_Time as index.")

print("\n---Cleaned DataFrame Head---")
print(df_cleaned.head())

print("\n---Task 3: Statistical Analysis---")
overall_stats = df_cleaned[['Temperature_C','Humidity_pct','Precipitation_mm']].agg(['mean','min','max', 'std'])
print("\nOverall Weather Metrics:")
print(overall_stats.to_string())


print("---Task 5: Grouping and Aggregation---")
agg_funcs = ['mean', 'min', 'max','std']

daily_stats = df_cleaned.resample('D').agg(agg_funcs)
daily_stats.columns = ['_'.join(col).strip() for col in daily_stats.columns.values]
daily_stats.dropna(inplace=True) 
print("\n--- 1. Daily Weather Summary---")
print(daily_stats.head().to_string())


monthly_stats = df_cleaned.resample('ME').agg(agg_funcs)
monthly_stats.columns = ['_'.join(col).strip() for col in monthly_stats.columns.values]
print("\n--- 2. Monthly Weather Summary ---")
print(monthly_stats.to_string())

print("\n---Task 6: EXPORTING DATA---")

df_cleaned.to_csv('cleaned_weather_data.csv')
print("Exported cleaned_weather_data.csv")

daily_stats.to_csv('daily_weather_summary.csv')
print("Exported daily_weather_summary.csv")

monthly_stats.to_csv('monthly_weather_summary.csv')
print("Exported monthly_weather_summary.csv")

print("\nTask 6: Data Export Complete.")