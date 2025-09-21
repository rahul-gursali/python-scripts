import json

with open("terraform.tfstate") as f:
    state = json.load(f)

for resource in state["resources"]:
    if resource["type"] == "aws_instance":
        for instance in resource["instances"]:
            print(instance["attributes"]["id"])
