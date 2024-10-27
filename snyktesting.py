import requests
import json

def create_snyk_project(snyk_token, project_path):
    headers = {
        "Authorization": f"token {snyk_token}",
        "Content-Type": "application/vnd.api+json"
    }

    data = {
        "origin": project_path
    }

    url = "https://api.snyk.io/rest/orgs/f4de899a-9507-4bc8-848d-7778456c2456/projects?version=2024-06-26"
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    return response.json()

token = "f26a5258-db80-4d1c-9807-572d4b6c3cf6"
project_path = "https://github.com/madhusmita65/myNewRepo.git"
print(create_snyk_project(token, project_path))

"""
{'error': True, 'message': 'The org madhusmita65-maMYwMK5ABgbfGYARK4Vqs (f4de899a-9507-4bc8-848d-7778456c2456) is not entitled for api access. Please upgrade your plan to access this capability', 'cliMessage': 'The org madhusmita65-maMYwMK5ABgbfGYARK4Vqs (f4de899a-9507-4bc8-848d-7778456c2456) is not entitled for api access. Please upgrade your plan to access this capability', 'userMessage': 'The org madhusmita65-maMYwMK5ABgbfGYARK4Vqs (f4de899a-9507-4bc8-848d-7778456c2456) is not entitled for api access. Please upgrade your plan to access this capability'}
"""
