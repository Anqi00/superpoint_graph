import os
import pandas as pd

def validate_file(file_path):
    try:
        data = pd.read_csv(file_path, sep=' ', header=None)
        print(f"{file_path} loaded successfully")
    except Exception as e:
        print(f"Error loading {file_path}: {e}")

data_root = '/home/msi/code/Largescale_PointCloud_Semantic/superpoint_graph/data/Stanford3dDataset_v1.2_Aligned_Version'
for root, dirs, files in os.walk(data_root):
    for file in files:
        if file.endswith('.txt'):
            validate_file(os.path.join(root, file))
