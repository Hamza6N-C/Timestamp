import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime(Your_start_date)
end_date = datetime(Your_end_date)

# Function to generate random timestamps
def generate_random_timestamps(start_date, end_date, num_timestamps):
    delta = end_date - start_date
    random_seconds = np.random.randint(0, int(delta.total_seconds()), num_timestamps)
    random_dates = [start_date + timedelta(seconds=int(rs)) for rs in random_seconds]
    timestamps_ns = [int(rd.timestamp() * 1e9) for rd in random_dates]  # Convert to nanoseconds
    return timestamps_ns, random_dates

# Generate N random timestamps
num_timestamps = N
timestamps_ns, random_dates = generate_random_timestamps(start_date, end_date, num_timestamps)

# Remove timezone information from datetime objects before creating the DataFrame
naive_datetimes = [rd.replace(tzinfo=None) for rd in random_dates]

# Convert to DataFrame
df = pd.DataFrame({
    'Timestamp (ns)': timestamps_ns,
    'Datetime': naive_datetimes
})

# Define the path to save the Excel file
output_file = r'C:\Your_File_Path\Your_File_Name.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)

# Read back the file for transformation
input_df = pd.read_excel(output_file)

# Transform to UTC-aware datetime
input_df['Transformed_Date'] = pd.to_datetime(input_df['Timestamp (ns)'], unit='ns', utc=True).dt.date
input_df['Transformed_Hour'] = pd.to_datetime(input_df['Timestamp (ns)'], unit='ns', utc=True).dt.strftime('%Y-%m-%d %H:00:00')

# Save the transformed dataframe back to the Excel file
output_transformed_file = r'C:\Your_File_Path\Your_File_Name.xlsx'
input_df.to_excel(output_transformed_file, index=False)

# Display the DataFrame to check differences
print(input_df[['Timestamp (ns)', 'Datetime', 'Transformed_Date', 'Transformed_Hour']])