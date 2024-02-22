import numpy as np
from sklearn.metrics import mean_squared_error, r2_score


def cosine_similarity(A, B):
    dot_product = np.dot(A, B)
    norm_a = np.linalg.norm(A)
    norm_b = np.linalg.norm(B)
    return dot_product / (norm_a * norm_b)


# 假设A和B是两条曲线的y值，x是共同的x轴
A = np.array([1, 2, 3, 4, 5])
B = np.array([1, 2, 3, 4, 5])

# 计算相关系数
correlation_coefficient = np.corrcoef(A, B)[0, 1]

# 计算MSE
mse = mean_squared_error(A, B)

# 计算R^2
r_squared = r2_score(A, B)

# 计算余弦相似度
similarity = cosine_similarity(A, B)

# 输出结果
print(f"相关系数: {correlation_coefficient}\nMSE: {mse}\nR^2: {r_squared}\n余弦相似度: {similarity}")
