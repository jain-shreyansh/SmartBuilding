import apiai
import json
import dbutils


CLIENT_ACCESS_TOKEN = '706fa003513a45c5a09c06b7de3bd107'


def extractParams(dc):
    ctx = dc['result']['contexts']
    params = {}
    for elem in ctx:
        elem_params = elem['parameters']
        for k, v in elem_params.items():
            params[k] = v
    return params

def extractIntentName(dc):
    return dc['result']['metadata']['intentName']

def performDBOps(conn, dc):
    intent_name = extractIntentName(dc)
    params = extractParams(dc)
    if intent_name == 'GetGroceries':
        dbutils.insert_grocs(conn, params['apt_number'],params['name'], params['groceries'])
    elif intent_name == 'GetComplaint':
        dbutils.insert_complaint(conn, params['apt_number'], params['name'], params['complaint'])


if __name__ == '__main__':
    conn = dbutils.check_db()
    cur = conn.cursor()
    cur.execute('select * from complaints')
    rows = cur.fetchall()
    for row in rows:
        print(row['complaint'])

    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    while(True):
        request = ai.text_request()
        request.lang = 'de'
        request.session_id = "oshack-vit-1"
        request.query = input()
        response = request.getresponse()
        json_resp = json.loads(response.read())
        print(json_resp['result']['fulfillment']['speech'])
        performDBOps(conn, json_resp)

