# built by aditywardhanm
# This block of code is used to download the the dataset from the kaggle page and unzip it and save it 
# in the directory defined by the address (currently in the same directory as the rest of the files)

# You need a Kaggle API Key to run this code.

# This code updates the dataset every week since the timestamp has started and the timestamp gets edited 
# everytime the code is run. 

import subprocess
import os
import time

dataset_name = 'Cornell-University/arxiv'           # The dataset_name contains the download path in "username/dataset format";
dataset = 'arxiv'                                   # The dataset contains the name of the .zip being downloaded;
timestamp_file = 'last_execution_timestamp.txt'     # The timestamp_file contains the timstamp of when the the file was downloaded;

def week_check(last_timestamp):
    current_timestamp = time.time()
    # Calculate the time difference in seconds
    time_difference = current_timestamp - last_timestamp
    # Check if a week (604800 seconds) has passed
    return time_difference >= 604800

def save_timestamp():
    current_timestamp = time.time()
    with open(timestamp_file, 'w') as file:
        file.write(str(current_timestamp))

def run_download():
    # Command to download the dataset using Kaggle API to the current directory
    download_command = f'kaggle datasets download -d {dataset_name}'
    
    # Run the download command
    subprocess.run(download_command, shell=True)

    # Unzip the downloaded dataset
    # Note: You may need to adjust this depending on the compression format used by Kaggle
    unzip_command = f'unzip -o {dataset}.zip -d {os.getcwd()}'
    
    # Run the unzip command
    subprocess.run(unzip_command, shell=True)


def data_setup(timestamp_file):
    # Check if a week has passed since the last execution
    if not os.path.exists(timestamp_file) or week_check(float(open(timestamp_file).read().strip())):
        try:
            run_download()
            save_timestamp()
            print("Download and extraction completed successfully.")
        except Exception as e:
            print(f"Error during download or extraction: {e}")
        
    else:
        print("Download skipped. A week has not passed since the last execution.")
