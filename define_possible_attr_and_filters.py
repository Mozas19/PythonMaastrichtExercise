import pandas as pd
import pybiomart
from pybiomart import Dataset
from pybiomart import Server

server = Server(host='http://www.ensembl.org')
server.list_marts()

mart = server['ENSEMBL_MART_SNP']
mart.list_datasets()

dataset = mart['hsapiens_snp']

def show_all_attributes_and_filters(dataset):

    print("Atributos posibles:")
    for attr in dataset.attributes:
        print(f"  - {attr}")

    print("\nFiltros posibles:")
    for filt in dataset.filters:
        print(f"  - {filt}")

show_all_attributes_and_filters(dataset)