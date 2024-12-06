samtools view -b -S $1 -o $2
# view - SAM/BAM/CRAM conversion view命令的主要功能是：将sam文件转换成bam文件
# -b output in BAM format
# -S input in SAM format
# -o output file