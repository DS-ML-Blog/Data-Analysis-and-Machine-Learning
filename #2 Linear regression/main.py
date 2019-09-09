from preparation import preparation
from plotHistograms import plotHistograms
from paramPhase import paramPhase
from predictions import predictions
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
import numpy as np
import seaborn as sns

plt.style.use('classic')

# 1. Przygotowanie danych da wizualizacji i dalszej analizy
df = preparation()

# 2. Histogramy z poszczególnymi parametrami pogodowymi dla wszystkich lat
params = ['Temperature', 'ApparentTemperature', 'Humidity', 'Pressure']
for counter, param in enumerate(params):
    figure = plotHistograms(df, param);
    plt.savefig(Figure = figure, fname = 'plots/2AD'+str(counter+1)+'.png')
    plt.close('all')

# 3. Korelacja między poszczególnymi zmiennymi numerycznymi
dfnum = df.select_dtypes([float])
labels = list(dfnum.columns)
labels[1] = 'App.Temp.'

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)
sns.heatmap(dfnum.corr(), cmap = 'PuOr', cbar_kws={'shrink': 0.8}, \
            square = True)
plt.title('Współczynniki korelacji', fontsize = 28)
ax.xaxis.set_ticks_position('bottom')
ax.set_xticklabels(labels, {'fontsize': 16})
ax.set_yticklabels(labels, {'fontsize': 16})
plt.xticks(rotation=60)
plt.subplots_adjust(left = 0.18, bottom = 0.05, right = 0.99, top = 0.99, \
                    wspace = 0.45, hspace = 0.45)
plt.savefig(Figure = fig, fname = 'plots/2AD5.png')


# 4. Wykres temperatury (uśrednionej po latach) od pory dnia dla poszczególnych
#    pór roku
paramPhase( df[['Temperature', 'YearPhase', 'DayPhase']], 'Temperatura',6)
paramPhase( df[['Pressure', 'YearPhase', 'DayPhase']], 'Ciśnienie',7)
paramPhase( df[['Humidity', 'YearPhase', 'DayPhase']], 'Wilgotność',8)
plt.close('all')

# 5. Regresja liniowa
# a) przewidywania temperatury
X = dfnum.drop(['ApparentTemperature','Temperature'], axis = 1)
y = dfnum['Temperature']

y_pred, y_test = predictions(X, y, tytul = 'temperatura', nr = 9)
print('Średni błąd (MAE): '+str(metrics.mean_absolute_error(y_pred, y_test)))
print('Średni błąd względny (MPAE): ' + \
        str(metrics.mean_absolute_error(y_pred, y_test) / y_test.mean()))

# b) Przewidywania temperatury odczuwalnej
X = dfnum.drop(['ApparentTemperature','Temperature'], axis = 1)
y = dfnum['ApparentTemperature']

y_pred, y_test = predictions(X, y, 'temperatura odczuwalna', nr = 10)
print('Średni błąd (MAE): '+str(metrics.mean_absolute_error(y_pred, y_test)))
print('Średni błąd względny (MPAE): ' + \
        str(metrics.mean_absolute_error(y_pred, y_test) / y_test.mean()))

# c) Przeidywania temperatury na podstawie samej wilgotności
X = dfnum[['Humidity']]
y = dfnum['Temperature']

y_pred, y_test = predictions(X, y, 'temperatura', nr = 11)
print('Średni błąd (MAE): ' + str(metrics.mean_absolute_error(y_pred, y_test)))
print('Średni błąd względny (MPAE): ' + \
        str(metrics.mean_absolute_error(y_pred, y_test) / y_test.mean()))
