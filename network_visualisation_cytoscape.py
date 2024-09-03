# 0. Libraries we need
import pandas as pd
import py4cytoscape as p4c

data = pd.read_csv("variants_to_genes_name.csv")

data = data.rename(columns={'snp': 'source', 'gene': 'target'})

network = p4c.create_network_from_data_frames(edges=data)

# Crear grupos de genes y SNPs
genes = data['target'].unique().tolist()
snps = data['source'].unique().tolist()

# Crear grupos de genes y SNPs
p4c.create_group(group_name="Gene Group", nodes=genes)
p4c.create_group(group_name="SNP Group", nodes=snps)

# Aplicar estilo visual
p4c.set_node_shape_default('ellipse')  # Forma de los nodos
p4c.set_node_color_default('#D3D3D3')  # Color de los nodos por defecto
p4c.set_node_border_width_default(2.0)

# Visualizar la red
p4c.notebook_export_show_image()