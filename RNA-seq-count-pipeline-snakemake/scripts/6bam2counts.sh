featureCounts -T $1 -p -t exon -g gene_name -a gencode.v22.annotation.gtf -o $2 $3
# -T 8: number of threads
# -p: paired-end
# -t exon: feature type
# -g gene_id: attribute type
# -a gencode.v22.annotation.gtf: annotation file
# -o result/gene_rawcounts.txt: output file
# $3 result/testtrim.sort.bam input file