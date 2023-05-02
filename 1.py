# 1) Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов,
# хоккеистов и штангистов.
#
# Даны значения роста в трех группах случайно выбранных спортсменов:
#
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
#
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
#
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
import numpy as np
import pandas as pd
from scipy import stats
football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifting = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
stats.f_oneway(football, hockey, weightlifting)
# F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698693)
# Получили значение pvalue = 0,01048
#  на уровне статистической значимости альфа = 0,05
#  отвергаем нулевую гипотезу. Т.е. средний рост футболистов, хоккеистов и штангистоа различен.
# При этом на уровне значимости альфа = 0,01
#  нулевую гипотезу отвергнуть не можем.