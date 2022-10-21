![BollyDumb Banner](docs/images/BollyDumb_banner.png)
# BollyDumb
A **Bollywood Movie Name Generator**, for assistance in playing the **Dumb Charades** with Bollywood Movies.
#### Demo: https://bollydumb.herokuapp.com/
## Local Installation 
Pre-requisites for local installtion using python virtual environment (venv): Python3, Git, Terminal application (gitbash, bash, powershell, etc.).

The following steps are written keeping in mind a linux os, exact commands and process might change on Windows and MacOS. Please modify the commands and steps as per your OS.

- Open a Termainal and Clone the repository to desired location using `git clone https://github.com/ravigupta-art/BollyDumb.git`.
- CD into cloned repository using `cd BollyDumb`.
- Create a virtual environment named 'python3env' using `python3 -m venv python3env`.
- Activate virtual environment using `source python3env/bin/activate`.
- Install the required python packages using `pip install -r requirements.txt`.
- Change the value of  'app.secret_key' in the file 'app.py' to a private and secure.  You may use [this](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/?highlight=secret%20key#configure-the-secret-key) method from flask documentation to generate the key.
- Start the application using `python app.py`
- Open a browser and goto `http://localhost:5000/` to start playing.

## Deploying to Heroku/PythonAnywhere/webserver
- Please look in to flask documentation [here](https://flask.palletsprojects.com/en/2.2.x/deploying/) to see the platform specific steps.

Note: The application is still a work in progress and we will be adding new features in future releases.

## Third party

- Flask 1.1.2 ([BSD-3-Clause License](https://github.com/pallets/flask/blob/master/LICENSE.rst))
- Bootstrap 4.5.3 ([MIT License](https://github.com/twbs/bootstrap/blob/main/LICENSE))
- Bootstrap Icons 1.2.2 ([ MIT License](https://github.com/twbs/icons/blob/main/LICENSE.md))
- JQuery 3.5.1 ([MIT License](https://jquery.org/license/))
