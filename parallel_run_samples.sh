#!/bin/bash
# Specify the number of concurrent runs
concurrent_runs=5
# Read the sample names from sample_name.txt
mapfile -t sample_names < Sample_name.txt
# Function to run cellranger for a single sample
run_cellranger() {
    sample=$1
    ./Run_cellranger.sh $sample
}
export -f run_cellranger  # Export the function to make it available to GNU Parallel
# Run cellranger for each sample in parallel
parallel -j $concurrent_runs run_cellranger ::: "${sample_names[@]}" 