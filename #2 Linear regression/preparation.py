import numpy as np
import pandas as pd


def preparation():
    df = pd.read_csv("data/weatherHistory.csv")
    df.rename(columns={"Formatted Date": "Date", "Precip Type": "Precip",
                       "Wind Speed (km/h)": "WindSpeed",
                       "Loud Cover": "Cloud Cover",
                       "Wind Bearing (degrees)": "WindBearing",
                       "Pressure (millibars)": "Pressure",
                       "Temperature (C)": "Temperature",
                       "Apparent Temperature (C)": "ApparentTemperature",
                       "Visibility (km)": "Visibility"}, index=str,
              inplace=True)

    df.drop(["Cloud Cover"], axis=1, inplace=True)

    df = df[df["Pressure"] > 100]
    df = df[df["Humidity"] > 0.05]

    df.drop(["Summary"], axis=1, inplace=True)
    df.drop(["Daily Summary"], axis=1, inplace=True)

    df["Precip"].replace(np.nan, "unknown", inplace=True)

    df["Year"] = pd.Series(df["Date"].str.slice(0, 4))
    df["Month"] = pd.Series(df["Date"].str.slice(5, 7),   dtype="float32")
    df["Day"] = pd.Series(df["Date"].str.slice(8, 10),  dtype="float32")
    df["Hour"] = pd.Series(df["Date"].str.slice(11, 13), dtype="float32")

    df["YearPhase"] = ((df["Month"]-1)*30 + df["Day"])*2*np.pi/361
    df["DayPhase"] = df["Hour"]/24*2*np.pi

    df.set_index(["Year"], inplace=True)

    df.drop(["Date", "Month", "Day", "Hour"], axis=1, inplace=True)

    return df
