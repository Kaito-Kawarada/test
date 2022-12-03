import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn import model_selection, preprocessing, linear_model, svm
import sklearn
sklearn.__version__

tokyo_temprature_dataframe = pd.read_csv( 
    "tokyo_1900-2019.csv", encoding='Shift-JIS', 
    names=("date", "ave", "ave1", "ave2", "highest", "highest1", "highest2", "lowest", "lowest1", "lowest2"), 
    usecols=lambda x: x not in ["ave1", "ave2", "highest1", "highest2", "lowest1", "lowest2"], 
    skiprows=6, index_col=['date'], parse_dates=True)

#print(tokyo_temprature_dataframe)
#print(tokyo_temprature_dataframe.dtypes)

tokyo_temprature_dataframe_after = tokyo_temprature_dataframe.set_index(
    [tokyo_temprature_dataframe.index.month, tokyo_temprature_dataframe.index.year, tokyo_temprature_dataframe.index])
tokyo_temprature_dataframe_after.index.names = ['month', 'year', 'date']

#print(tokyo_temprature_dataframe_after)
#print(tokyo_temprature_dataframe_after.columns)

tokyo_temprature_dataframe_new = tokyo_temprature_dataframe_after.reset_index()
print(tokyo_temprature_dataframe_new.dtypes)
month_i = 1
#while month_i <= 12:
#    month_i += 1
#    tokyo_temprature_dataframe_new[tokyo_temprature_dataframe_new["month"] == month_i].plot(x='year', y='ave')
#    tokyo_temprature_dataframe_new[tokyo_temprature_dataframe_new["month"] == month_i].plot(x='year', y='highest')
#    tokyo_temprature_dataframe_new[tokyo_temprature_dataframe_new["month"] == month_i].plot(x='year', y='lowest')
#    plt.show()

for month_i in range(1, 13):
    df = tokyo_temprature_dataframe_new[tokyo_temprature_dataframe_new["month"] == month_i]
    x = df['year']
    y = df['ave']
    z = df['highest']
    w = df['lowest']
    clf_y = svm.SVR(kernel='rbf', gamma='auto', epsilon=2.0)
    clf_z = svm.SVR(kernel='rbf', gamma='auto', epsilon=2.0)
    clf_w = svm.SVR(kernel='rbf', gamma='auto', epsilon=2.0)
    x = np.array(x).reshape(-1, 1)
    clf_y.fit(x, y)
    clf_z.fit(x, z)
    clf_w.fit(x, w)
    x_reg = np.arange(1900, 2020, 1)
    x_reg = np.array(x_reg).reshape(-1, 1)
    line_Y_clf_y = clf_y.predict(x_reg)
    line_Y_clf_z = clf_z.predict(x_reg)
    line_Y_clf_w = clf_w.predict(x_reg)
    plt.scatter(x, y, c='g', marker='s')
    plt.scatter(x, z, c='r', marker='s')
    plt.scatter(x, w, c='b', marker='s')
    plt.plot(x, line_Y_clf_y, c='g')
    plt.plot(x, line_Y_clf_z, c='r')
    plt.plot(x, line_Y_clf_w, c='b')
    plt.show()
    y_pred = clf_y.predict([[2050]])
    z_pred = clf_z.predict([[2050]])
    w_pred = clf_w.predict([[2050]])
    y_score = clf_y.score(x_reg, y)
    z_score = clf_z.score(x_reg, z)
    w_score = clf_w.score(x_reg, w)
    print('month:', month_i)
    print('ave:', y_pred)
    print('CD of ave:', y_score)
    print('highest:', z_pred)
    print('CD of highest:', z_score)
    print('lowest', w_pred)
    print('CD of lowest:', w_score)
print('These are predictions of 2050')