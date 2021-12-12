'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''
import requests
response = requests.delete("http://demo.codingnomads.co:8080/tasks_api/users/Bob")

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?first_name=Bob")
print(response.status_code)
