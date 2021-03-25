import requests
import requests_html


# authentication OAUTH
def get_token(grant_type,id,secret):
    params = {"grant_type":grant_type,
            "client_id":id,
            "client_secret":secret,
            "scope":"public"
            }

    r = requests.post("https://osu.ppy.sh/oauth/token",data=params)
    
    if r.status_code != 200:
        print("Token denied.")
        return -1
    else:
        about = r.json()
        print("Token granted.")
        return about['access_token']

    
    
if __name__ == "__main__":
    
    from load import load
    
    id, secret, grant_type = load()
    get_token(grant_type = grant_type,
              id = id,
              secret = secret
              )