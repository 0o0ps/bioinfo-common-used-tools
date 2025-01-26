#!/bin/bash
cellranger count --id=$1 \
           --transcriptome=/mnt/public/wangxinkang/refdata-gex-GRCh38-2024-A \
           --sample=$1 \
           --fastqs=/mnt/public/wangxinkang/projects/gse/cellranger_2nd/raw/$1 \
           --create-bam=true \
           --localcores=8 \
           --localmem=64 \
           --chemistry=ARC-v1

           ## fastqs 大目录
            ##    chemistry 请根据实际情况修改
            ## transcriptome 基因组