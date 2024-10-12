import pickle

# 指定要读取的 .pkl 文件路径
file_path = '/home/shaol/gjx/Kalib/dataset/test_sample_droid_data/Kalib/Kalib_outputs/pnp_inference_res.pkl'

# 打开文件并读取数据
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# 输出读取的数据
print(data)