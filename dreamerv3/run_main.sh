# Run the main.py 3 times 

for i in 1 2 3
do 
    python tum-adlr-13/dreamerv3/dreamerv3/main.py --logdir ~/logdir_debug/{timestamp} --configs dmc_proprio debug --run.steps 2000
done