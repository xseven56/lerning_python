# import pandas as pd
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
#
# # Используя get_dummies
# print(data)
# print(pd.get_dummies(data))
#
# # Не используя get_dummies
# unique_values = data['whoAmI'].unique()
# one_hot = pd.DataFrame()
# for value in unique_values:
#     one_hot[f'whoAmI_{value}'] = (data['whoAmI'] == value).astype(int)
# print(one_hot)

