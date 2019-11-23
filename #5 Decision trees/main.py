import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("loan_data.csv")
# I. Preprocessing
# rename
rename_dict = {"credit.policy": "decision", "log.annual.inc": "log_income", 
               "dti": "debt_to_income", "days.with.cr.line":
                   "days_with_cr_line",
               "revol.bal": "amount_unpaid", "inq.last.6mths":
                   "recent_inq_num",
               "delinq.2yrs": "payment_delay_num",
               "not.fully.paid": "not_fully_paid"}

df.rename(columns=rename_dict, index=str,  inplace=True)

df["purpose"].replace(df["purpose"].unique(),
                      ["purpose"+str(i)
                       for i in range(len(df["purpose"].unique()))],
                      inplace=True)

purpose = pd.get_dummies(df["purpose"], drop_first=True)
df.drop(["purpose"], inplace=True, axis=1)
df = pd.concat([df, purpose], axis=1)

# drop
df.drop(["int.rate", "revol.util", "pub.rec"], axis=1, inplace=True)
df["income"] = df["log_income"].apply(np.exp)

# II. EDA
# a)
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
sns.distplot(df["installment"], kde=False, hist_kws=dict(edgecolor="k",
             linewidth=1))
plt.title("Rozkład wielkości raty miesięcznej", fontsize=22)
plt.xlabel("Wielkość raty [$]", fontsize=20)
plt.ylabel("Ilość klientów", fontsize=20)
ax.tick_params(axis="both", which="major", labelsize=20)
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.9)
plt.savefig(figure=fig, fname="plots/5AD1.png")

# b)
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
sns.distplot(df["log_income"], kde=False, hist_kws=dict(edgecolor="k",
             linewidth=1))
plt.title("Rozkład wartości logarytmu \nrocznego przychodu", fontsize=22)
plt.xlabel("Logarytm rocznego przychodu", fontsize=20)
plt.ylabel("Ilość klientów", fontsize=20)
ax.tick_params(axis="both", which="major", labelsize=20)
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.9)
plt.savefig(figure=fig, fname="plots/5AD2.png")

# c)
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
sns.distplot(df["fico"], kde=False, hist_kws=dict(edgecolor="k",
             linewidth=1))
plt.title("Rozkład wartości wskaźnika FICO", fontsize=22)
plt.xlabel("Wskaźnik FICO", fontsize=20)
plt.ylabel("Ilość klientów", fontsize=20)
ax.tick_params(axis="both", which="major", labelsize=20)
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.9)
plt.savefig(figure=fig, fname="plots/5AD3.png")

# d)
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
sns.scatterplot(df["fico"], df["days_with_cr_line"])
plt.title("Zależność między wskaźnikiem FICO\na liczbą dni z zadłużeniem",
          fontsize=22)
plt.xlabel("Wskaźnik FICO", fontsize=20)
plt.ylabel("Liczba dni z zadłużeniem", fontsize=20)
ax.tick_params(axis="both", which="major", labelsize=20)
plt.subplots_adjust(left=0.18, bottom=0.1, right=0.95, top=0.9)
plt.savefig(figure=fig, fname="plots/5AD4.png")

# e)
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
sns.boxplot(df["decision"], df["debt_to_income"])
plt.title("Rozkład współczynnika debt to income \ndla poszczególnych statusów"
          " decyzji", fontsize=22)
plt.xlabel("Decyzja", fontsize=20)
plt.ylabel("Wartość współczynnika debt to income", fontsize=20)
ax.tick_params(axis="both", which="major", labelsize=20)

# f)
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
sns.scatterplot(df["log_income"], df["installment"])
plt.title("Zależność wielkości raty od logarytmu\n przychodu rocznego",
          fontsize=22)
plt.xlabel("Logarytm przychodu rocznego", fontsize=20)
plt.ylabel("Wielkość raty miesięcznej [$]", fontsize=20)
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.9)
plt.savefig(figure=fig, fname="plots/5AD6.png")


# III. Machine learning
# 1. Decision tree
X = df.drop(["decision"], axis=1)
y = df["decision"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,
                                                    random_state=101)

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
dtree_pred = dtree.predict(X_test)

cm = confusion_matrix(y_test, dtree_pred)
print(cm)
print("Accuracy: ", str(round(accuracy_score(y_test, dtree_pred), 3)))

# 2. Random forest
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)

rfc_cm = confusion_matrix(y_test, rfc_pred)
print("\n", rfc_cm)
print("Accuracy: ", str(round(accuracy_score(y_test, rfc_pred), 3)))

# 3. Logistic regression

lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

lr_cm = confusion_matrix(y_test, lr_pred)
print("\n", lr_cm)
print("Accuracy: ", str(round(accuracy_score(y_test, lr_pred), 3)))

plt.close("all")
