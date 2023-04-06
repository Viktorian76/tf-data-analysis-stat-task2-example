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
    sigma_h = np.sqrt(np.sum(x**2) / (31 * size_x))
    
    left = sigma_h / np.sqrt(chi2.ppf(1 - alpha/2, df=size_x))
    right = sigma_h / np.sqrt(chi2.ppf(alpha/2, df=size_x))
    
    return (left, right)
