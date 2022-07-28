from fastapi import FastAPI
import uvicorn
import pickle
import secrets
from flask import Flask,request
import base64
import json
api = Flask(import_name='api_churn')

model = pickle.load(open("churn_LogisticRegression.pkl", 'rb'))
classifier = pickle.load(open("Churn_RandomForestClassifier.pkl", "rb"))

#checker le fonctionnement de l'API
@api.get('/status')
def is_running():
	return str(1)

users = {"alice": "d29uZGVybGFuZA==", "bob": "YnVpbGRlcg==" , "clementine": "bWFuZGFyaW5l"}

#def decode_base64(base64_msg):
#  base64_bytes = base64_msg.encode('utf-8')
#  mdp_bytes = base64.b64decode(base64_bytes+ b'==')
#  mdp = mdp_bytes.decode('utf-8')
#  return mdp

def decode_base64(mdp):
    b = mdp.encode("UTF-8")
    e = base64.b64encode(b)
    s = e.decode("UTF-8")        
    return s

#liste des auth
from flask import jsonify, abort, make_response
@api.get('/authentication')
def auth():
    if authentication():
        return "welcome"
        

def authentication():
    username= request.args['username']
    password= request.args['password']
    decoded_password=decode_base64(password)
    if users[username]==decoded_password:
        return True
    else:
        abort (400)
#message d'erreur si le mot de passe est eronne
@api.errorhandler(400)
def password_not_correct(error):
	return make_response(jsonify({'error': 'password not correct'}), 403)

# convertir string to dict
def parse_data(data):
  if isinstance(data,str):
    return json.loads(data)
  return data
# le model LogisticRegression
@api.get('/v1/lr')
def get_is_transaction_fraud2():
    if authentication():
        client = parse_data(request.args['client'])
        # prédiction avec le model LogisticRegression
        v_client=[list(client.values())]
        model_prediction = model.predict(v_client)
        # affichage des résultats:

        resultat_lr='''
        - Resultat avec le modèle LogisticRegression: {contrat_status}'''
        if model_prediction == 1:
            contrat_status = "le client va résilier" 
        else:
            contrat_status = "le client ne va pas résilier"
        lr=resultat_lr.format(contrat_status=contrat_status)
        return lr
#le model de RandomForestClassifier:
@api.get('/v2/rfc')
def get_is_transaction_fraud1():

    #prediction avec le model de RandomForestClassifier:
    if authentication():
        client = parse_data(request.args['client'])
        v_client=[list(client.values())]
        RandomForestClassifier_prediction = classifier.predict(v_client)
        # affichage des résultats avec les kmeans
        Resultat_RFC='''
        - Resultat avec le modèle RandomForestClassifier: {contrat_status}'''
        if RandomForestClassifier_prediction == 1:
            contrat_status = "le client va résilier" 
        else:
            contrat_status = "le client ne va pas résilier"
        RFC=Resultat_RFC.format(contrat_status=contrat_status)

        return RFC


#message d'erreur si le mot de passe est eronne
@api.errorhandler(400)
def password_not_correct(error):
	return make_response(jsonify({'error': 'password not correct'}), 403)   
if __name__ == '__main__':
	api.run(host="0.0.0.0", port=8000)
