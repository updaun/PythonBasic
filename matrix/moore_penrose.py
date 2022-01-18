# Scikit Learn 을 활용한 회귀분석
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fix(X, y)
y_test = model.predict(x_test)

# Moore-Penrose 역행렬
# y절편을 직접 추가해야된다.
X_ = np.array([np.append(x, [1]) for x in X]) # intercept 항 추가
beta = np.linalg.pinv(X_) @ y
y_test = np.append(x, [1]) @ beta