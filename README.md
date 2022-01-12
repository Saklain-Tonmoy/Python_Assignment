## Project Name

> Web Scraping using Python and Scrapy

## Description

> It's a Python based Web Scrawler using Scrapy for Scraping the hotels information from https://www.kayak.co.in/ website

## Project Link

> https://github.com/Saklain-Tonmoy/Python_Assignment

## Languages Used

> - Python
> - MYSQL

## Tools and Packages Used

> - Scrapy
> - MYSQL Connector
> - Fake-User-Generator
> - Python Virtual Environment

## Prerequisites

> - Install Python (recommended version 3.8)
> - Install XAMPP/WAMPP (recommended XAMPP)

## Database Creation
### Step 1
> Create a database from XAMPP(localhost) named (mydb) and import the mydb.sql file from cloned folder.

```
CREATE DATABASE [IF NOT EXISTS] mydb;
```
### Step 2
> Import the (mydb.sql) provided with the cloned folder into the database.


## Project Setup

### Step 1

> Please go to the folder where you want to install the application and open the Termial/CMD. Then type the following command and press enter

```
git clone https://github.com/Saklain-Tonmoy/Python_Assignment
```

### Step 2

> After cloning please open the folder using cmd or VSCode, and run the following commands to install and activate the Virtual Environment

First,
```
python3 -m venv my-env
```
Second,
```
source my-env/bin/activate

```

### Step 3
> Install Scrapy using the following command
```
pip install Scrapy
```


### Step 4

> Then change the directory using the following command

```
cd Scrapy_Crawl
```

### Step 5

> Install MYSQL Connector by running the following commandfor interacting with Database

```
python -m pip install mysql-connector-python
```

### Step 6

> Install Fake User Generator for avoiding the blocking of bot Scrawling by running the following command

```
pip install scrapy-fake-useragent
```

### Step 7

> Finally, run the project using following command

```
scrapy crawl hotels
```

### Finally, thanks from Saklain Tonmoy :neutral_face:
