import pandas as pd
import numpy as np

# Read the CSV file
file_path = './Small_Fires.csv'
df = pd.read_csv(file_path)

column_to_modify = 'severity'

df[column_to_modify] = 0

output_file_path = './Small_Fires.csv'
df.to_csv(output_file_path, index=False)

print(f"Modified CSV saved to {output_file_path}")
