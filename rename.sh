rename 's/_(1|2)\.fastq\.gz$/_R$1.fastq.gz/' *.fastq.gz
rename 's/ERR(\d+)_R1/ERR$1_S1_L001_R1_001/' *.fastq.gz
rename 's/ERR(\d+)_R2/ERR$1_S1_L001_R2_001/' *.fastq.gz
## 生成sample_name.txt
ls *.fastq.gz | sed 's/_.*//' | sort | uniq > Sample_name.txt