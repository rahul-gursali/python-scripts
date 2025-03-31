import requests

JENKINS_URL = "http://jenkins-server/job/my-pipeline/build"
USER = "admin"
API_TOKEN = "your-token"

response = requests.post(JENKINS_URL, auth=(USER, API_TOKEN))
print(response.status_code)
