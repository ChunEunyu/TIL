def compress_string(s):
    _c = "" # 이전 문자를 저장하는 변수 
    cnt = 0  # 중복 카운트를 저장하는 변수
    result = "" # 결과문자열

    for c in s: # 중복 검사하기  
        if c!=_c:  # 현재 문자가 이전 문자와 다른 경우
            _c = c # 현재 문자를 이전 문자 변수에 대입
            if cnt: result += str(cnt) # 중복카운트된 수를 문자열로 변환하고 result 문자열에 추가
            result += c # 결과 문자열에 
            cnt = 1
        else: # 현재 문자가 이전 문자와 같은 경우
            cnt +=1 # 카운트 변수에 1 더하기
    if cnt: result += str(cnt) # 중복카운트된 수를 문자열로 변환하고 result 문자열에 추가
    return result

print(compress_string("aaabbcccccca"))  # a3b2c6a1 출력
