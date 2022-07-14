#문자열 word가 주어질 때, Dictionary를 활용해서
#  해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.


# word = input()

# dic = {}


# for i in word:
#     if dic.get(i) == None:
#         dic[i] = 1
#     else:
#         dic[i] += 1

# for i in dic:
#     print(i,dic[i])



word = 'banana'


result = {}
for char in word:
    #딕셔너리에 키가 없으면?
    if not char in result:  
        #키랑 값을 1로 초기화한다.
        result[char] = 1
    # 딕셔너리에 키가 있으면?
    else:
        result[char] = result[char]+1


print(result)


word = 'banana'  # 풀이 2


result = {}
for char in word:
    # result ['a']없으면 keyerror
    # result.get('a') 기본값이 None
    # result.get('a',0) 기본값이 0
    result[char] = result.get(char, 0 ) + 1

print(result)

# 출력
for key in result:
    print(key, result[key])
    
