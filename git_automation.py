import requests

def make_http_request(url):
    token = "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"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response


def main():
    new_list = []
    
    org_name = "comcast-ghec-poc"
    
    # get all repo names of the organization
    url = "https://api.github.com/orgs/" + org_name + "/repos"
    response = make_http_request(url)
    repos = []
    if response.status_code == 200:
        print("Request successful!")
        resp = response.json()
        for data in resp:
            repos.append(data["name"])
    else:
        print("Request failed with status code:", response.status_code)
    print(repos)
    for repo in repos:

        #get collaborators details
        collaborator_url = "https://api.github.com/repos/" + org_name + "/" + repo + "/collaborators"
        response = make_http_request(collaborator_url)
        if response.status_code == 200:
            print("Request successful!")
            resp = response.json()

            for data in resp:
                new_dict = {"login": data["login"], "role_name": data["role_name"]}
                new_list.append(new_dict)     
        else:
            print("Request failed with status code:", response.status_code)

        #get teams details
        teams_url = "https://api.github.com/repos/" + org_name + "/" + repo + "/teams"
        response = make_http_request(teams_url)

        if response.status_code == 200:
            print("Request successful!")
            resp = response.json()
            admin_role ={
        "admin": True,
        "maintain": True,
        "push": True,
        "triage": True,
        "pull": True
        }
            for data in resp:
                if "permissions" in data: 
                    if data["permissions"] == admin_role:
                        new_dict = {"name": data["name"], "role_name": "admin"}  
                    else:
                        new_dict = {"name": data["name"], "role_name": "not_admin"} 
                    
                new_list.append(new_dict)  
            print (new_list)  
        else:
            print("Request failed with status code:", response.status_code)




if __name__ == "__main__":
    main()

