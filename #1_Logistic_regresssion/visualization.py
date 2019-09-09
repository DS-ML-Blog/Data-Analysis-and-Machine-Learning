import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import pandas as pd
import os

# I. Wczytanie datasetu i reorganizacja danych
df = pd.read_csv('dane/titanic.csv',sep=';')

df.drop(['PassengerId', 'Name','Ticket','Cabin'],inplace = True, axis=1)

# najniższa cena biletu to 8 funtów
df.loc[df['Fare'] <= 8, ['Fare']] = np.mean(df['Fare'])

 # najwyższa cena biletu to 250 funtów
df.loc[df['Fare'] > 250, ['Fare']] = np.mean(df[df['Pclass']==1]['Fare'])

df.dropna(inplace = True)

df['Family'] = df['SibSp'] + df['Parch']
df.drop(['SibSp', 'Parch'], inplace = True, axis = 1)

df['Embarked'].replace('Q','Queensland',inplace = True)
df['Embarked'].replace('C','Cherbourg',inplace = True)
df['Embarked'].replace('S','Southampton',inplace = True)

# II. wizualizacja
# 1. Countlot z podziałem na miejsce gdzie wsiedli i hue z podziałem na klasy
sns.set(font_scale=2.5,palette = 'deep',rc={'figure.figsize':(10,10)})
sns.set_style('whitegrid')

fig = sns.countplot(x = 'Embarked', hue = 'Pclass', data = df)
fig.set_title('Miejsce wejścia na \n pokład vs. klasa',fontsize = 40)
fig.set_xlabel('Miejsce wejścia na pokład', fontsize = 32)
fig.set_ylabel('Ilość pasażerów', fontsize = 32)

fig.legend(['Klasa 1', 'Klasa 2', 'Klasa 3'], fontsize = 20, frameon = True, \
            edgecolor = 'black')

plt.tight_layout()
plt.savefig(figure = fig, fname = 'plots/1AD1.png')
plt.close()

# 2. Stripplot obrazujący korelację między ceną a klasą
sns.set(font_scale=2.5,palette = 'deep',rc={'figure.figsize':(10,10)})
sns.set_style('whitegrid')

fig = sns.stripplot(x = 'Pclass', y = 'Fare', data = df, jitter = 1)
fig.set_title('Rozkład cen biletów\n w zależności od klasy',fontsize = 40)
fig.set_xlabel('Klasa', fontsize = 32)
fig.set_ylabel('Cena biletu w funtach', fontsize = 32)
fig.set_ylim([0,270])

plt.tight_layout()
plt.savefig(figure = fig, fname = 'plots/1AD2.png')
plt.close()

# 3. Histogram ilości osób dla wszystkich przedziałów wiekowych
sns.set(font_scale=2.5,palette = 'deep',rc={'figure.figsize':(10,10)})
sns.set_style('ticks')

fig = sns.distplot(df['Age'], kde = False, bins = np.linspace(0,80,80), \
                   hist_kws=dict(edgecolor="k", linewidth=1))
plt.xticks(np.arange(0, 81, 10))
plt.yticks(np.arange(0,49, 4))
fig.set_title('Rozkład wieku',fontsize = 40)
fig.set_xlabel('Wiek', fontsize = 32)
fig.set_ylabel('Ilość pasażerów', fontsize = 32)

plt.tight_layout()
plt.savefig(figure = fig, fname = 'plots/1AD3.png')
plt.close()

# 4. Histogram ilości osób dla wszystkich przedziałów wiekowych i nałożony
#    na niego histogram osób, które przeżyły
sns.set(font_scale=2.5,palette = 'deep',rc={'figure.figsize':(10,11)})
sns.set_style('ticks')

fig = sns.distplot(df['Age'], kde = False, bins = np.linspace(0,80,80), \
                   hist_kws=dict(edgecolor="k", linewidth=1))
fig = sns.distplot(df[df['Survived']==1]['Age'], color = 'red', kde = False, \
                   bins = np.linspace(0,80,80), \
                   hist_kws=dict(edgecolor="k", linewidth=1))
plt.xticks(np.arange(0, 81, 10))
plt.yticks(np.arange(0, 49, 4))
fig.set_title('Rozkład wieku wszystkich\n oraz ocalałych pasażerów', \
              fontsize = 40)
fig.set_xlabel('Wiek', fontsize = 32)
fig.set_ylabel('Ilość pasażerów', fontsize = 32)
plt.legend(['Wszyscy pasażerowie','Ocaleni pasażerowie'], fontsize = 20, \
            frameon = True, edgecolor = 'black')

plt.tight_layout()
plt.savefig(figure = fig, fname = 'plots/1AD4.png')
plt.close()

# 5. Histogram ilości mężczyzn dla wszystkich przedziałów wiekowych
#    i nałożony na niego histogram mężczyzn, którzy przeżyli
sns.set(font_scale=2.5, palette = 'deep', rc={'figure.figsize':(10,11)})
sns.set_style('ticks')

fig = sns.distplot(df[df['Sex']=='male']['Age'], kde = False, \
                   bins = np.linspace(0,80,80),
                   hist_kws=dict(edgecolor="k", linewidth=1))
fig = sns.distplot(df[(df['Sex']=='male') & (df['Survived']==1)]['Age'], \
                   color = 'red', kde = False, bins = np.linspace(0,80,80), \
                   hist_kws=dict(edgecolor="k", linewidth=1))
plt.xticks(np.arange(0, 81, 10))
plt.yticks(np.arange(0, 49, 4))
fig.set_title('Rozkład wieku wszystkich oraz \n ocalałych pasażerów - mężczyźni',\
              fontsize = 40)
fig.set_xlabel('Wiek', fontsize = 32)
fig.set_ylabel('Ilość pasażerów', fontsize = 32)
plt.legend(['Wszyscy pasażerowie','Ocaleni pasażerowie'], fontsize = 20, \
            frameon = True, edgecolor = 'black')

plt.tight_layout()
plt.savefig(figure = fig, fname = 'plots/1AD5.png')
plt.close()

# 6. Histogram ilości kobiet dla wszystkich przedziałów wiekowych i nałożony
#    na niego histogram kobiet, które przeżyły
sns.set(font_scale=2.5,palette = 'deep', rc={'figure.figsize':(10,11)})
sns.set_style('ticks')

fig = sns.distplot(df[df['Sex']=='female']['Age'], kde = False, \
                   bins = np.linspace(0,80,80), hist_kws=dict(edgecolor="k", \
                   linewidth=1))
fig = sns.distplot(df[(df['Sex']=='female') & (df['Survived']==1)]['Age'], \
                   color = 'red', kde = False, bins = np.linspace(0,80,80),
                   hist_kws = dict(edgecolor="k", linewidth=1))
plt.xticks(np.arange(0, 81, 10))
plt.yticks(np.arange(0, 49, 4))
fig.set_title('Rozkład wieku wszystkich oraz \n ocalałych pasażerów - kobiety',\
              fontsize = 40)
fig.set_xlabel('Wiek', fontsize = 32)
fig.set_ylabel('Ilość pasażerów', fontsize = 32)
plt.legend(['Wszyscy pasażerowie','Ocaleni pasażerowie'], fontsize = 20, \
            frameon = True, edgecolor = 'black')

plt.tight_layout()
plt.savefig(figure = fig, fname = 'plots/1AD6.png')
plt.close()

# 7. Procent tych, którzy przeżyli z podziałem na klasy i płeć
sns.set(font_scale=2.5,palette = 'deep', rc={'figure.figsize':(10,10)})
sns.set_style('whitegrid')

fig = sns.barplot(x='Sex', y='Survived', hue='Pclass', ci=None, data=df)
fig.set_title('Prawdopodobieństwo przeżycia \n vs. płeć i klasa',fontsize = 40)
fig.set_xlabel('Płeć', fontsize = 32)
fig.set_ylabel('Prawdopodobieństwo przeżycia', fontsize = 32)
fig.set_xticklabels(['Mężczyźni','Kobiety'])

fig.legend(['Klasa 1', 'Klasa 2', 'Klasa 3'], fontsize = 20, frameon = True, \
            edgecolor = 'black', loc = 0)

plt.tight_layout()
plt.savefig(figure = fig, fname = 'plots/1AD7.png')
plt.close()
