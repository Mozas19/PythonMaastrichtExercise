# 0. Libraries we need
import pandas as pd
import pybiomart
from pybiomart import Dataset
from pybiomart import Server

# 1. Specifies the full path to the file
file_path = "variant_list.txt"

# 2. Load the variant data, considering each row as a value.
with open(file_path, "r") as f:
    variants = [line.strip() for line in f]

# 3. Creates my DataFrames
variants_df = pd.DataFrame({'snp_id': variants, 'gene': ''})

# 4. Create Server and Marts to extract data from a exact dataset not known
server = Server(host='http://www.ensembl.org')
server.list_marts()

mart = server['ENSEMBL_MART_SNP']
mart.list_datasets()

dataset = mart['hsapiens_snp']

# 5. Define a function to retrieve gene information for each variant
def get_gene_info(variants_df):
    variant_ids = variants_df['snp_id'].tolist()
    results = []
    try:
        for variant in variant_ids:
            # Retrieve multiple attributes (modify for your needs)
            result = dataset.query(
                attributes=['refsnp_id', 'ensembl_gene_name'],
                filters={'snp_filter': variant}
                )

            #print(result)

            if result.empty:
                # Handle empty results (e.g., assign 'Not Found' values)
                results.append({
                    'snp': variant,
                    'gene': 'Not Found'
                    })
            else:
                results.append({
                    'snp': variant,
                    'gene': result['Gene Name'].tolist()[0]
                    })

    except Exception as e:
            print(f"Error processing variant {variant}: {e}")
            results.append({
                'snp': variant,
                'gene': 'Error'
            })
        
    return pd.DataFrame(results)

# 6. Get gene information for the variants
results_df = get_gene_info(variants_df)

# 7. Print the resulting DataFrame
print(results_df)

# 8. Save the results to a TXT file
output_txt_file = "variants_to_genes_name.txt"
results_df.to_csv(output_txt_file, index=True, header=True, sep='\t')
print(f"Results saved to {output_txt_file}")