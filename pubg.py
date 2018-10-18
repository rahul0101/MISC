import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy import stats

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option("display.max_columns", 10)

# Dataset available at kaggle.com/lazyjustin/pubgplayerstats
df = pd.read_csv("PUBG_Player_Statistics.csv")
#print(df.columns.values)
df = df.ix[0:1200,:]
df = df[['solo_KillDeathRatio','solo_TimeSurvived','solo_Rating','solo_DamageDealt','solo_RoundsPlayed','solo_HeadshotKills','solo_WinRatio']]
df['solo_TimeSurvived'] = df['solo_TimeSurvived']/df['solo_RoundsPlayed']
del df['solo_RoundsPlayed']
df = df.loc[(df!=0).any(1)]
df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]
df.loc[:,'solo_TimeSurvived'] = (df.loc[:,'solo_TimeSurvived']-df['solo_TimeSurvived'].mean())/df['solo_TimeSurvived'].std()
df.loc[:,'solo_KillDeathRatio'] = (df.loc[:,'solo_KillDeathRatio']-df['solo_KillDeathRatio'].mean())/df['solo_KillDeathRatio'].std()
df.loc[:,'solo_Rating'] = (df.loc[:,'solo_Rating']-df['solo_Rating'].mean())/df['solo_Rating'].std()
df.loc[:,'solo_DamageDealt'] = (df.loc[:,'solo_DamageDealt']-df['solo_DamageDealt'].mean())/df['solo_DamageDealt'].std()
#df.loc[:,'solo_WinRatio'] = (df.loc[:,'solo_WinRatio']-df['solo_WinRatio'].mean())/df['solo_WinRatio'].std()
df.loc[:,'solo_HeadshotKills'] = (df.loc[:,'solo_HeadshotKills']-df['solo_HeadshotKills'].mean())/df['solo_HeadshotKills'].std()


X = df[['solo_KillDeathRatio','solo_TimeSurvived','solo_Rating','solo_DamageDealt','solo_HeadshotKills']]
#del X['solo_TimeSurvived']
Y = df[['solo_WinRatio']]

X_train = X[:1000]
X_test = X[1000:]
Y_train = Y[:1000]
Y_test = Y[1000:]

reg = linear_model.LinearRegression()
reg.fit(X_train,Y_train)
pred = reg.predict(X_test)
print('Coefficients: \n', reg.coef_)
print("Mean squared error: %.2f"
      % mean_squared_error(Y_test, pred))
print('Variance score: %.2f' % r2_score(Y_test, pred))
'''
#plt.scatter(X_test, Y_test,  color='black')
#plt.scatter(X_test, Y_test,  color='red')
#plt.plot(X_test, pred, color='blue', linewidth=1)
#plt.plot(X_test['solo_TimeSurvived'], pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()'''
print(df.head())
