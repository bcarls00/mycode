Welcome to Brian's Switch summarizer and configuration builder. 

For getting a summarized, one page snapshot of your switch you will use the summarize.py script.
This script will take the current configuration file form the switch and output a summary to either a custom 
file or as a dated entry in the default switch_list file.
First you want to copy your file to the project/sources directory.
Then run the summarize.py script. Answer a few questions and you'll be on your way!


For creating a new configuration file for a switch you will use the create_config.py script.
This script will take a standardized, easy to read file and output a file that when ran in the switch will 
fully configure it to the specified parameters.
First you need to copy the master.conf to the sources directory and edit it to your desired parameters.
Then you will run the create_config.py script which will output the config file to the finished directory.
