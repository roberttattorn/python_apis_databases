'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''
import requests
from pprint import pprint
code=input("Please select from the following options (enter the number of the action you'd like to take):\n
1) Create a new account (POST)\n
2) View all your tasks (GET)\n
3) View your completed tasks (GET)\n
4) View only your incomplete tasks (GET)\n
5) Create a new task (POST)\n
6) Update an existing task (PATCH/PUT)\n
7) Delete a task (DELETE)\n")

if code == 1:
  name = input("Please input your name")
  password = input("Please select your password")
  data = {
   "name":name,
   "password":password
  }
  response = requests.post("http://demo.codingnomads.co:8080/tasks_api/users",data)
  print(response.status_code)
if code == 2:
  response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?name=[name]&task=*")
  data = response.json()
  pprint(data)
if code == 3:
  response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?name=[name]&task!=''")
  data = response.json()
  pprint(data)
if code == 4:
  response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?name=[name]&task=''")
  data = response.json()
  pprint(data)
if code == 5:
  name = input("your name please")
  task = input("create a task, please")
  data = {
    "name":name,
   "task":task
  }
  response = requests.post("http://demo.codingnomads.co:8080/tasks_api/users",data)
if code == 6:
  name = input("your name please")
  task = input("task to update")
  data = {
    "name":name,
   "task":task
  }
  response = requests.put("http://demo.codingnomads.co:8080/tasks_api/users",data)
  if code == 7:
    user = input("user to delete")
    requests.delete("http://demo.codingnomads.co:8080/tasks_api/users?name=user")
  
                           
