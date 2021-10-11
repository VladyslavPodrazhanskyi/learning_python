import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.dummy import DummyRegressor





# df['price_value'] = df['price_value'].str.replace(" ", "").str.replace(",", ".").astype(float)
# df.sample(10)

# np.percentile(df['price_value'], 99.9)

# df[ df["price_value"] > 10000000 ]["price_value"]

"""
Очень простая модель
Давай сразу сделаем "ручную" версию модели, 
чтобы было более понятно. 
Для этого находим среднее значение 
и всегда возвращаем его для нашего "прогноза". 
Вот так просто.
Наш прогноз записываем в столбце price_pred.
"""


# price_mean = df["price_value"].mean()
# df["price_pred"] = price_mean
# price_mean

"""
Теперь давай считать ошибку. У нас есть правильный ответ (в price_value) и то, 
что мы спрогнозировали (в price_pred). 
Теперь, вычитая одно из другого - получаем разницу (ошибку).
Затем "обрезаем знак" и находим среднее значение ошибки.
"""

# df["price_diff"] = df["price_pred"] - df["price_value"]
# df["price_diff"].abs().mean()


'''если возвращать не среднее значение, а медиану'''
# df["price_pred"] = df["price_value"].median()
# mean_absolute_error(df["price_value"], df["price_pred"])







