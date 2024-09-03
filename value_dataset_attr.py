import pandas as pd
import pybiomart
from pybiomart import Dataset
import py4cytoscape as cyto
import itertools
import re

# Conectar al servidor de Ensembl
dataset = Dataset(name="hsapiens_gene_ensembl", host="http://www.ensembl.org")

filter_name = 'reactome'

# Realizar la consulta sin límite
result = dataset.query(attributes=[filter_name])

# Imprimir los primeros 1 valores en la consola
first_5_rows = result.head(1)
print(first_5_rows)