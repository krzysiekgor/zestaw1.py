import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyp
#https://htmlcolorcodes.com/

#zad1
# pyp.figure(figsize=(9,6))
# pyp.bar(0,140,color='#ffffff',width=0.8)
# pyp.bar(0,100,color='#349263',width=0.8)
# pyp.bar(0,20,color='#4E1864',width=0.8)
# pyp.bar(1,70,color='#18644C',width=0.8)
# pyp.bar(1,10,color='#58D5C6',width=0.8)
# pyp.bar(2,75,color='#B5BD51',width=0.8)
# pyp.bar(2,30,color='#A49A04',width=0.8)
# pyp.bar(3,25,color='#F3AFAF',width=0.8)
# pyp.bar(3,10,color='#4885FE',width=0.8)
# pyp.bar(4,50,color='#5AFF01',width=0.8)
# pyp.bar(5,0)
# pyp.plot(np.arange(0,6,1),[120,120,120,120,120,120],color='green')
# pyp.title('Tytul')
# plt.savefig('1.pdf')
#pyp.show()

# #zad2
# xlsx = pd.ExcelFile('mieszkania1.xlsx')
# df = pd.read_excel(xlsx,header=0)
# f = plt.figure()
# ax = f.add_subplot(111)
# plt.text(-0.1,-0.12,'136019',horizontalalignment='center',
#      verticalalignment='center', transform = ax.transAxes)
# pyp.bar(df['Rok']-0.2,df['Wartość'].where(df['Formy budownictwa']=='indywidualne'),width=0.2)
# pyp.bar(df['Rok'],df['Wartość'].where(df['Formy budownictwa']=='spółdzielcze'),width=0.2)
# pyp.bar(df['Rok']+0.2,df['Wartość'].where(df['Formy budownictwa']=='komunalne'),width=0.2)
# plt.savefig('zad2.pdf')
# pyp.show()

#zad3
xlsx = pd.ExcelFile('turystyka1.xlsx')
df = pd.read_excel(xlsx,header=0)
print(df.iterrows())
df = df.stack(level=0)

df.index = df.index.rename('Kategoria',level=1)
df.index = df.index.rename('level',level=0)
# df.index = df.index.rename('wartosc',level=2)
df.name='wartosc'
df = df.reset_index()
c= df.where(df['level']==0).dropna()
d= df.where(df['level']==1).dropna()
df = pd.merge(c,d,on='Kategoria')
df = df.drop(['level_x','level_y'],axis=1)
df = df.rename(columns={'wartosc_x':'Rok','wartosc_y':'Ilość'})

print(c)
print(d)

print(df)
