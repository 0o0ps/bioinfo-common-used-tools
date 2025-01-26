rename 's/_(1|2)\.fastq\.gz$/_R$1.fastq.gz/' *.fastq.gz # 变成R1,R2
# find raw/ -type f -name "*.fastq.gz" -exec rename 's/_(1|2)\.fastq\.gz$/_R$1.fastq.gz/' {} \;
rename 's/ERR(\d+)_R1/ERR$1_S1_L001_R1_001/' *.fastq.gz
# find . -type f -name "*.fastq.gz" -exec rename 's/SRR(\d+)_R1/SRR$1_S1_L001_R1_001/' {} \;
rename 's/ERR(\d+)_R2/ERR$1_S1_L001_R2_001/' *.fastq.gz
# find . -type f -name "*.fastq.gz" -exec rename 's/SRR(\d+)_R2/SRR$1_S1_L001_R2_001/' {} \;

## 生成sample_name.txt
ls *.fastq.gz | sed 's/_.*//' | sort | uniq > Sample_name.txt