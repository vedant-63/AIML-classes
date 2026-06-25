import matplotlib.pyplot as plt

quality_counts = df['quality'].value_counts()

plt.figure(figsize=(8,6))
plt.bar(quality_counts.index,quality_counts,color='deeppink')
plt.title('count plot of quality')
plt.xlabel('quality')
plt.ylabel('count')
plt.show()