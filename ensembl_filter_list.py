import pandas as pd
import pybiomart
from pybiomart import Dataset
import os

# Get the current working directory for file creation
current_directory = os.getcwd()

# Define the file name
file_name = 'Filtros.csv'

# Create the full file path
file_path = os.path.join(current_directory, file_name)

# Connect to Ensembl server
server = Server(host='http://www.ensembl.org')

# Access the specific dataset
mart = server['ENSEMBL_MART_ENSEMBL']
dataset = mart['hsapiens_gene_ensembl']

# Retrieve all attributes (filters) in the dataset
attributes = dataset.list_attributes()

# Create a pandas DataFrame to efficiently store and manipulate filter data
df = pd.DataFrame(attributes)

# Optionally filter the DataFrame if needed (e.g., to include only specific columns)
# filtered_df = df[<your_filtering_criteria>]

# Save the DataFrame to a CSV file in your working directory
df.to_csv(file_path, index=False)  # Avoid including an index column

print(f"Successfully created '{file_name}' in your working directory.")