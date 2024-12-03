java -jar src/trimmomatic-0.36/trimmomatic-0.36.jar PE $1 $2 -baseout $3 -threads $4 ILLUMINACLIP:src/trimmomatic-0.36/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
# PE: paired end
# -threads 16: number of threads
# ./data/raw/Pre_biospy_GC_RNA/Daping-fastq/GC_NAIC_GC01_pre_R1.fastq.gz: Read 1
# ./data/raw/Pre_biospy_GC_RNA/Daping-fastq/GC_NAIC_GC01_pre_R2.fastq.gz: Read 2
# -baseout ./result/testtrim: output file name
# ILLUMINACLIP:src/Trimmomatic-0.36/adapters/TruSeq3-PE.fa:2:30:10: adapter file
#? LEADING:3: remove leading low quality or N bases
#? TRAILING:3: remove trailing low quality or N bases
