import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='BIZ UDGothic')
ctv_list=list()
date_list=str()
df=pd.read_csv('tokyo_2021syazyounerai.csv', skiprows=[0,1676], encoding="shift_jis", names=["罪名","手口","管轄警察署（発生地）","管轄交番・駐在所（発生地）","市区町村コード（発生地）","都道府県（発生地）","市区町村（発生地）","町丁目（発生地）","発生年月日（始期）","発生時（始期）","発生場所","発生場所の詳細","施錠関係","現金被害の有無"])
ctv_list=df.loc[:,"市区町村（発生地）"]
date_list=pd.to_datetime(df.loc[:,"発生年月日（始期）"])
print(ctv_list.value_counts())
print(ctv_list.describe())
ctv_list.value_counts().plot(kind='bar')
plt.show()