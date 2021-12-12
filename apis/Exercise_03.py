'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests

user={
    name:"Bob:,
    email:"bob@mail.bs"
}
response = requests.post("http://demo.codingnomads.co:8080/tasks_api/users",user)
check = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?name=Bob&email=bob@mail.bs"
print(check)
