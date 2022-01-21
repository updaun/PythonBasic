# 예제 파일 이름을 pickle.py로 하면 AttributeError 발생 가능
import pickle

# pickle 은 파이썬에 특화된 binary_file이다

# pickle write binary
f = open("file_handing/log/list.pickle", "wb")
test = [1,2,3,4,5]
pickle.dump(test, f)
f.close()

# # pickle read binary
f = open("file_handing/log/list.pickle", "rb")
test_pickle = pickle.load(f)
print(test_pickle)
f.close()
