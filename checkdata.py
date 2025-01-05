# import os
# import pandas as pd

# def validate_file(file_path):
#     try:
#         data = pd.read_csv(file_path, sep=' ', header=None)
#         print(f"{file_path} loaded successfully")
#     except Exception as e:
#         print(f"Error loading {file_path}: {e}")

# data_root = '/home/msi/code/Largescale_PointCloud_Semantic/superpoint_graph/data/Stanford3dDataset_v1.2_Aligned_Version'
# for root, dirs, files in os.walk(data_root):
#     for file in files:
#         if file.endswith('.txt'):
#             validate_file(os.path.join(root, file))






# import h5py
# import os

# def inspect_h5_file(file_path):
#     """Inspect the structure and content of an HDF5 file."""
#     try:
#         with h5py.File(file_path, 'r') as f:
#             print(f"Inspecting file: {file_path}")
#             print("Root keys:")
#             for key in f.keys():
#                 if isinstance(f[key], h5py.Group):
#                     print(f"Group: {key}")
#                     for subkey in f[key].keys():
#                         subdataset = f[key][subkey]
#                         if isinstance(subdataset, h5py.Dataset):
#                             print(f"    Dataset: {subkey}, Shape: {subdataset.shape}, Dtype: {subdataset.dtype}")
#                 elif isinstance(f[key], h5py.Dataset):
#                     dataset = f[key]
#                     print(f"Dataset: {key}, Shape: {dataset.shape}, Dtype: {dataset.dtype}")

#             # Example: Inspect specific datasets if present
#             if 'sp_labels' in f:
#                 print("\nSample values from 'sp_labels':")
#                 print(f['sp_labels'][:10])  # Print the first 10 values
            
#             if 'target' in f:
#                 print("\nSample values from 'target':")
#                 print(f['target'][:10])  # Print the first 10 values
            
#             if 'in_component' in f:
#                 print("\nSample values from 'in_component':")
#                 print(f['in_component'][:10])  # Print the first 10 values

#     except Exception as e:
#         print(f"Error inspecting file {file_path}: {e}")

# if __name__ == "__main__":
#     # Path to the folder containing .h5 files
#     h5_folder = "data/Stanford3dDataset_v1.2_Aligned_Version/superpoint_graphs"  # Adjust this to the path where your .h5 files are located

#     # Loop through all .h5 files in the folder
#     for root, dirs, files in os.walk(h5_folder):
#         for file in files:
#             if file.endswith(".h5"):
#                 file_path = os.path.join(root, file)
#                 inspect_h5_file(file_path)





# import os
# import shutil

# def rename_annotations(input_dir, output_dir):
#     # 遍历输入目录
#     for root, dirs, files in os.walk(input_dir):
#         # 确保输出目录结构一致
#         relative_path = os.path.relpath(root, input_dir)
#         target_dir = os.path.join(output_dir, relative_path)
#         os.makedirs(target_dir, exist_ok=True)

#         # 如果是Annotations文件夹
#         if "Annotations" in root:
#             # 找到父目录的树编号
#             parent_dir = os.path.basename(os.path.dirname(root))

#             if parent_dir.startswith("tree") and parent_dir[4:].isdigit():
#                 tree_id = parent_dir[4:]

#                 # 遍历文件并重命名
#                 for file in files:
#                     src_file = os.path.join(root, file)

#                     if file == "prunned_tree.txt":
#                         dst_file = os.path.join(target_dir, f"floor_{tree_id}.txt")
#                     elif file == "remained_tree.txt":
#                         dst_file = os.path.join(target_dir, f"ceiling_{tree_id}.txt")
#                     else:
#                         dst_file = os.path.join(target_dir, file)

#                     # 复制并重命名文件
#                     shutil.copy2(src_file, dst_file)
#         else:
#             # 复制非Annotations文件夹中的文件
#             for file in files:
#                 src_file = os.path.join(root, file)
#                 dst_file = os.path.join(target_dir, file)
#                 shutil.copy2(src_file, dst_file)

# if __name__ == "__main__":
#     input_dir = "/home/msi/data/S3DIS_format"  # 原始数据目录
#     output_dir = "/home/msi/data/S3DIS_format_renamed"  # 输出数据目录

#     rename_annotations(input_dir, output_dir)
#     print("Annotations 文件重命名完成！")


import h5py

res_file = "results/s3dis/best/cv1/predictions_test.h5"
with h5py.File(res_file, 'r') as f:
    group = f['Area_1']
    print("Keys in Area_1:", list(group.keys()))

