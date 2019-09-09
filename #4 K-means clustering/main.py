import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from scipy.spatial.distance import cdist

#1. Przykład
data = make_blobs(n_samples = 200, n_features = 2, centers = 3, \
                  cluster_std = 1.8, random_state = 101)

fig = plt.figure(figsize = (9,9))
ax = fig.add_subplot(111)
plt.scatter(data[0][:,0], data[0][:,1])
plt.xlabel('Zmienna 1', fontsize = 22)
plt.ylabel('Zmienna 2', fontsize = 22)
plt.title('Sztucznie wygenerowane dane\nna potrzeby klasteryzacji', \
           fontsize = 24)
ax.tick_params(axis='both', which='major', labelsize=20)
plt.subplots_adjust(left = 0.2, bottom = 0.1, right = 0.9, top = 0.9)
plt.savefig(fname = 'plots/4AD1.png')


fig = plt.figure(figsize = (9,9))
ax = fig.add_subplot(111)
plt.scatter(data[0][:,0], data[0][:,1], c = data[1], cmap = 'rainbow')
plt.xlabel('Zmienna 1', fontsize = 22)
plt.ylabel('Zmienna 2', fontsize = 22)
plt.title('Sztucznie wygenerowane dane \nz podziałem na kategorie', \
            fontsize = 24)
ax.tick_params(axis='both', which='major', labelsize=20)
plt.subplots_adjust(left = 0.2, bottom = 0.1, right = 0.9, top = 0.9)
plt.savefig(fname = 'plots/4AD2.png')


kmeans = KMeans(n_clusters = 3)
kmeans.fit(data[0])

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (14,9))
ax1.set_title('Rzeczywiste kategorie', fontsize = 20)
ax1.scatter(data[0][:,0], data[0][:,1], c = data[1], cmap = 'rainbow')
ax2.set_title('Kategorie według K Means', fontsize = 20)
ax2.scatter(data[0][:,0], data[0][:,1], c = kmeans.labels_, cmap = 'rainbow')
ax1.tick_params(axis='both', which='major', labelsize=20)
ax2.tick_params(axis='both', which='major', labelsize=20)
plt.subplots_adjust(left = 0.1, bottom = 0.1, right = 0.9, top = 0.9)
plt.savefig(fname = 'plots/4AD3.png')


# 2. Starbucksy
df = pd.read_csv('data.csv')
df = df[['Longitude','Latitude', 'Country']]
df = df.dropna()

# a) Wykres bez klastrowania
fig = plt.figure(figsize = (16,8))
ax = fig.add_subplot(111)
plt.scatter(df['Longitude'], df['Latitude'], s = 0.1)
plt.title('Rozkład kawiarni Starbucksa na świecie według danych z kaggle.com', \
            fontsize = 24)
ax.tick_params(axis='both', which='major', labelsize=20)
plt.subplots_adjust(left = 0.05, bottom = 0.1, right = 0.95, top = 0.9)
plt.savefig(fname = 'plots/4AD4.png')

# b) podział na 6 klastrów
kmeans = KMeans(n_clusters = 6)
kmeans.fit(pd.DataFrame.as_matrix(df[['Longitude','Latitude']]))

fig = plt.figure(figsize = (16,8))
ax = fig.add_subplot(111)
plt.scatter(df['Longitude'], df['Latitude'], c = kmeans.labels_,s = 0.1, \
            cmap = 'rainbow')
plt.title('Podział kawiarni na sześć klastrów', fontsize = 24)
ax.tick_params(axis='both', which='major', labelsize=20)
plt.subplots_adjust(left = 0.05, bottom = 0.1, right = 0.95, top = 0.9)
plt.savefig(fname = 'plots/4AD5.png')

# c) podział na kolejno 6,5,4,3 klastry
fig = plt.subplots(2,2,figsize = (12,8))
plt.suptitle('Podział kawiarni na różną liczbę klastrów', fontsize = 20)
axes = []
for i,n_cluster in enumerate([6,5,4,3]):
    kmeans = KMeans(n_clusters = n_cluster)
    kmeans.fit(pd.DataFrame.as_matrix(df[['Longitude','Latitude']]))

    axes.append(plt.subplot(2,2,i+1))
    plt.scatter(df['Longitude'], df['Latitude'], c = kmeans.labels_,s = 0.1, \
                cmap = 'rainbow')
    axes[i].set_xlabel(['a) 6','b) 5','c) 4','d) 3'][i], fontdict = {'size': 17})

plt.subplots_adjust(left = 0.05, bottom = 0.1, right = 0.95, top = 0.9, \
                    hspace = 0.25)
plt.savefig(fname = 'plots/4AD6.png')
plt.close('all')

# 3.Zasada działania

x = [1, 1.5, 2.5, 3, 5, 5.3, 6]
y = [3, 2.9, 3.5, 3.1, 4.2, 3.5, 4]
init_kat = [1,2,2,1,1,2,1]

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3,2, figsize = (7,9))
plt.suptitle('Zasada działania algorytmu K Means Clustering', fontsize = 20)

ax1.scatter(x, y)
ax1.set_xlabel('a)', fontdict = {'size':12})
ax1.set_xlim([0, 7])
ax1.set_ylim([2, 4.7])

ax2.scatter(x, y, c = init_kat)
ax2.set_xlabel('b)', fontdict = {'size':12})
ax2.set_xlim([0, 7])
ax2.set_ylim([2, 4.7])

ax3.scatter(x, y, c = init_kat)
ax3.set_xlabel('c)', fontdict = {'size':12})
ax3.scatter([ np.mean([i for c,i in enumerate(x) if init_kat[c]==1]), \
    np.mean([i for c,i in enumerate(x) if init_kat[c]==2])], \
    [np.mean([i for c,i in enumerate(y) if init_kat[c]==1]), \
    np.mean([i for c,i in enumerate(y) if init_kat[c]==2])], marker = '^', \
            c = [1,2])
ax3.set_xlim([0, 7])
ax3.set_ylim([2, 4.7])

ax4.scatter(x,y, c = [2,2,2,2,1,1,1])
ax4.set_xlabel('d)', fontdict = {'size':12})
ax4.set_xlim([0, 7])
ax4.set_ylim([2, 4.7])

ax5.scatter(x,y, c = [2,2,2,2,1,1,1])
ax5.set_xlabel('e)', fontdict = {'size':12})
ax5.scatter([ np.mean(x[:4]), np.mean(x[4:]) ], \
             [np.mean(y[:4]), np.mean(y[4:])], marker = '^', c = [2,1])
ax5.set_xlim([0, 7])
ax5.set_ylim([2, 4.7])

ax6.scatter(x,y, c = [2,2,2,2,1,1,1])
ax6.set_xlabel('f)', fontdict = {'size':12})
ax6.set_xlim([0, 7])
ax6.set_ylim([2, 4.7])

plt.subplots_adjust(left = 0.1, bottom = 0.07, right = 0.95, top = 0.9, \
                    hspace = 0.25, wspace = 0.2)
plt.savefig(fname = 'plots/4AD7.png')
plt.close()

# 4. Elbow method
data = make_blobs(n_samples = 200, n_features = 2, centers = 5, \
                  cluster_std = 1.2, random_state = 100)
error = []

for K in range(3,12):
    kmeans = KMeans(n_clusters = K)
    kmeans.fit(data[0])
    error.append(sum(np.min(cdist(data[0],kmeans.cluster_centers_,'euclidean'), \
                 axis=1)) / data[0].shape[0])

fig = plt.figure(figsize = (8,8))
plt.scatter(data[0][:,0],data[0][:,1])
plt.title('Sztucznie wygenerowane dane', fontsize = 20)
plt.savefig(fname = 'plots/4AD8.png')

fig, ax = plt.subplots(1,1,figsize = (8,8))
plt.plot(range(3,12),error)
plt.xlabel('K', fontsize = 16)
plt.ylabel('Sum of squared errors', fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.title('Zależność SSE od K', fontsize = 20)

plt.savefig(fname = 'plots/4AD9.png')

plt.close('all')

#
