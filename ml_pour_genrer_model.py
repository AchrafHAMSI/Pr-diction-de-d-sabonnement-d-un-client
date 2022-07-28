#%matplotlib inline
import numpy as np
import pandas as pd
#!pip install imbalanced-learn
#!pip install imblearn
#!conda install -c conda-forge imbalanced-learn
from matplotlib import pyplot
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from numpy import where
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, StratifiedKFold, KFold
from sklearn.metrics import confusion_matrix, accuracy_score, balanced_accuracy_score, mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import seaborn as sns

#Importation de la dataframe churn
df = pd.read_csv('https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/churn.csv', sep= ',', header = 0, index_col = 'customerID')
print(df.describe())
print(df.head())
print(df.info())
print(df.columns)
print("les clients restent en moyenne 32 mois et paient 64 $ par mois. Cependant, cela pourrait être dû au fait que différents clients ont des contrats différents.",df.describe())
print(df.dtypes)
#visulatisation d'un jeu de données
#fig, ax = plt.subplots(4, 5, figsize=(15, 12))
#plt.subplots_adjust(left=None, bottom=None, right=None, top=1, wspace=0.3, hspace=0.4)
#for variable, subplot in zip(df.columns, ax.flatten()):
#  sns.histplot(df[variable], ax=subplot)

#sns.countplot(x='Churn',data=df,hue='gender',palette="coolwarm_r")

#vérification des variables NAN
df.isna().any()

df["PaymentMethod"].nunique()
df["PaymentMethod"].unique()

df["Contract"].nunique()
df["Contract"].unique()
#Identify unique values: ‘Payment Methods’ and ‘Contract’ are the two categorical variables in the dataset. When we look into the unique values in each categorical variables, we get an insight that the customers are either on a month-to-month rolling contract or on a fixed contract for one/two years. Also, they are paying bills via credit card, bank transfer or electronic checks.

#Vérification de la distrbtion de la varbiable target : Churn
df["Churn"].value_counts()

#transformation de type de la variable TotalCharges de OBJECT à float
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'],errors = 'coerce')
df.head()
df.info()
df.isna().sum()
df = df.fillna(df.median())
df.isna().sum()

#formatter un jeu de données

#remplacer les variables qualitatives par des variables binaires
df = df.replace(('Yes', 'No'), (1, 0))
df = df.replace(('Male', 'Female'), (1, 0))
#(f) Afficher les 10 premières lignes du DataFrame modifié.
df.head(10)
df.columns
#remplacer les variables qualitatives par des variables binaires
df= pd.get_dummies(df,drop_first=True)
df.head(10)

#Dans un DataFrame nommé X, stocker les variables explicatives du jeu de données.
X = df.drop(['Churn'], axis =1)
#Dans un DataFrame nommé y, stocker la variable cible ('churn').
y=df['Churn']
X.head()
df["Churn"].value_counts()
counter = Counter(y)
print(counter)
sns.countplot(df["Churn"]);

from imblearn.over_sampling import SMOTE
from collections import Counter
oversample = SMOTE()
X, y = oversample.fit_resample(X, y)
# summarize the new class distribution
counter = Counter(y)
print(counter)
y.head()
sns.countplot(y);

#appliquer des algorithmes ML

#(i) Importer la fonction train_test_split du sous module sklearn.model_selection. 
from sklearn.model_selection import train_test_split
#(j) Séparer les données en un jeu d'entraînement (X_train, y_train) et un jeu de test (X_test, y_test) en gardant 20% des données pour l'échantillon de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,  random_state = 42)
#(c) Affichez les dimensions de X_train, X_test, y_train et y_test à l'aide de l'attribut shape.
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)


#Entraîner le modèle sur le jeu de données d'entraînement grâce à la méthode fit de la classe LogisticRegression.
model2 = LogisticRegression(solver="newton-cg").fit(X_train, y_train)

# On prédit les y à partir de X_test

y_pred = model2.predict(X_test)

# On calcule la matrice de confusion et on l'affiche

print("\n Matrice de confusion \n", confusion_matrix(y_test, y_pred))

# On affiche l' accuracy du modèle

print("\nAccuracy:", accuracy_score(y_test, y_pred), "\n")

# On regarde s'il y a un déséquilibre de classe

print("Répartition des classes : \n", y.value_counts(), "\n")

# On affiche la balanced accuracy du modèle

print("Balanced accuracy:", round(balanced_accuracy_score(y_test, y_pred), 2))

# La balanced accuracy est inférieure que l'accuracy de 0.1, le déséquilibre de classes impacte ainsi sur les performances du modèle
#construire un modèle balanced avec pickle
import pickle
pickle_out = open("churn_LogisticRegression.pkl", "wb")
pickle.dump (model2, pickle_out)
pickle_out.close()
##Entraîner le modèle sur le jeu de données d'entraînement grâce à la méthode fit de la classe LogisticRegression.
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=200, random_state=0) 
classifier.fit(X_train, y_train) 
predictions = classifier.predict(X_test)

#
from sklearn.metrics import classification_report, accuracy_score
print(classification_report(y_test,predictions )) 
print(accuracy_score(y_test, predictions))

# On calcule la matrice de confusion et on l'affiche

print("\n Matrice de confusion \n", confusion_matrix(y_test, predictions))

# On affiche l' accuracy du modèle

print("\nAccuracy:", accuracy_score(y_test, predictions), "\n")

# On affiche la balanced accuracy du modèle

print("Balanced accuracy:", round(balanced_accuracy_score(y_test, predictions), 2))

# La balanced accuracy est inférieure que l'accuracy de 0.1, le déséquilibre de classes impacte ainsi sur les performances du modèle
#construire un modèle catBossterClassifier avec pickle
import pickle
pickle_out = open("Churn_RandomForestClassifier.pkl", "wb")
pickle.dump (classifier, pickle_out)
pickle_out.close()