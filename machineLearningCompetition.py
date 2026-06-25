import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics

digits = datasets.load_digits()
_, axses = plt.subplots(nrows=2, ncols=2, figsize=(5, 5))
axses = axses.flatten()

 # 3. Pehle 4 handwritten digits ko plot karo
for ax, image, label in zip(axses, digits.images, digits.target):
     ax.set_axis_off()
     ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
     ax.set_title("Training: %i" % label)

plt.show()


# learn.metrics import mean_absolute_error
# from sklearn.model_selection import train_test_split
#
# import pandas as pd
#
# # Load the data using the correct absolute Windows path
# iowa_file_path = r"C:\Users\Dell Laptop\PycharmProjects\PythonProject\train.csv"
# home_data = pd.read_csv(iowa_file_path)
#
# # Separate the target
# y = home_data.SalePrice
#
# # Create X (After completing the exercise, you can return to modify this line!)
# features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
#
# # Select columns corresponding to features, and preview the data
# X = homimport pandas as pd
# from sklearn.ensemble import RandomForestRegressor
# from ske_data[features]
# X.head()

# Split into validation and training data
# train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
#
# # Define a random forest model
# rf_model = RandomForestRegressor(random_state=1)
# rf_model.fit(train_X, train_y)
# rf_val_predictions = rf_model.predict(val_X)
# rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)
#
# print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))