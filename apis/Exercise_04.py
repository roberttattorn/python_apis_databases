'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests
from pprint import pprint
data = {
  first_name:"bob",
  last_name:"Stress",
  email:"bob@mail.bs"
}
response = put("http://demo.codingnomads.co:8080/tasks_api/users",data)
check= get("http://demo.codingnomads.co:8080/tasks_api/users?first_name=Bob&last_name=Stress&email=bob@mail.bs")
data = check.json()
pprint(data)
