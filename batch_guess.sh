#!/bin/bash
cpwd=$(pwd)
echo $cpwd
cd $1
echo $3
for file in *.jpg; 
	do 
		python $3label_image.py $file $2 2> lasterrout.txt > lastresout.txt;
		var=$(head -n 1 lastresout.txt)
		if [[ $var == *"elec (score = 0.9"* ]] 
		then		
			echo $(pwd)"/"$file" : "$var
			cp -b $(pwd)"/"$file $(pwd)"/selected/"
		else
			echo "." #$(pwd)"/"$file" : BAD"
			g="l"
		fi
			
done
cd $cpwd

# use bash batch_guess.sh guess_img/DCIM/  /tf_files/Electricity_Bill_Classifier /tf_files/

#python $2/label_image.py $file $2 | tail -n 2
#sh batch_guess.sh guess_img/DCIM/  /tf_files/Electricity_Bill_Classifier /tf_files/
