import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("train.csv")
sns.set_palette("pastel")
sns.pairplot(df)
plt.show()