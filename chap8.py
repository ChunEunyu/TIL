def chkDupNum(s):
    result = []
    for num in s: 
        if num not in result:   # result 리스트에 없는 수
            result.append(num)  # result 리스트에 추가
        else:                   # result 리스트에 있는 수
            return False        # False
    return len(result) == 10    # result 요소 개수가 10개면 True

print(chkDupNum("0123456789"))      # True 리턴
print(chkDupNum("01234"))           # False 리턴
print(chkDupNum("01234567890"))     # False 리턴
print(chkDupNum("6789012345"))      # True 리턴
print(chkDupNum("012322456789"))    # False 리턴
