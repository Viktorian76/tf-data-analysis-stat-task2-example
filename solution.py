import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 344589832 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    #loc = x.mean()
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    
    size_x = len(x)
    
    left = np.sqrt(size_x * (x ** 2).mean() / (31 * chi2.ppf(q = 1 - alpha / 2, df= 2 * size_x)))
    right = np.sqrt(size_x * (x ** 2).mean() / (31 * chi2.ppf(q = alpha / 2, df= 2 * size_x)))   
    return (left, right)
