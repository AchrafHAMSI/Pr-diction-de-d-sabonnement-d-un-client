import os
import requests
import time


#définition de l'adresse de l'API
api_address = '108.128.169.67'

# port de l'API
api_port = 8000

# requête1
r1 = requests.get(
        url='http://{address}:{port}/authentication'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland'
    }
)

output1 = '''
============================
    Authentication test
============================

request done at "/authentication"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''
# requete2
r2 = requests.get(
        url='http://{address}:{port}/authentication'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder'
    }
)

output2 = '''
============================
    Authentication test
============================

request done at "/authentication"
| username="bob"
| password="builder"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''
# requete3
r3 = requests.get(
        url='http://{address}:{port}/authentication'.format(address=api_address, port=api_port),
    params= {
        'username': 'clementine',
        'password': 'mandarine'
    }
)

output3 = '''
============================
    Authentication test
============================

request done at "/authentication"
| username="clementine"
| password="mandarine"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

trois_requetes = [r1,r2,r3]
trois_outputs = [output1, output2, output3]

for r, output in zip (trois_requetes, trois_outputs):
    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(status_code=status_code, test_status=test_status))
    output = output.format(status_code=status_code, test_status=test_status)

    #impression dans un fichier
if os.environ.get('LOG') == "1":
    with open('api_test.log', 'a') as file:
        file.write(output)

#    time.sleep(0)
#time.sleep(3600)