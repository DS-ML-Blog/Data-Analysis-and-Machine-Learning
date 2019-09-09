import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# I. Import danych. Dla porównania przygotować kilka zestawów uczących

# 1. Import z pliku, usunięciecie niepotrzebnych kolumn
data1 = pd.read_csv('dane/titanic.csv', sep = ';')
data1.drop(['PassengerId', 'Name','Ticket','Cabin'],inplace = True, axis=1)
data1.dropna(inplace = True)
data1['Family'] = data1['SibSp'] + data1['Parch']

sex = pd.get_dummies(data1['Sex'], drop_first = True)
embark = pd.get_dummies(data1['Embarked'], drop_first = True)
data1 = pd.concat([data1, sex, embark], axis = 1)
data1.drop(['Sex','Embarked','SibSp', 'Parch'], axis = 1, inplace = True)

# 2. To co przedtem + usunięcie wszystkich zmiennych ciągłych (fare, age)
data2 = pd.read_csv('dane/titanic.csv', sep = ';')
data2.drop(['PassengerId', 'Name','Ticket','Cabin'],inplace = True, axis=1)
data2.dropna(inplace = True)
data2.drop(['Fare', 'Age'],inplace = True, axis=1)
data2['Family'] = data2['SibSp'] + data2['Parch']

sex = pd.get_dummies(data2['Sex'], drop_first = True)
embark = pd.get_dummies(data2['Embarked'], drop_first = True)
pclass = pd.get_dummies(data2['Pclass'], drop_first = True)
data2 = pd.concat([data2, sex, embark, pclass], axis = 1)
data2.drop(['Sex','Embarked', 'Pclass','SibSp', 'Parch'], axis = 1, \
            inplace = True)

# 3. To co przedtem + wywalenie Family i embarked
data3 = pd.read_csv('dane/titanic.csv', sep = ';')
data3.drop(['PassengerId', 'Name','Ticket','Cabin'],inplace = True, axis=1)
data3.dropna(inplace = True)
data3.drop(['Fare', 'Age', 'SibSp', 'Parch', 'Embarked'],inplace = True, axis=1)

sex = pd.get_dummies(data3['Sex'], drop_first = True)
pclass = pd.get_dummies(data3['Pclass'], drop_first = True)
data3 = pd.concat([data3, sex, pclass], axis = 1)
data3.drop(['Sex', 'Pclass'], axis = 1, inplace = True)

# 4. To co przedtem + wywalenie klasy (sama płeć)
data4 = pd.read_csv('dane/titanic.csv', sep = ';')
data4.drop(['PassengerId', 'Name','Ticket','Cabin'],inplace = True, axis=1)
data4.dropna(inplace = True)
data4.drop(['Fare', 'Age', 'SibSp', 'Parch', 'Embarked', 'Pclass'], \
            inplace = True, axis=1)

sex = pd.get_dummies(data4['Sex'], drop_first = True)
data4 = pd.concat([data4, sex], axis = 1)
data4.drop(['Sex'], axis = 1, inplace = True)

# II. Machine learning

# 1. Dla data1
# a) Podział danych na uczące i testowe
X = data1.drop(['Survived'], axis = 1)
y = data1['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, \
                                                    random_state = 1)

# b) Stworzenie modelu uczącego i sprawdzenie wyników
logmodel = LogisticRegression(solver = 'lbfgs')
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

cm = confusion_matrix(y_test, predictions)
performance1 = (cm[0,0] + cm[1,1])/sum(sum(cm))

# 2. Dla data2
# a) Podział danych na uczące i testowe
X = data2.drop(['Survived'], axis = 1)
y = data2['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, \
                                                    random_state = 1)

# b) Stworzenie modelu uczącego i sprawdzenie wyników
logmodel = LogisticRegression(solver = 'lbfgs')
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

cm = confusion_matrix(y_test, predictions)
performance2 = (cm[0,0] + cm[1,1])/sum(sum(cm))

# 3. Dla data3
# a) Podział danych na uczące i testowe
X = data3.drop(['Survived'], axis = 1)
y = data3['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, \
                                                    random_state = 1)

# b) Stworzenie modelu uczącego i sprawdzenie wyników
logmodel = LogisticRegression(solver = 'lbfgs')
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

cm = confusion_matrix(y_test, predictions)
performance3 = (cm[0,0] + cm[1,1])/sum(sum(cm))

# 4. Dla data4
# a) Podział danych na uczące i testowe
X = data4.drop(['Survived'], axis = 1)
y = data4['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, \
                                                    random_state = 1)

# b) Stworzenie modelu uczącego i sprawdzenie wyników
logmodel = LogisticRegression(solver = 'lbfgs')
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

cm = confusion_matrix(y_test, predictions)
performance4 = (cm[0,0] + cm[1,1])/sum(sum(cm))

# ---------------------------------------------------------
print(performance1)
print(performance2)
print(performance3)
print(performance4)
