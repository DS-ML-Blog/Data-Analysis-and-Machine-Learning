import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, \
                            accuracy_score
from sklearn.svm import SVC

df = pd.read_csv('dane/iris.csv')
df['Legenda'] = df['variety']
df['variety'].replace( {'Setosa':1, 'Versicolor':2, 'Virginica':3}, \
                        inplace = True)

# I. Wizualizacja
fig = plt.figure(figsize = (4,4), facecolor = 'white')

df.rename(columns={'petal.length':'Długość płatka [cm]', \
                   'petal.width':'Szerokość płatka [cm]', \
                   'sepal.length': 'Długość działki [cm]', \
                   'sepal.width':'Szerokość działki [cm]'}, index = str, \
                   inplace = True)
sns.pairplot(df.drop(['variety'], axis = 1), hue = 'Legenda')

plt.savefig(figure = fig, fname = 'plots/3AD1.png')

# II. Klasyfikacja
# 1. KNN
X = df.drop(['variety', 'Legenda'], axis = 1)
y = df['variety']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, \
                                                    random_state = 101)

accuracyList = []
for k in range(1,21):
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    accuracyList.append(accuracy_score(y_test, predictions))

fig = plt.figure(figsize = (9,7), facecolor = 'white')
ax = fig.add_subplot(111)
plt.plot(range(1,21), accuracyList,'o', linestyle = 'dashed', markersize = 4)
plt.ylabel('Dokładność (accuracy)', fontsize = 17)
plt.xlabel('K', fontsize = 17)
plt.title('Zależność dokładności modelu od ilości sąsiadów (K)', fontsize = 18,\
          y = 1.05)
plt.xticks(np.arange(1,21,2))
ax.tick_params(axis='both', labelsize = 14)
plt.savefig(Figure = fig, fname = 'plots/3AD2.png')
plt.close(fig)

K = 5
knn = KNeighborsClassifier(n_neighbors = K)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)

print(confusion_matrix(y_test, predictions))
print(round(accuracy_score(y_test, predictions),2))

# 2. SVM
svm = SVC()
svm.fit(X_train, y_train)
predictions = svm.predict(X_test)

print(confusion_matrix(y_test, predictions))
print(round(accuracy_score(y_test, predictions),2))
