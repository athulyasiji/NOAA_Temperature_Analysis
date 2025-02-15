import pandas as pd

def load_and_clean_data(filename):
    """ Load data, convert dates, remove leap days. """
    df = pd.read_csv(filename)
    df["date"] = pd.to_datetime(df["date"])
    df = df[~((df["date"].dt.month == 2) & (df["date"].dt.day == 29))]  # Remove Feb 29
    df["year"] = df["date"].dt.year
    df["day_of_year"] = df["date"].dt.strftime("%m-%d")
    return df

if __name__ == "__main__":
    df = load_and_clean_data("datasets/temperature.csv")
    print(df.head())
