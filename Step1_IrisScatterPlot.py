"""
@author : Muhamad Irvan Dimetrio
NIM     : 18360018
Teknik Informatika
Institut Sains dan Teknologi Nasisonal
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Menampilan scatter plot perbandingan Sepal
iris = pd.read_csv('iris.csv', names=['Sepal lenght (cm)', 'Sepal width (cm)', 'Petal lenght (cm)', 'Petal width (cm)',
                                      'label'], header=0, sep=",")

sns.scatterplot(x='Sepal lenght (cm)', y='Sepal width (cm)', hue='label', data=iris).set_title('Perbandingan Sepal')
plt.figure(1) # n adalah nomor berbeda untuk setiap window gambar
plt.show()

#Menampilan scatter plot perbandingan petal
iris2 = pd.read_csv('iris.csv', names=['Sepal lenght (cm)', 'Sepal width (cm)', 'Petal lenght (cm)', 'Petal width (cm)',
                                      'label'], header=0, sep=",")

sns.scatterplot(x='Petal lenght (cm)', y='Petal width (cm)', hue='label', data=iris2).set_title('Perbandingan Petal')
plt.figure(1) # n adalah nomor berbeda untuk setiap window gambar
plt.show()
