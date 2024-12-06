## env = scanpy
## daping group 下的所有样本整合成一个count matrix
import pandas as pd
import glob 
import os
# test = pd.read_csv("/cluster2/huanglab/xwang/projects/RNA-seq-count-pipeline-snakemake/data/processed/counts/Daping/GC_NAIC_GC01_pre__gene_rawcounts.txt",\
#         sep="\t", index_col=0, comment='#')
# test["Length"]

# rawfile_root = "data/processed/counts/Daping/*gene_rawcounts.txt"
# result_file = "data/processed/counts/Daping/all_samples_gene_rawcounts.csv"
rawfile_root = "data/processed/counts/Fujian/*gene_rawcounts.txt"
result_file = "data/processed/counts/Fujian/all_samples_gene_rawcounts.csv"

all_counts = []
rawcount_files = glob.glob(rawfile_root) #获取所有样本的rawcount文件
for files in rawcount_files:
    count_matrix = pd.read_csv(files, sep="\t", comment='#')
    count_col = count_matrix.columns[-1] #最后一列是count值
    df = count_matrix[['Geneid', count_col]] #只保留geneid和count值
    df.columns = ['Geneid', os.path.basename(files).replace('__gene_rawcounts.txt', '')] #!将count值的列名改为文件名
    df.set_index('Geneid', inplace=True) #将Geneid设置为索引
    all_counts.append(df)
all_counts = pd.concat(all_counts, axis=1,join = 'outer') #将所有样本的count值合并,axis=1表示横向合并,join = 'outer'表示取并集
all_counts.to_csv(result_file) #保存合并后的count值文件
na_values = all_counts.isna().sum().sum() #检查是否有缺失值
print(f"Completed! Number of missing values: {na_values}")