import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


# 1. Load and preprocess data
df = pd.read_csv("data/titanic.csv", sep=';')

df.drop(["PassengerId", "Name", "Ticket", "Cabin"], inplace=True, axis=1)
df.dropna(inplace=True)
df["Family"] = df["SibSp"] + df["Parch"]

sex = pd.get_dummies(df["Sex"], drop_first=True)
embark = pd.get_dummies(df["Embarked"], drop_first=True)
df = pd.concat([df, sex, embark], axis=1)
df.drop(["Sex", "Embarked", "SibSp", "Parch"], axis=1, inplace=True)


# 2. Train ML model
X = df.drop(["Survived"], axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=1)


logmodel = LogisticRegression(solver="lbfgs")
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

cm = confusion_matrix(y_test, predictions)
performance = (cm[0, 0] + cm[1, 1])/sum(sum(cm))

print(performance)
