import os
import requests
import time
import json
#définition de l'adresse de l'API
api_address = '108.128.169.67'

# port de l'API
api_port = 8000

# requête1 | tester l'api!

client = {
        "gender": 1,
        "SeniorCitizen": 0,
        "Partner": 1,
        "Dependents": 1,
        "tenure": 72,
        "PhoneService": 1,
        "PaperlessBilling": 0,
        "MonthlyCharges": 24.10,
        "TotalCharges": 1734.65,
        "MultipleLines_1": 1,
        "MultipleLines_No phone service": 0,
        "InternetService_DSL": 0,
        "InternetService_Fiber optic": 1,
        "OnlineSecurity_1": 0,
        "OnlineSecurity_No internet service" :1,
        "OnlineBackup_1": 0,
        "OnlineBackup_No internet service": 1,
        "DeviceProtection_1": 0,
        "DeviceProtection_No":1,
        "TechSupport_1": 0,
        "TechSupport_No internet service": 1,
        "StreamingTV_1": 0,
        "StreamingTV_No internet service" :1,
        "StreamingMovies_1": 0,
        "StreamingMovies_No internet service" : 1,
        "Contract_One year": 0,
        "Contract_Two year" : 1,
        "PaymentMethod_Credit card (automatic)": 1,
        "PaymentMethod_Electronic check": 0,
        "PaymentMethod_Mailed check": 0
}
jload = str(json.dumps(client))
# requête1
r1_v1 = requests.get(
        url='http://{address}:{port}/v1/lr'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'client': jload
    }
)
#print(client)
#decoder le texte en format utf-8
#output1 = r1_v1.content.decode('utf-8')
#print(output1)

output1 = '''
============================
    logistic_regression test
============================

request done at "/v1/lr"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}
result :
==>  {result}

'''
if r1_v1.status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output1.format(status_code=r1_v1.status_code, test_status=test_status,result=r1_v1.content.decode('utf-8')))
output1 = output1.format(status_code=r1_v1.status_code, test_status=test_status,result=r1_v1.content.decode('utf-8'))

r2_v2 = requests.get(
        url='http://{address}:{port}/v2/rfc'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'client': jload
    }
)
#print(client)
#decoder le texte en format utf-8

output2 = '''
============================
    randomforest test
============================

request done at "/v2/rfc"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}
result :
==>  {result}

'''
if r2_v2.status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output2.format(status_code=r2_v2.status_code, test_status=test_status,result=r2_v2.content.decode('utf-8')))
output2 = output2.format(status_code=r2_v2.status_code, test_status=test_status,result=r2_v2.content.decode('utf-8'))
#output2 = r2_v2.content.decode('utf-8')

output = output1+output2
    #impression dans un fichier
if os.environ.get('LOG') == "1":
    with open('api_test.log', 'a') as file:
        file.write(output)

