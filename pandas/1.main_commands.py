import pandas as pd


# one dimensional data structure
s = pd.Series([3, -5, 7, 4], index=["a", 56, "c", "sfjk"])
# print(s)


# 2 dimensional dataframe
data = {
    "Country": ["Belgium", "India", "Brazil"],
    "Capital": ["Brussels", "New Delhi", "Brasilia"],
    "Population": [11190846, 1303171035, 207847528]
}

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data, columns=["Country", "Capital", "Population"])

# Dropping

dropped_s = s.drop([56, "c"])
# print(dropped_s)


dropped_df = df1.drop("Country", axis=1)
# print(dropped_df)

# print(df2.sort_index(ascending=False))
# print(df2.sort_values("Population", ascending=False))

# print(df1.rank())
#    Country  Capital  Population
# 0      1.0      2.0         1.0
# 1      3.0      3.0         3.0
# 2      2.0      1.0         2.0


# Get one element
# print(s["c"])
# print(df1[1:])

# Setting
# print(s)
s["skfdf"] = 24
s[56] = 12345
# print(s)

# Basic information

# print(df1.shape)  # (3, 3)
# print(df1.index)  # RangeIndex(start=0, stop=3, step=1)
# print(df1.info())  #
# print(df1.count())  #
# Country       3
# Capital       3
# Population    3
# dtype: int64

# Summary

# print(df1.sum())
# Country              BelgiumIndiaBrazil
# Capital       BrusselsNew DelhiBrasilia
# Population                   1522209409
# dtype: object

# print(df1.cumsum())
# print(df1.max())
# print(df1.describe())
# print(df1.mean())
# print(df1.median())

# applying functions:
# print(df2.apply(lambda x: x * 2))
# print(df2.applymap(lambda x: x * 2))

s2 = pd.Series([345, 12, 11, 98], index=["a", "c", 56, 'skfsdfkj'])
# print(s + s2)
# print(s2.add(s, fill_values=0)) # not working

print(df1.sample(1))






