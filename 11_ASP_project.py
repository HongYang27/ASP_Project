import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class EvaluateMark:
    def total(marklist):
        return sum(marklist)

datas = pd.read_excel('dataNew.xls')
print(datas)

print(datas.columns)

print(datas.head(5))
data = datas['Period'].str.split(' ', n=1, expand=True)
datas["Month"] = data[0]
datas["Year"] = data[1]
datas.index = datas['Year']
del datas['Period']
print(data)
print(datas)
print(datas.dtypes)
datas["Year"] = pd.to_numeric(datas["Year"])
print(datas.dtypes)

df3 = datas[(datas['Year'] >= 1900) & (datas['Year'] <= 1910)]
print(df3)

ps = df3['Calories'].sort_values(ascending=False)
print(ps)

total = ps.sum()
print(total)

mean = ps.mean()
print(mean)

index = np.arange(len(ps.index))
print(index)
plt.xlabel('Year', fontsize=10)
plt.ylabel('Calories', fontsize=10)
plt.xticks(index, ps.index, fontsize=10, rotation=90)
plt.title('1900-1910')
plt.bar(ps.index, ps.values)
plt.show();


