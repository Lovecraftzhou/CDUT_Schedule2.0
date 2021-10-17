import numpy as np
import pandas as pd
from IPython.display import display


#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)

# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)
# pd.set_option('display.width', 180)    # 设置打印宽度(**重要**)

def DealData(data):
    # print(data)
    df = pd.DataFrame(data)
    grouped = df.groupby(['name','days'])
    # df1 = grouped.get_group('teacher')
    # print(df1)

    all_data = []
    for key,value in grouped:
        # print(key)
        # print(value)
        Week_dict = {}
        all_week = ''

        for w in value['Week']:
            # print(w)
            all_week += str(w)
            all_week += ','

        ddd = "周{D}第{S}-{E}节".format(D=value.iloc[0,3],S=value.iloc[0,4],E=value.iloc[0,5])+'{'+"第{A}周".format(A=all_week)+'}'
        Week_dict['name'] = key[0]
        Week_dict['teacher'] = value.iloc[0,1]
        Week_dict['room'] =value.iloc[0,2]
        Week_dict['days'] =value.iloc[0,3]
        Week_dict['nums'] =value.iloc[0,4]
        Week_dict['enum'] =value.iloc[0,5]
        Week_dict['attend'] = all_week
        Week_dict['ddd'] = ddd
        all_data.append(Week_dict)
    # display(df)

    # print(all_data)
    return all_data