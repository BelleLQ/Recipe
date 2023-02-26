# Recipe App - Delicious

### Demo of this app


### Setup on AWS EC2 Ubuntu
1. Update apt-get
```
sudo apt-get update
```
2. To clone this repository, run the following command on the terminal
```
git clone https://github.com/BelleLQ/Recipe.git
```

3. You will need django to be installed to run this app. 

Go to the cloned project's directory and install pip
```
cd Recipe
```
```
sudo apt install python3-pip -y
```
Download django using pip
```
pip install django
```

4. Once you have django downloaded, run the following command
Install virtual environment
```commandline
apt install python3.10-venv
```
Create a virtual environment
```
python3 -m venv env
```
Activate the virtual environment
```
source env/bin/activate
```
Install the packages listed in the app's requirements.txt file:
```
sudo pip install -r requirements.txt
```
```
python3 manage.py makemigrations
```
This will create all the migrations file (database migrations) required to run this App.

5. To apply this migrations run the following command
```
python3 manage.py migrate
```
6. Last step, we need to create an admin user. On the terminal, run the following command and provide username, password and email as instructed.
```
python3 manage.py createsuperuser
```

7. Now let's start the server and make the App live by running the following command
```
python3 manage.py runserver
```
Once the server is running, head over to http://127.0.0.1:8000 for the App.
