import pandas as pd
df = pd.read_csv('diabetes.csv')

# get glucose series
dfGlucose = df['Glucose']
# calculate the mean of the series
dfGlucoseMean = df['Glucose'].mean()
# plot the series and the mean in the same graph
dfGlucose.plot()
plt.axhline(y=dfGlucoseMean, color='r', linestyle='-')
plt.suptitle('Glucose graph and mean')
plt.show()