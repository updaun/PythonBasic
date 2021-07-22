from googletrans import Translator

# print(Translator) # <class 'googletrans.client.Translator'>

# How to install Googletrans
# pip install googletrans==3.1.0a0
# 다른 버전에서 에러 발생

# 번역기 객체 생성
translator = Translator()

# test sentence
# sentence = "안녕하세요. 반갑습니다."
sentence = input("번역할 문장을 입력해 주세요 : ")

# 언어 감지 문장 설정
detected = translator.detect(sentence)
# print(detected) # Detected(lang=ko, confidence=1)
# print(detected.lang) # ko

# 번역
result = translator.translate(sentence, 'en')

print("===========출 력 결 과===========\n")
print(detected.lang,":",sentence)
print(result.dest,":",result.text, "\n")
print("=================================")
