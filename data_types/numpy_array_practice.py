import numpy as np

week_array = np.array([
    ['Mоn', 18, 20, 22, 17],
    ['Tuе', 11, 18, 21, 18],
    ['Wеd', 15, 21, 20, 19],
    ['Thu', 11, 20, 22, 21],
    ['Fri', 18, 17, 23, 22],
    ['Sаt', 12, 22, 20, 18],
    ['Sun', 13, 15, 19, 16]
])

print(type(week_array))
print(week_array)

m = np.reshape(week_array, (7, 5))

print('m_r')
m_r = np.append(week_array, [['Аvg', 12, 15, 13, 11]], 0)

print(m_r)


