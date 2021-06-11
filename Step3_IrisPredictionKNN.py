"""
@author : Muhamad Irvan Dimetrio
NIM     : 18360018
Teknik Informatika
Institut Sains dan Teknologi Nasisonal
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Meload Dataset dari file csv dan mengekstrak fitur dan label classnya
iris = pd.read_csv('iris.csv', names =['Sepal lenght (cm)', 'Sepal width (cm)', 'Petal lenght (cm)',
                                       'Petal width (cm)', 'label'], header = 0)

# Mengubah label spesies bunga menjadi angka unik 0,1,2
Y = iris.iloc [:, 4]
label_encoder = LabelEncoder()
iris['label']= label_encoder.fit_transform(iris['label'])
iris['label'].unique()
label_encoder_y = LabelEncoder()
Y= label_encoder_y.fit_transform(Y)

fitur = iris.iloc[:, 0:2].values


# Mengambil algoritma K Nearest Neigbor sebagai model
model = KNeighborsClassifier(n_neighbors=1)

# Latih model menggunakan dataset
model.fit(fitur, Y)

#Prediksi dengan data yang dimasukkan
SepalLengthInput = input("Masukkan Sepal length(cm)? \n"+ ">>>")
SepalWidthInput = input("Masukkan Sepal width(cm) ? \n"+">>>")
LengthData = float(SepalLengthInput)
WidthData = float(SepalWidthInput)

prediksinya = model.predict([[LengthData, WidthData]])
if prediksinya == 0:
    print("Iris Setosa")
elif prediksinya == 1:
    print("Iris Versicolour")
else:
    print("Iris Virginica")