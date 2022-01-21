import numpy as np

def l1_norm(x):
	x_norm = np.abs(x)
	x_norm = np.sum(x_norm)
	return x_norm

def l2_norm(x):
	x_norm = x * x
	x_norm = np.sum(x_norm)
	x_norm = np.sqrt(x_norm)
	return x_norm

# test_vector = np.array([-1, 2, -3])
test_vector = np.array([-6,-8])

l1_value = l1_norm(test_vector)
l2_value = l2_norm(test_vector)
numpy_l2_value = np.linalg.norm(test_vector)
print("test_vector :", test_vector)
print("l1_value :",l1_value,"\nl2_value :", l2_value)
print("numpy_l2_value :",numpy_l2_value)

# Vector 사이의 거리
x = np.array([-3, 0])
y = np.array([0, 4])

diff = y-x
l1_value = l1_norm(diff)
l2_value = l2_norm(diff)
print("diff :", diff)
print("l1_value :",l1_value,"\nl2_value :", l2_value)

# Vector 사이의 각도
# l2-norm 에서만 가능하다.
def vector_angle(x, y):
    # 제2 코사인 법칙 사용
    # np.inner(내적) : 내적은 정사영된 벡터의 길이와 관련 있다. 
    # (정사형 벡터)proj = x * cos(theta)  ,  <x,y> = x*y*cos(theta)
    # 내적은 두 벡터의 유사도( similarity )를 측정하는데 사용
    v = np.inner(x, y) / (l2_norm(x)*l2_norm(y))
    theta = np.arccos(v)
    return theta

x = np.array([0, 1])
y = np.array([0, 2])
print("angle :", vector_angle(x,y))

x = np.array([1, -1, 1, -1])
y = np.array([4, -4, 4, -4])
print ("inner :", np.inner(x,y))