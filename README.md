<img src="https://www.unisg.ch/-/media/93125423859d46928371a633b15cfcb1.jpg" alt="SIAW logo" width="200" align="right">


# Overview
|#|Content|
|----|----|
|1|Basics of Python|
|2|Working with APIs|
|3|Create your own image classifier|
|4|Creating websites and APIs with Flask|
|5|Introduction GCP|
|6|Links and resources discussed in class|

# 0. Before we start

We will use features of GCP in today's class. You can either sign up for your own account (you get $300 in free credit but need to register a credit card) or I can add you to a temporary project.

If you want me to add you to today's project so you can interact with the environment later on, please add your email address to this google sheet. Your email address must be associated with an active Google Account, Google Workspace account or Cloud Identity account.

https://docs.google.com/spreadsheets/d/1ZRTXJImjzOs4AxeBqa20CK508w6dbcpVNEAv7cGvYwU/edit?usp=sharing

# 1. Python

## 1.1 Python quickstart

If you are already familiar with programming with R, then learning a new programming language will be surprisingly easy. All it takes is getting used to some alternative semantic and naming conventions. We cover the basics in one large script before we move on to leveraging the work of other users via packages.

See scripts:
* `01a_Introduction to Python`
* `01b_Python Packages`

## 1.2 Data science in Python with numpy, pandas and scikit learn

Machine learning in Python is very similar to R. While some of you might find some conventions faster in R, Python offers some other advantages for packaging code into classes that allow easier and cleaner re-usage.

See scripts:
* `01c_Numpy and Pandas - Essential data science packages`
* `01d_ML with Python`

# 2. Working with APIs

One of the coolest part about programming is when you can connect your application to the internet: Fetch data from online sources and interact with other platforms. The glue keeping all applications together are Application Programming Interfaces (APIs) that ensure an in-between layer with basic rules on how one app can interact with another.

See script: `2a_APIs.ipynb`

### Links

Open Weather: https://openweathermap.org/api

Nasa API: https://api.nasa.gov/


# 3. Create your own image classifier

Chrome plugin to download images in bulk from google:
https://chrome.google.com/webstore/detail/download-all-images/ifipmflagepipjokmbdecpmjbibjnakm

You can alternatively also download the banana images here:
https://drive.google.com/drive/folders/1a98FEbmLfiCb85jnxFm35dRDcvG8EaME?usp=sharing

The script `03a_call_image_classifier.py` shows how to call the API

# 4. Websites and APIs with Flask

See scripts and folders:

* `04a_flask_basic.py`
* `04b_flask_bootstrap`
* `04c_flask_with_forms`

# 5. Introduction to GCP

## Start your own server

1. Go to the hamburger menu (top left corner)
1. Select: "Compute Engine" > "VM Instances" (you might have to enable an API)
1. Select "Create instance" and give it a new name.
  1. Choose any region in europe-west
  1. Choose "e2-micro" as machine type
  1. Change the boot disk from Debian to Ubuntu 21.10
  1. Tick the boxes "Allow HTTP traffic" and "Allow HTTPS traffic"
  1. Create the server

See below how to install python and other packages on the server.

## SSH into your server from your terminal

1. First we generate a SSH key (secure shell key). This is a two-sided password that ensures a safe connection while interacting with our server over the public internet. Go to your terminal and run `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`. When prompted for a passphrase just hit enter
2. This should have created a private and a public key. The public key (ending with .pub) is deposited on the server, the private key stays on our computer and is what we use to access the server.
3. Navigate into the directory where you SSH keys were saved. You can use `ls` to show all files and directories in the current directory and `cd your_directory_name` to step into that directory.
1. We want to copy the public key to our server.  Use `cat filename` to print the public key and copy it to your clipboard. Make sure that you don't capture any additional whitespaces in the beginning or end.
1. Navigate to you server in GCP and click on it to open its settings. Click "Edit" at the top.
1. Scroll down to "SSH Keys" (you can also search with CMD + F or CTRL + F) and add the public SSH key that you have copied to your clipboard.
1. Save the new settings. It might take a minute or so for the settings to be written to the server.
1. Take note of the user name that is associated with the SSH key. You will need it to enter the server in the next step.
1. Back in the compute engine overview copy the <b>external</b> ip address of your server. In your terminal on your own computer you can now enter your server by running `ssh -i path_to_your_private_ssh_key your_user_name@your_servers_external_ip`. Your computer will not recognise the server and ask you whether you want to continue. Say yes.
1. You should now be logged into your server. There won't be much there yet, but we will change that next.

## Send files to your server

1. Enter the directory with the folder (or file) you want to send to the server
1. Run the command `scp -ri path_to_your_private_ssh_key your_folder_name your_user_name@your_servers_external_ip:`. The `-r` stands for recursive and is required for folders. If you are just sending a file you can omit. The ":" at the end indicates where on the server we want to save the data. In our case the home directory is fine.
1. Your files should now be transmitted to the server. You can ssh into the server now to start your Flask app

## Running the flask app

To run the app we first set up python and pip

```
sudo apt-get update   # downloads the updates
sudo apt update   # installs the updates


# Installing python and pip
sudo apt install python3-pip   # download and install pip
pip3 --version    # check that everything works
sudo pip3 install flask # install packages, in this case flask

# You may want to install some other packages. In this case for the Vision app:
sudo pip3 install wtforms flask_wtf google-cloud-automl
```

### Connect a domain to a server

You can buy domains at for example [namecheap.com](http://namecheap.com), domains.google, or many other sites. You can your own domain for roughly 1-10 CHF a year

Here is a tutorial for connecting a Namecheap domain to a GCP server:
[https://www.youtube.com/watch?v=eXtqqofrhOo](https://www.youtube.com/watch?v=eXtqqofrhOo)

# 6. Links and resources discussed in class

Recommended reinforcement learning course: [https://deepmind.com/learning-resources/-introduction-reinforcement-learning-david-silver](https://deepmind.com/learning-resources/-introduction-reinforcement-learning-david-silver)

ChinAI: Newsletter on AI in ChinaAI -[https://chinai.substack.com/](https://chinai.substack.com/)

Linear Algebra review:

- 3Blue1Brown: [https://www.youtube.com/watch?v=kjBOesZCoqc&list=PL0-GT3co4r2y2YErbmuJw2L5tW4Ew2O5B&ab_channel=3Blue1Brown](https://www.youtube.com/watch?v=kjBOesZCoqc&list=PL0-GT3co4r2y2YErbmuJw2L5tW4Ew2O5B&ab_channel=3Blue1Brown)
- (Schaum) Schaums outline of theory and problems of matrix algebra
- (Deisenroth) Mathematics for Machine learning

Hackerrank: small coding problems to practice -[https://www.hackerrank.com/challenges/grading/problem](https://www.hackerrank.com/challenges/grading/problem)

Recommended youtube tutorials for python in general

- Sentdex: [https://www.youtube.com/playlist?list=PLQVvvaa0QuDeAams7fkdcwOGBpGdHpXln](https://www.youtube.com/playlist?list=PLQVvvaa0QuDeAams7fkdcwOGBpGdHpXln)
- Corey Schafer: [https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)

Recommended youtube tutorials for numpy/pandas :

- Sentdex: [https://www.youtube.com/playlist?list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-](https://www.youtube.com/playlist?list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-)
- Corey Schafer: [https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)

Recommended youtube tutorials for numpy/pandas:

- Sentdex: [https://www.youtube.com/playlist?list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB](https://www.youtube.com/playlist?list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB)
- Corey Schafer: [https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)


# Other

If you questions of any sorts please don't hesitate to contact me via email:
[dominique.c.a.paul@gmail.com](mailto:dominique.c.a.paul@gmail.com)
