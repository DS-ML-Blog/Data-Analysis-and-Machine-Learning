def preparation():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    from plotHistograms import plotHistograms
    import matplotlib.pyplot as plt

    df = pd.read_csv('dane/weatherHistory.csv')
    df.rename(columns={'Formatted Date': 'Date', 'Precip Type': 'Precip', \
                'Wind Speed (km/h)':'WindSpeed', 'Loud Cover':'Cloud Cover', \
                'Wind Bearing (degrees)': 'WindBearing', \
                'Pressure (millibars)':'Pressure', \
                'Temperature (C)': 'Temperature', \
                'Apparent Temperature (C)':'ApparentTemperature',\
                'Visibility (km)': 'Visibility'},index=str,  inplace = True)

    # Ta kolumna zawiera same zera
    df.drop(['Cloud Cover'], axis = 1, inplace = True)

    # Usuwa outliery
    df = df[df['Pressure']>100]
    df = df[df['Humidity']>0.05]

    # Zmienne kategoryczne, ale ilość kategorii jest zbyt duża do analizy
    df.drop(['Summary'], axis=1, inplace = True)
    df.drop(['Daily Summary'], axis=1, inplace = True)

    # Zamienia NaNy na unknown
    df['Precip'].replace(np.nan,'unknown', inplace = True)

    # Zamienia datę i godzinę w postaci stringa na poszczególne części do floatów
    df['Year']  = pd.Series(df['Date'].str.slice(0,4))
    df['Month'] = pd.Series(df['Date'].str.slice(5,7),   dtype = 'float32')
    df['Day']   = pd.Series(df['Date'].str.slice(8,10),  dtype = 'float32')
    df['Hour']  = pd.Series(df['Date'].str.slice(11,13), dtype = 'float32')
    # ... po czym zamienia je na 'fazę' z zakresu [0, 2pi]...
    df['YearPhase'] = ((df['Month']-1)*30 + df['Day'])*2*np.pi/361
    df['DayPhase'] = df['Hour']/24*2*np.pi
    # ...i dodaje indeks wyższej hierarchii (rok)...
    df.set_index(['Year'], inplace = True)
    # ...po czym usuwa niepotrzebne kolumny
    df.drop(['Date', 'Month', 'Day', 'Hour'], axis = 1, inplace = True)


    return df
