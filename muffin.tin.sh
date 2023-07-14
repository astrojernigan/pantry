#!/bin/bash

########################################
### ---GET READY TO RUN THE MODEL--- ###
########################################

# Switch over to the main run directory
cd ~/cgenie.muffin/genie-main


# Load the essential modules
module load gcc netcdf-fortran rcac

########################################
### ---PROVIDE EXPERIMENT DETAILS--- ###
########################################

# arguments are passed from batch.muffin.sh file
./genie_example.job -f configs/${1}.xml
