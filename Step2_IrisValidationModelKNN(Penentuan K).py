"""
@author : Muhamad Irvan Dimetrio
NIM     : 18360018
Teknik Informatika
Institut Sains dan Teknologi Nasisonal
"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Meload Dataset dari file csv dan mengekstrak fitur dan label classnya
iris = pd.read_csv('iris.csv', names =['Sepal lenght (cm)', 'Sepal width (cm)', 'Petal lenght (cm)',
                                       'Petal width (cm)', 'label'], header = 0)
fitur = iris.iloc[:, 0:2].values
label = iris.iloc[:, -1].values

# Splitting the dataset into the Training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(fitur, label, test_size=1/3, random_state=42)
print("Data Training: ")
print(X_train)
print("Data Test: ")
print(X_test)

#Mengambil model K=3 Nearest Neighbor dan melatih model dengan X_train, Y_train
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, Y_train)

#Hitung akurasi dari model
akurasi = model.score(X_train, Y_train)
print("Akurasi dari model adalah : {}".format(akurasi))
