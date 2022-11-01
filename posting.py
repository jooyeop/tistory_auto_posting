import requests

def getAccessToken():
    url = "https://www.tistory.com/oauth/access_token?"
    client_id = "e3c0e269e2b2d03851835d1bad98a0ca"
    client_secret = "e3c0e269e2b2d03851835d1bad98a0caed8cf45df49e8ea3e52ad8e34296540f767d2498"
    code = "cbb271a122a866ca35a22a738090b0f617088870c160750b3a42965da3c180a99fcfdc25"
    redirect_uri = "https://yeobing.tistory.com/"
    grant_type="authorization_code" # authorization_code 고정

    data = url
    data += "client_id="+client_id+"&"
    data += "client_secret="+client_secret+"&"
    data += "redirect_uri="+redirect_uri+"&"
    data += "code="+code+"&"
    data += "grant_type="+grant_type
    print(data)
    return  requests.get(data)

if __name__ == "__main__":
    token = getAccessToken().content
    print(token.decode('utf-8'))

access_code = '7d13a517677238efc2b674a367736d23_9e310677c4e36c1c8db304f82203de2c'