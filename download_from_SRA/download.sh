echo SRA_datadown
openssh=/mnt/public/wangxinkang/projects/gse/asperaweb_id_dsa.openssh
cat /mnt/public/wangxinkang/projects/gse/SRR_Acc_List.txt |while read id
do
	num=`echo $id | wc -m `
	if [ $num -eq 12 ]
	then	
		date
		echo "SRR + 8"
		x=$(echo $id | cut -b 1-6)
		y=$(echo $id | cut -b 10-11)
		echo "Downloading $id "
		(ascp -QT -l 300m -P 33001 -k 1 -i $openssh era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/$x/0$y/$id/   ./)
	elif  [ $num -eq 11 ]
	then	
		date
		echo  "SRR + 7"
		x=$(echo $id | cut -b 1-6)
		y=$(echo $id | cut -b 10-10)
		echo "Downloading $id "
		( ascp  -QT -l 500m -P33001  -k 1 -i $openssh  era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/$x/00$y/$id/   ./)
	elif [ $num -eq 10 ]
	then
		date
		echo  "SRR + 6"
		x=$(echo $id |cut -b 1-6)
		echo "Downloading $id "
		( ascp  -QT -l 500m -P33001 -k 1 -i  $openssh era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/$x/$id/   ./ )
	fi
done
