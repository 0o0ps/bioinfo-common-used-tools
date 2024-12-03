nohup snakemake -s Snakefile -j 7 --latency-wait 60  --printshellcmds --verbose > log.txt 2>&1 &
#keep-going: continue running even if one rule fails
#rerun-incomplete: rerun the incomplete rules
#--printshellcmds: print the shell commands that will be executed
#--verbose: print the full command line of the executed command
#--latency-wait 60: wait for 60 seconds before executing the command
#--resources mem_mb=8000: set the memory limit to 8000 MB
#--resources disk_mb=1000000: set the disk limit to 1000000 MB
