# 导入os模块，用于操作文件和文件夹
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1,2" 

import subprocess

# 定义moe_loras和moe_test的路径
moe_loras_path = "/home/qianzy/LLaMA-LoRA-Tuner/moe_loras/"
moe_test_path = "/home/qianzy/LLaMA-LoRA-Tuner/moe_test/"
moe_output_path = "/home/qianzy/LLaMA-LoRA-Tuner/moe_perturb/"

# 获取moe_loras和moe_test下的所有文件夹和文件名
moe_loras_folders = os.listdir(moe_loras_path)
moe_test_files = os.listdir(moe_test_path)

# 循环遍历moe_loras_folders和moe_test_files，生成四个参数
for lora_weights in moe_loras_folders:
    # if lora_weights == "enzymes":
    for test_file in moe_test_files:
        # if (test_file == "tox21-1.json"):
        output_file = moe_output_path + lora_weights + "&" + test_file.replace(".json", "").split("-")[0] + ".txt"
            # os.system(f"python test-moe.py {moe_loras_path + lora_weights} {moe_test_path + test_file} {output_file}")
        subprocess.call(("python","test-moe_perturb.py",moe_loras_path + lora_weights, moe_test_path + test_file, output_file))
