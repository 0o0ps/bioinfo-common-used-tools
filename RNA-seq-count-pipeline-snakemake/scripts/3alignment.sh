hisat2 -p $1 -1 $2 -2 $3 -x hg38/hg38 -S $4
# -p 8: use 8 threads
# -1: R1.fastq
# -2: R2.fastq
# -x: genome index file prefix , hg38 = human
# -S: output file
