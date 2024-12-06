用snakemake来对bulk RNA-seq 进行定量
genome = hg38
env = snakemake


├── data
│   ├── processed
│   └── raw
├── gencode.v22.annotation.gtf
├── hg38
│   ├── hg38.1.ht2
│   ├── hg38.2.ht2
│   ├── hg38.3.ht2
│   ├── hg38.4.ht2
│   ├── hg38.5.ht2
│   ├── hg38.6.ht2
│   ├── hg38.7.ht2
│   └── hg38.8.ht2
├── log.txt
├── run.sh
├── samples.txt
├── scripts
│   ├── 2filter_adapter.sh
│   ├── 3alignment.sh
│   ├── 4transfer_into_bam_file.sh
│   ├── 5sort_bam.sh
│   ├── 6bam2counts.sh
│   ├── 7integrate_samples.py
│   ├── 8normalization.py
│   ├── build_index.sh
│   └── temp.py
├── Snakefile
└── src
    └── trimmomatic-0.36