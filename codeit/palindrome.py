def is_palindrome(word):
    palindrome = list(word)
    # 문자열을 반대로 뒤집는 과정에 주의한다.
    if palindrome == list(reversed(palindrome)):
        result = True
    else:
        result = False
    return result

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))