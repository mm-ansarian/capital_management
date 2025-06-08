## Birth
At first, my purpose of creating this project was making a program to manage the
financial activities;
So I started and when I finished programming, I felt that I can learn a lot of things by developing this program and improve my skills, so I started developing and I put it in GitHub.

## Introduction
In this PC app called "Capital Management", you can register your financial transactions and see some details about your capital. 
This program contains a GUI(Graphical User Interface) designs with Qt5, a database that is mysql and some source codes written with python.

## How to run
#### Easy run
To run the program easily(for the users or someone who wants to test the app), I put a .exe file in the project's folder, but it seems that there is a problem related to database module; so the .exe file doesn't work yet and you can't open the app with the .exe file(An error happen when opening the .exe file).

#### For developers
If you want to develop it or see its source codes(or the only way to run this program till now 😐), follow the steps below:

1. Install `python3` and `mysql` on your system.
2. Clone the project repository:
```bash
git clone https://github.com/mm-ansarian/Capital_Management.git
``` 
or 
```bash
git clone git@github.com:mm-ansarian/Capital_Management.git
```
3. Open the project folder.
4. Install the required Python packages(`PyQt5` and `mysql-connector-python`). You can do this by using the `requirements.txt`:
```bash
pip install -r requirements.txt
```
5. Configure the database connection:
- Open `options.py`.
- Update the host, username, and password variables with your own database credentials (lines 18 to 21).

6. Set up the MySQL database:
- Create a new database in MySQL.
- Import the database schema if provided.
7. Run `app.py`

## Used tools
- **Programming language**: Python
- **Database**: MySQL
- **GUI**: Qt

## TODO
- [ ] Change the database frome MySQL to SQLite3.
- [ ] Add an organised layout to the GUI.
- [ ] Add dark mode to the program.
