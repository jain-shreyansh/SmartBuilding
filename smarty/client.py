import apiai
import json


CLIENT_ACCESS_TOKEN = '706fa003513a45c5a09c06b7de3bd107'


def extractParams(dc):
    ctx = dc['result']['contexts']
    params = {}
    for elem in ctx:
        elem_params = elem['parameters']
        for k, v in elem_params.items():
            params[k] = v
    return params

if __name__ == '__main__':
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    while(True):
        request = ai.text_request()
        request.lang = 'de'
        request.session_id = "oshack-vit-1"
        request.query = input()
        response = request.getresponse()
        json_resp = json.loads(response.read())
        print (json_resp['result']['fulfillment']['speech'])
        print(extractParams(json_resp))

