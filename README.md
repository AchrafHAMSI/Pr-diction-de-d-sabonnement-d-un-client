Vérifier si le dossier du projet contient les fichiers suivant : 
-api.py
-Authentication_test.py
-docker-compose.yml
-Dockerfile
-Dockerfile1
-Dockerfile2
-ml_pour_genrer_model.py
-ML_test.py
-requirements.txt
-deployment-eval.yml
-ingress-eval.yml
-service-eval.yml

Installer les fichiers suivant :

- Installer le fichier requirements.txt file. Command: pip install requirements.txt

- generer les modéles de machine learning pour les utiliser dans api.py. Command: python3 ml_pour_generer_model.py

- Lancer le docker compose qui va créer les images. Command: docker-compose up

Command:Exécutez la commande suivante dans le terminal pour installer minikube
```console
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
- Start minikube. command:  minikube start

- Exécutez la commande suivante pour lancer le dashboard de minikube : minikube dashboard --url=true

- lancer kubectl: kubectl proxy --address='0.0.0.0' --disable-filter=true

- Déploiement d'une API avec Kubernetes. Command: kubectl create -f my-deployment-eval.yml

- créer le service ClusterIp . Commande: kubectl create -f my-service-eval.yml

- Enable ingress. Command : minikube addons enable ingress

- créeringress. Command: kubectl create -f my-ingress-eval.yml

- Execute this command to get IP address of the Ingress: kubectl get ingress


les utilisateurs qui ont accés au API sont :
●	alice: wonderland
●	bob: builder
●	clementine: mandarine# Pr-diction-de-d-sabonnement-d-un-client
