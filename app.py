from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

import os
import requests
import json

_client_id = os.environ.get('CLIENT_ID')
_client_secret = os.environ.get('CLIENT_SECRET')
_token_url = 'https://connect.visma.com/connect/token'

client = BackendApplicationClient(client_id=_client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=_token_url, 
            client_id=_client_id,
            client_secret=_client_secret,
            scope='vismanet_erp_service_api:create vismanet_erp_service_api:delete vismanet_erp_service_api:read vismanet_erp_service_api:update',
            tenant_id=os.environ.get('TENANT_ID'))

_accesstoken = token['access_token']

response = requests.get("https://integration.visma.net/API/service/controller/api/v1/inventory/",                          
                            headers={
                                'Accept': 'application/json',
                                'Authorization': 'Bearer ' + _accesstoken                                
                            }
                            )

if response.status_code == 200:
    item = json.loads(response.text)

    result = {
        "Description": item['description']            
    }
    