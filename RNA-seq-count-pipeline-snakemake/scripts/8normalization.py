
from matplotlib import axis
import pandas as pd
import os

print("11111",os.getcwd())

### input & output files 
input_count_file = 'data/processed/counts/Fujian/all_samples_gene_rawcounts.csv'
input_length_file = 'data/processed/counts/gene_length.csv'
output_FPKM_file = "data/processed/counts_integrated/Fujian/all_samples_gene_FPKM.csv"
output_TPM_file = "data/processed/counts_integrated/Fujian/all_samples_gene_TPM.csv"


### 两种Normalization方法
def FPKM_normalization(df,length):
    '''
    FPKM normalization
    df (dataframe): dataframe ,expression counts matrix
    length (dataframe): gene length, the index should be the same as the df
    '''
    # Step 1: 计算每个样本的总reads数
    total_reads = df.sum(axis=0)  # 每个样本的总reads数 axis = 0 along with the row(i.e. sum of each column)
    total_reads_million = total_reads / 1e6  # 缩放到百万单位
    # Step 2: 将基因长度转换为千碱基（kb）
    length['Length'] = length['Length'] / 1000
    df = df.div(total_reads_million,axis=1) #axis=1表示按列除 按样本除 归一化到每百万reads
    if (length.index == df.index).all(): #检查两个dataframe的index是否一致
        df = df.div(length['Length'],axis=0) #axis=0表示按行除 按基因长度除
    else:
        print("The index of df and length are not the same!")
    return df

def TPM_normalization(df,length):
    '''
    TPM normalization 先gene length 再total reads
    df (dataframe): dataframe ,expression counts matrix
    length (dataframe): gene length, the index should be the same as the df
    '''
    # Step 1: 将基因长度转换为千碱基（kb）
    length['Length'] = length['Length'] / 1000 #将基因长度转换为千碱基（kb）
    if (length.index == df.index).all(): #检查两个dataframe的index是否一致
        df = df.div(length['Length'],axis=0) #axis=0表示按行除 按基因长度除
    else:
        print("The index of df and length are not the same!")
    # Step2: 计算每个样本的总reads数
    total_reads = df.sum(axis=0)  # 每个样本的总reads数
    total_reads_million = total_reads / 1e6  # 缩放到百万单位
    df = df.div(total_reads_million,axis=1) 
    
    return df




if not os.path.exists(os.path.dirname(output_FPKM_file)):
    os.makedirs(os.path.dirname(output_FPKM_file))

df_count = pd.read_csv(input_count_file,index_col=0)
df_length = pd.read_csv(input_length_file,index_col=0)
FPKMout = FPKM_normalization(df_count,df_length)
TPMout = TPM_normalization(df_count,df_length)
FPKMout.to_csv(output_FPKM_file)
print("FPKM normalization finished!")
TPMout.to_csv(output_TPM_file)
print("TPM normalization finished!")

## generate length csv
# _df = pd.read_csv('/cluster2/huanglab/xwang/projects/RNA-seq-count-pipeline-snakemake/data/processed/counts/Daping/GC_NAIC_GC01_pre__gene_rawcounts.txt',sep='\t',comment= '#')
# df_length = _df[['Geneid','Length']]
# df_length.to_csv('data/processed/counts/gene_length.csv',index=False)

## 验证没问题
# fpkm = pd.read_csv(output_FPKM_file,index_col=0)
# tpm = pd.read_csv(output_TPM_file,index_col=0)
# fpkm.head()
# tpm.head()
# fpkm.sum(axis=0)
# tpm.sum(axis=0)

