import numpy as np
import pandas as pd
df = pd.read_csv('C:\\Users\\buleb\\Downloads\\Wonju_Populatoin_Rate.csv',encoding='euc-kr')
x = np.arange(21)
arr = np.array(df['반곡관설동 총인구수 (명)'])
y =  np.array(df['나이'])
print(arr)

mean = np.mean(arr)
print(mean)

sorted_midarr = np.sort(arr)
mid = np.median(sorted_midarr)
print (mid)

def skewness(input):
    # 길이
    len_inp = len(input)
    result = 0
    for i in input:
        result += ((i - np.mean(input)) / np.std(input)) ** 3
    result = result / len_inp
    return result

def kurtosis(input):
    # 길이
    len_inp = len(input)
    result = 0
    for i in input:
        result += ((i - np.mean(input)) / np.std(input)) ** 4
    result = (result / len_inp) - 3
    return result

print(skewness(arr))
print(kurtosis(arr))

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
 
fm.get_fontconfig_fonts()
plt.rc('font', family='Malgun Gothic')

# 계급수를 10으로 하여 히스토그램을 그림
plt.bar(x,arr,width=1, edgecolor="black")
plt.xticks(x, y,rotation=45)
plt.title('반곡 관설동 총인구수', fontsize=20)
plt.xlabel('나이',fontsize=18)
plt.ylabel('인구 수',fontsize=18)
plt.show()
