np=4	# Number of processors

# Prepare the case
./scripts/prepare.sh

#
mpirun -np $np reactingFoam -parallel	2>&1	| tee log/sprayFoam.log

# Send notification
./scripts/notify.sh
