\# 📘 Week 8 – Database \& CSV Integration Project



This project demonstrates how to set up a small database system using Python, load multiple CSV files, and perform basic operations such as user authentication and incident management.



It includes:



\- Automatic database creation  

\- Table creation  

\- CSV → Database mapping  

\- User registration \& login  

\- Basic CRUD operations  

\- Console summaries + debug logs  



---



\## 🚀 Features



\### ✅ 1. Database Setup  

The script automatically:

\- Connects to SQLite  

\- Creates tables  

\- Loads CSV data  

\- Maps CSV → correct DB fields  



\### ✅ 2. CSV Import System  

Supported CSV files inside the `DATA/` folder:

\- `cyber\_incidents.csv`

\- `datasets\_metadata.csv`

\- `it\_tickets.csv`



Each file is read, cleaned, mapped, and inserted into its table.



\### ✅ 3. User Authentication  

Includes:

```python

register\_user(username, password, role)

login\_user(username, password)

```

Passwords are safely hashed using \*\*bcrypt\*\*.



\### ✅ 4. Incident Management  

Includes:

\- Creating new incidents  

\- Viewing all incidents  



---



\## 📂 Project Structure



```

project/

│── DATA/

│   ├── cyber\_incidents.csv

│   ├── datasets\_metadata.csv

│   └── it\_tickets.csv

│

│── app/

│   ├── data/

│   │   ├── db.py

│   │   ├── schema.py

│   │   └── incidents.py

│   ├── services/

│   │   └── user\_service.py

│   └── \_\_init\_\_.py

│

│── main.py

│── README.md

```



---



\## 🛠️ Requirements



Install all Python dependencies:



```

pip install bcrypt pandas sqlalchemy

```



---



\## ▶️ How to Run



1\. Ensure all CSVs are inside `DATA/`

2\. Install required libraries

3\. Run the program:



```

python main.py

```



This will:

\- Create tables  

\- Load CSV data  

\- Show a summary  

\- Test user registration + login  

\- Insert a sample incident  



---



\## 🔍 Debug Output



The script prints helpful information like:



\- CSV column names  

\- First row preview  

\- Number of mapped rows  

\- Records inserted per table  



---



\## 📌 Notes



\- The database is SQLite and is created automatically  

\- All CSV loading logic is inside `load\_all\_csv\_data()`  

\- The structure is clean and extendable for future assignments  



---



\## 🧾 Example Output



```

============================================

STARTING COMPLETE DATABASE SETUP

============================================

Loaded 55 rows into cyber\_incidents

Loaded 12 rows into datasets\_metadata

Loaded 30 rows into it\_tickets



Database Summary:

&nbsp; users: 0 rows

&nbsp; cyber\_incidents: 55 rows

&nbsp; datasets\_metadata: 12 rows

&nbsp; it\_tickets: 30 rows



--- Testing Authentication ---

Register: User created successfully

Login: Login successful



--- Testing CRUD Operations ---

Created incident #1

```



---




\# 📘 Week 8 – Database \& CSV Integration Project



This project demonstrates how to set up a small database system using Python, load multiple CSV files, and perform basic operations such as user authentication and incident management.



It includes:



\- Automatic database creation  

\- Table creation  

\- CSV → Database mapping  

\- User registration \& login  

\- Basic CRUD operations  

\- Console summaries + debug logs  



---



\## 🚀 Features



\### ✅ 1. Database Setup  

The script automatically:

\- Connects to SQLite  

\- Creates tables  

\- Loads CSV data  

\- Maps CSV → correct DB fields  



\### ✅ 2. CSV Import System  

Supported CSV files inside the `DATA/` folder:

\- `cyber\_incidents.csv`

\- `datasets\_metadata.csv`

\- `it\_tickets.csv`



Each file is read, cleaned, mapped, and inserted into its table.



\### ✅ 3. User Authentication  
# 📘 Week 8 – Database & CSV Integration Project

This project demonstrates how to set up a small database system using Python, load multiple CSV files, and perform basic operations such as user authentication and incident management.

It includes:

- Automatic database creation  
- Table creation  
- CSV → Database mapping  
- User registration & login  
- Basic CRUD operations  
- Console summaries + debug logs  

---

## 🚀 Features

### ✅ 1. Database Setup  
The script automatically:
- Connects to SQLite  
- Creates tables  
- Loads CSV data  
- Maps CSV → correct DB fields  

### ✅ 2. CSV Import System  
Supported CSV files inside the `DATA/` folder:
- `cyber_incidents.csv`
- `datasets_metadata.csv`
- `it_tickets.csv`

Each file is read, cleaned, mapped, and inserted into its database table.

### ✅ 3. User Authentication  
Includes:
```python
register_user(username, password, role)
login_user(username, password)
```
Passwords are safely hashed using **bcrypt**.

### ✅ 4. Incident Management  
Includes:
- Creating new incidents  
- Viewing all incidents  

---

## 📂 Project Structure

```
project/
│── DATA/
│   ├── cyber_incidents.csv
│   ├── datasets_metadata.csv
│   └── it_tickets.csv
│
│── app/
│   ├── data/
│   │   ├── db.py
│   │   ├── schema.py
│   │   └── incidents.py
│   ├── services/
│   │   └── user_service.py
│   └── __init__.py
│
│── main.py
│── README.md
```

---

## 🛠️ Requirements

Install all needed Python modules:

```
pip install bcrypt pandas sqlalchemy
```

---

## ▶️ How to Run the Project

1. Ensure the `DATA/` folder contains all CSV files  
2. Install the required dependencies  
3. Run the program:

```
python main.py
```

The script will:
- Create database tables  
- Import CSV data  
- Display a summary  
- Test registration & login  
- Insert a sample incident  

---

## 🔍 Debug Output

The script prints helpful logs such as:

- CSV column names  
- First row preview  
- Number of mapped rows  
- Rows inserted into each table  

---

## 📌 Notes

- SQLite database is created automatically  
- CSV loading logic is handled inside `load_all_csv_data()`  
- Easy to extend for future assignments or features  

---

## 🧾 Example Output

```
============================================
STARTING COMPLETE DATABASE SETUP
============================================
Loaded 55 rows into cyber_incidents
Loaded 12 rows into datasets_metadata
Loaded 30 rows into it_tickets

Database Summary:
  users: 0 rows
  cyber_incidents: 55 rows
  datasets_metadata: 12 rows
  it_tickets: 30 rows

--- Testing Authentication ---
Register: User created successfully
Login: Login successful

--- Testing CRUD Operations ---
Created incident #1
```

