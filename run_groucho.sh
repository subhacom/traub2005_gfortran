#!/bin/bash
# run this file on the master by typing ./run_groucho.sh {grouchoexe} &

# the groucho program will then start up on 14 nodes on colossus with
# two of the rank on master (see colossusnodes). Replace {grouchoexe}
# with the specific executable you want to run
# (e.g. groucho_fig7A). The colossusnodes file has only localhost by
# default - thus it will emulate 14 nodes on a single node. If you
# have more nodes at your disposal, list them in the colossusnodes file.

GROUCHO_TIME_FILE=master_output.txt
echo Starting groucho `date`,  will write time data to $GROUCHO_TIME_FILE
echo groucho start: `date` >  $GROUCHO_TIME_FILE
nice mpirun -machinefile colossusnodes -np 14 ./$1 >&  tempfile.x
cat  tempfile.x >> $GROUCHO_TIME_FILE
echo groucho end: `date` >>  $GROUCHO_TIME_FILE
echo Finished groucho `date`
