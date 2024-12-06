import scanpy as sc
import os 
# dic = {1: "a", 2: "b", 3: "c"}
# print(**dic)
### test concatenate

# test1 = sc.read_10x_mtx("/mnt/public/wangxinkang/projects/temptest/testsamples/ERR13381157/outs/filtered_feature_bc_matrix")
# test1.obs["sample"] = "ERR13381157"
# test2 = sc.read_10x_mtx("/mnt/public/wangxinkang/projects/temptest/testsamples/ERR13381158/outs/filtered_feature_bc_matrix")
# test2.obs["sample"] = "ERR13381158"
# ## 合并测试成功
# test_combine = test1.concatenate(test2)
# test_combine
# test_combine.obs

samples = os.listdir("/mnt/public/wangxinkang/projects/temptest/testsamples")
samples
adata_list = []
for sample in samples:
    adata = sc.read_10x_mtx(f"/mnt/public/wangxinkang/projects/temptest/testsamples/{sample}/outs/filtered_feature_bc_matrix")
    adata.obs["sample"] = sample
    adata_list.append(adata)

adata_list

adata_combined = adata_list[0].concatenate(*adata_list[1:])



adata_combined.obs["sample"].value_counts()

