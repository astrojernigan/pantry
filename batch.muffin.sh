#!/bin/bash

## To submit jobs using this file: bash muffin.tin.sh [-t int:int:int] [-o] config_1 [config_2 ...]
## 			       or: bash muffin.tin.sh [-t int:int:int] [-o] config_{1,2,...}
## where:
##        -t  sets job time limit, with the format hr:min:sec
##        (default: 336:00:00, maximum: 336:00:00)
##	  -o  overwrites previous output if present

username='jjernig'
account='olson172'
output_directory="/scratch/bell/${username}"
config_directory="${HOME}/cgenie.muffin/genie-main/configs"

job_time='336:00:00'

usage="Usage: ./$(basename "$0") [-h] [-t int:int:int] [-y] config_file ... --submits a job to the queue for each config file specified

where:
	-t  set the job time limit, with format hr:min:sec 
	    (default: ${job_time}, maximum: 336:00:00)
	-o  overwrites previous output if present
	-h  displays this text

to submit multiple jobs, pass each config file name as a separate parameter, separated by a space, or use brace expansion: config_{a,b}_{0,1} is read as config_a_0 config_a_1 config_b_0 config_b_1

dependencies: batch.muffin.sh"

overwrite_input=""
overwrite_all=""

while getopts "t:oh" option
do	case "$option" in
		t)
			job_time="$OPTARG"
			;;
		o)
			overwrite_input="yes"
			overwrite_all="yes"
			;;
		h)
			echo 1>&2 "$usage"
			exit 1
			;;
		*)
			echo 1>&2 "$usage"
			exit 1
			;;
	esac
done
shift $(($OPTIND-1))

job_array=( "$@" )
for job in "${job_array[@]}"
do	
	if [[ -f "${config_directory}/${job}.xml" ]]
	then
		sed -i "/^		<var name=\"EXPID\">.*/ s/>.*<\/var>/>${job}<\/var>/" "${config_directory}/${job}.xml"
	else
		echo "Config file ${job}.xml does not exist"
		exit 1
	fi
	## Submits one job for each combination of parameters supplied ##

	if [[ -d "${output_directory}/$job" ]] # checks if output for this job exists
	then				       # if so, asks for permission to overwite
		until [[ $overwrite_input == "yes" || $overwrite_input == "no" ]]; do
			read -p "Output for $job already exists. Overwrite? yes or no : " overwrite_input
		done
		if [[ $overwrite_input == "yes" ]]
		then
			if [[ "${#job_array[@]}" -gt 1 ]]
			then	
				until [[ $overwrite_all == "yes" || $overwrite_all == "no" ]]; do
					read -p "Overwrite all? yes or no : " overwrite_all
				done
				[[ $overwrite_all == "no" ]] && overwrite_input=""
			fi
			rm -r "${output_directory}/$job" 
			[[ -f "${job}.out" ]] && rm ${job}.out
			[[ -f "${job}.out" ]] && rm ${job}.err
		else
			exit 2
		fi
	fi

	sbatch --nodes=1 --tasks=1 --time=${job_time} --mail-type=END,FAIL --mail-user=${username}@purdue.edu --account=${account} --job-name=${job} --output=${job}.out --error=${job}.err batch.muffin.sh ${job} # calls batch.muffin.sh to submit the individual job
done
