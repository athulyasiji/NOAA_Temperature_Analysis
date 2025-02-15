import matplotlib.pyplot as plt

def plot_temperature_trends(record_highs, record_lows):
    """ Plot record high and low temperatures from 2005-2014. """
    plt.figure(figsize=(12, 6))
    plt.plot(record_highs.index, record_highs.values, label="Record High (2005-2014)", color="red")
    plt.plot(record_lows.index, record_lows.values, label="Record Low (2005-2014)", color="blue")
    plt.fill_between(record_highs.index, record_highs.values, record_lows.values, color="gray", alpha=0.3)
    plt.xlabel("Day of Year")
    plt.ylabel("Temperature (°C)")
    plt.title("Record High and Low Temperatures (2005-2014)")
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()
