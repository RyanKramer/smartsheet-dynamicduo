## Thank You For Supporting Us!

### It is a thanks to you and many like you that have enabled us to continue to build processes just like this one to make managing your Smartsheet processes even more automated!

## What's included?

## This process includes the following items: 

- config.yml (this is the properties or configuration file where you will set your token and sheets)
- requirements.txt (this used for installing the dependencies in which your interpreter will utilize)
- delete_data.py (this is the script that you will execute to remove the data)

## Tutorial

### 1. Generate API Token - 
    - Login to Smartsheet
    - Click on the user profile at top right
    - Click Apps & Integrations
    - Click API Access
    - Click Generate new access token
    - Name the token (name does not matter)
    - Copy the access token (example: 6afh1x8e73gkxc8x7dqrgwaa59)
    - Put this token in your config.yml for the api_token property


### 2. Add the sheet IDs to your configuration file  - 
    - Login to Smartsheet
    - Go to the respective grid you want to clear
    - Click on File on the top left
    - Click Properties...
    - Copy the Sheet ID (example: 7625735557932911
    - Add this sheet to your configuration file for the sheet_id property
    - Repeate this process for each sheet and seperate the sheet IDs by ,'s


### Setup python environment
    - This process was meant to be written using Python 3 for Mac. Follow directions at this link for setting up Python 3 on your system - https://www.python.org/about/gettingstarted/
    - Install pip which manages your python dependencies - https://pip.pypa.io/en/stable/installing/
    - Optionally use a virtual environment to segment interpreter - https://docs.python.org/3/tutorial/venv.html
    - Install dependencies - run this command from the base of the project - 'pip install -r requirements.txt'
    - Run your process - 'python delete_data.py'


### You should be up and running!
If you run into any issues, please reach out to us and we will do our best to get you up and running as well as improve the documentation for future users!