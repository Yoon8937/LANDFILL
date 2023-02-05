# print('가능'*7) #--> 가능가능가능가능가능가능가능
# print(not False) #True
# print(not True)  #False
# print(not (5>10)) #True



# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# #이것은 bool타입임
# is_adult = age>=3 #3살보다 크면 어른
#
# print("우리집"+ animal +"의 이름은 " + name + "예요")
# print(name+"는"+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
# print(name,"는",age,"살이며, ",hobby,"을 아주 좋아해요") #but ,(콤마)를 하면 띄어씌기 하나 들감
# print(name +"는 어른일까요? " + str(is_adult))
# '''이렇게
# 하면
# 여러문장이
# 주석 가능'''
#
# print('''이렇게
# 하면
# 여러문장이
# 주석 가능''')
#
# sentence = """이렇게
#  하면
#     여러문장이
# 주석 가능"""
# print(sentence)
#
# #줄바꿈
# print("{0}과 {1}이 마르고 닳도록 하느님이 보우하사 우리나라 만세"\
#       .format("동해물","백두산"))


# print(2**3) #제곱
# print(9.2//3) #몫만 구하기
#
# print((3>0) and (3<5))
# print((3>0) & (3<5))    #이게 가능 하구나ㅋㅋㅋ. 몰랐넹
# print((3>0) or (3>5))
# print((3>0) | (3>5)) #이게 가능 하구나ㅋㅋㅋ. 몰랐넹
# print(5>4>3)#True
# print(5>4>7) #False
#
# print(abs(-5)) #절대값
# print(pow(4,2)) #제곱(4**2같음)     4^2이건 뭐지?
# print( max(5,12) )
# print( min(8,3,1) )
# print( round(3.14) ) #결과: 3
# print( round(4.59) ) #결과: 4
# print(round(3.141592,3)) #3번 인덱스에서 반올림해라
# import math
# print(math.sqrt(16)) #제곱근
# print(math.floor(4.99)) #내림
# print(math.ceil(3.14))  #올림
#
# import random
# print(random.random())
# # print(random())#밑에 처럼 할수 없음.
#
# from random import *
# print(random())
# print(random()*10) #0.0~10.0미만의 임이의 값 생성
# print(int(random()*10)+1)
# print(randrange(1,46)) #1부터 46미만의 수까지
# print(randint(1,45))#1부터45이하까지



# # 슬라이싱
# jumin = "980506-1234567"
# print(jumin[7:])
# print(jumin[-1:]) #맨뒤에 첫번째 숫자
# print(jumin[-7:]) #맨 뒤에서부터 7번째까지
#
# sen = "Python is Amazing Python P"
# print(sen.lower())
# print(sen.upper())
# print(sen[0].isupper())
# print(sen.replace("Python","Java")) #문자열에 있는 모든 단어를 replace함
#
# index = sen.index("n")
# print(index)
# index= sen.index("n", index+1) #n의 현재 인덱스에 1을 더하면 다음꺼 찾아줌.
# print(index)
#
# print(sen.find("java")) #값이 없으면 -1반환 BUT index함수는 에러남.



# #문자열포맷!!!
# #방법1
# print("나는 %d살입니다." %20)
# print("나는 %s을 좋아해요" % "파이썬")
# print("나는 %s살입니다." %20) #%s는 모두가능
# print("Apple은 %c로 시작해요" %"A") #char이라서 한글자만 받음
# print("나는 %s색과 %s색을 좋아해요"%("파란","빨간")) #두 개 이상 할때
#
# #방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요{2}".format("파란","빨간",10))
# #순서 바꾸기도 가능
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))
#
# #방법3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간",age=20 ))
#
# #방법4 (3.6V 이상부터 가능)
# age = 20
# color = "오렌지"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 탈출문자
# print("백문이 불여일견\n백견이 불여일타") #줄바꿈 : \n
# print("저는 \"토마토\"입니다.")
#
# print("Red\tApple") #탭 : \t
#
# # print("C:\Users\yoon\PycharmProjects\도서관리프로그램") #오류남
# print("C:\\Users\\yoon\\PycharmProjects\\도서관리프로그램") #\\를 두개 넣어줘야 인식함.



# #리스트
# # a = [9,8,7,9]
# # print(a.index(9))
# # print(a.index(9,1))
# subway = ["유재석","조세호",'박명수']
# # print(subway.index("조세호"))
# subway.insert(1,"정형돈") #인덱스 1에 들어가고 뒤로밀림
# print(subway)
# subway.pop()
# print(subway)
#
# num_list = [5,2,3,1,4]
# num_list.sort()
# print(num_list)
# # print(num_list.sort()) #이렇게하면 None출력됨
# # print(sorted(num_list)) #위 처럼 할거면 이렇게하기
# num_list.reverse()
# print(num_list)
# num_list.clear() #모두 지우기
# print(num_list)
#
# #다양한 자료형 함께 사용가능
# mix_list = ["조세호",20,True]
# num_list = [5,2,4,3,1]
# num_list.extend(mix_list) #리스트 확장
# print(num_list)


# #딕셔너리
# #키값은 중복이 안됨!
# cabin = {3:"유재석",100:"하하"}
# print(cabin[3])
# print(cabin[100])
# print(cabin.get(3)) #이것도 가능
# #만약없는 수를 가지고오면.
# # print(cabin[5]) #이건 오류남!!!
# print(cabin.get(5)) #이건 None출력됨
# print(cabin.get(5,"사용 가능")) #
#
# print(3 in cabin) #True
# print(5 in cabin) #False
#
# cabinet = {"A-3":"유재석","B-100":"하하"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])
# cabinet["A-3"] = "박명수" #박명수값이 업데이트됨.
# cabinet["C-20"] = "조세호" #추가할때
# print(cabinet)
#
# del cabinet["A-3"]
# print(cabinet)
# print( cabinet.keys() ) #키값만 출력
# print( cabinet.values() ) #value값만 출력
#
# cabinet.clear() #모두 지우기
# print(cabinet)


# #튜플
# #내용 변경, 추가 x  But 속도가 리스트보다 빠름.
# menu = ["돈까스", "치즈까스"]
# # menu.add("치킨") #불가능
#
# (name, age, hobby) = ("김종국","26","운동")
# print(name,age,hobby)
#
# tup = 1,2,3 #이것은 튜플. 1,2,3, 이것도 튜플.     1, 이것도 튜플.
# print(type(tup))


# # set(집합)
# # 중복 안됨, 순서 없음.
# my_set = {1,2,2,3,3,3}
# print(my_set)
#
# java = {"유재석","김태호","정형돈"} #set타입
# python = set(["유재석","박명수"])
# print(java & python) #교집합. 신기하네열
# print(java.intersection(python)) #교집합
#
# print(java | python) #합집합
# print(java.union(python)) #합집합
#
# print(java - python) #차집합
# print(java.difference(python)) #차집합
#
# python.add("김태호") #추가가능
# print(python)
# python.remove("김태호") #삭제가능
# print(python)


# #자료구조의 변경
# menu = {"커피","우유","주스"}
# print(menu,type(menu))
#
# menu = list(menu)
# print(menu,type(menu))
#
# menu = tuple(menu)
# print(menu,type(menu))
#
# menu = set(menu)
# print(menu,type(menu))



# if
# for waiting_no in [0,1,2,3,4,5]:
#     print("대기번호 : {0}".format(waiting_no))

# customer = "토르"
# person = "unknown"
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")



# def profile(name,age,main_lang):
#     print("이름 : {0}\t\t나이 :{1}\t\t주 사용언어 :{2}" \
#           .format(name,age,main_lang))
# profile("유재석",20,"파이썬")
# profile("정준하",25,"자바")
#
# #기본값
# def profile(name,age=20,main_lang='파이썬'):
#     print("이름 : {0}\t\t나이 :{1}\t\t주 사용언어 :{2}" \
#           .format(name,age,main_lang))
# profile('유재석')#아무것도 안주면, 디폴드값으로 들어감.
# profile('정준하',999,main_lang=" C language") #이렇게도 가능함.

# #가변인자!!!
# def profile(name,age,*language):
#     print("이름 : {0}\t\t나이 :{1}\t\t".format(name,age))
#     for lang in language:
#         print(lang,end=" ")
#     print()
# profile("유재서",20,"python",'java','C','C++','C#','JavaScript')
# profile("유재서",20,"kotlin",'swift')


# #지역변수(함수 안에서만 사용)와 전역변수(모든 공간에서 사용가능)
# gun = 10
# def checkpoint(soldiers): #경계근무
#     # gun = 20 #지역변수
#     global gun #전역변수
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
# print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명이 경계근무 나감
# print("남은 총 : {}".format(gun))
#
# print("=======================")
# gun = 10
# def betterCheckPoint(gun,sldr):
#     gun = gun - sldr
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
# print("전체 총 : {0}".format(gun))
# gun = betterCheckPoint(gun,2)
# print("남은 총 : {}".format(gun))





# 실행 shift + F10
# 행이동 alt + shift + 방향키

# print('hi'); print('idk') # 세미콜론으로 이렇게 가능

# num_count = [0] * 10 #오늘의 문법!!!!!
# print(num_count)

#오늘의 문법
# arr = list(map(int,range(10))) #이렇게도 초기화 가능!!!!!
# print(arr)


# n = 3
# arr=[0]*n
# #arr=[]*n #이렇게 하면결과는?
# print(arr)
#
# arr = [[] for _ in range(3)]
# print(arr)

# a,b,c = map(int,input().split())
# print(a,b,c)
# arr = list(map(int,input().split()))
# print(arr)


# word = "Hello"
# arr = word.split()
# arr = list(word)
# print(arr)
# s = "".join(arr) #리스트를 문자열로 만들기
# print(s)

# test = 7
# print('this is test',test)


### 둘이 비교해보기(결과는 무엇일까요?)
# arr = [[]] * 5
# print(arr)
#
# ## ※이것 주의하기※
# arr = [[]*5]
# print(arr)
# arr = [[7]*5]
# print(arr)


arr = [[]] * 5
arr[0].append(10)
## 결과 예측해보기~
# print(arr)    #답

arr[1].append(20)
# arr[0].append(0) #만약 이렇게 추가하면 어떻게 될까??
# print(arr)

###이렇게 추가하면 어떻게 될까요?  먼저 생각해보기
arr.append(30)
# print(arr)


### 이것의 결과는 뭘까요~?
array = [0]*4
# print(array)


### 이것의 결과는 뭘까요~?
# n = 3
# arr = [[0]*4 for i in range(n)]
# print(arr)
# arr = [[0] for i in range(n)]
# print(arr)


### 언더바(_)는 반복을 위해 변수의 값을 무시할 때 사용(단순반복에 사용)
# for _ in range(5):
#     print("hello world")

# #이럴때는 사용불가
# summary = 0
# for i in range(1,5):
#     summary += i

#이 때 언더바(_) 사용가능
# n=3
# n=4
# arr = [[0]*n for _ in range(n)]
# print(arr)

# #이럴때는 사용불가
# arr = [i*i for i in range(1,10)]


### 리스트 컴프리헨션을 이용하면 모두 동일한 객체에 대해서 똑같이 적용됨. 주의!
# n = 3
# m = 4
# arr = [[0]*m] * n
# print(arr)
# arr[1][1] = 7
# print(arr)




"""
입력 데이터의 개수가 많은 문제를 풀 때, input() 함수를 사용하면,
동작 속도가 느려서 시간 초과로 인한 오답 판정을 받을 수 있습니다.

따라서, 입력 데이터가 많은 문제에는, sys 라이브러리의 readline() 함수를
이용해 시간 초과를 피할 수 있습니다.

sys 라이브러리를 사용할 때는, 한 줄을 입력 받고 나서, 반드시 rstrip() 함수를 호출해야합니다.
● sys.stdin.readline() 으로 입력을 받으면, 입력 후 엔터가 줄 바꿈 기호로 입력되는데,
● 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야합니다.
"""

#한개의 정수 입력 받기
# import sys
# a = int(sys.stdin.readline().rstrip())
# print(a)

#공백 기준으로 분리된 여러 정수 입력 받기
# import sys
# a, b, c = map(int, sys.stdin.readline().rstrip().split())
# print(a,b,c)

#공백 기준으로 분리된 여러 정수를 입력 받아, 리스트에 저장하기
# import sys
# data = list(map(int, sys.stdin.readline().rstrip().split()))
#[1,2,3]

###공백 기준으로 분리된 여러 정수를 n번 입력 받아, 2차원 리스트에 저장하기
# import sys
# n = int(sys.stdin.readline().rstrip())
# data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# # data = [list(map(int,input().split())) for _ in range(n)] #위랑 같음
# # [[1, 2, 3], [4, 5, 6]]
# print(data)


#이거 어떻게 입력하는지 알기
# import sys
# n = int(sys.stdin.readline())
# money = [int(sys.stdin.readline()) for _ in range(n)]
# print(money)


## f-string
# print(f'hello world')
# k = 'usa'
# num = 7
# print(f'hello {k} world. {num}!')

# import sys
# s = sys.stdin.read()  #입력할때 다 입력하고서, ctrl + D 눌러줘야됨.
# print(s)



# sen = """Hello World
# I love Pizza!
# Python is the best language.
# """
# arr1 = sen.split('\n')
# print(arr1)
# arr2 = sen.splitlines() #위와 같은 결과가 도출됨.
# print(arr2)


## 이거 알 것 같은면 지우기
# import sys
# sen = sys.stdin.readline() #그럼 이건 어떻게 될까요?
# sen = sys.stdin.read() #입력을 다 하면, ctrl + D를 눌러줘야함.
# sen = sys.stdin.read().split() #그럼 이건 어떻게 될까요?
# print(sen)


# 이거 알면 지우기
# arr = [[-1, 1], [2, 1], [2, 2], [3, 3], [4, 0]]
# arr[0][0], arr[0][1] = arr[0][1], arr[0][0] #이렇게 둘이 바꾸는것도 가능
# print(arr)


# import sys
# arr = sys.stdin.read().split() #이 둘의 차이점은?
# arr = sys.stdin.read().splitlines() #이거 제대로 숙지하기!
# for i in arr:
#     print(int(i.split()[0]) + int(i.split()[1]))


### 백준 10951번
### 이러면 아무것도 입력안하고 엔터를 쳤을 때 while문이 종료
# while True:
#     try:
#         A, B= map(int,input().split())
#         print(A+B)
#     except:
#         break



# import sys
# n = 3
# 하나씩 비교해보기
# arr = [sys.stdin.readline() for _ in range(n)]
# arr = [sys.stdin.readline().split() for _ in range(n)]
# arr = [sys.stdin.readline().rstrip() for _ in range(n)]

#만약 이렇게하면 리스트가 리스트 안에 리스트를 집어넣게 된다. (X)
# arr = [sys.stdin.read().splitlines() for _ in range(n)]
# arr = sys.stdin.read().splitlines() #이렇게 해야됨.
# print(arr)


# import sys
# arr = []
# for line in sys.stdin:
#     arr.append(line.split())
# print(arr)


### 이렇게도 가능ㄷ ㄷ
# n = int(input())
# print("\n".join(map(str,range(n,0,-1))))


# #이런 문법도 있네용
# n = 10
# for i in reversed(range(1, n)):
#     print(i)


# 문자열리스트를 정수리스트로 바꾸는 방법은?
# for문 거꾸로 어캐 할까요?


# 이건 왜 쫌 다르냥
# graph = [[] for _ in range(3)]
# print(graph)
# graph[0].append(7)
# print(graph)
#
# arr = [[]] *3
# arr[0].append(7)
# print(arr)


# # 결과 예측 해보기
# arr = [ 1,2,3,4,5,6,7]
# # [ 시작 인덱스 : 끝 인덱스 : 간격 ]
# print(arr[::2])
# print(arr[::3])
#
# print(arr[-1:])
#
# print(arr[:-1]);print(arr[::-1])
# arr = list(reversed(arr)) #list붙여줘야 함
# print(arr)


# n을 입력받는것을 리스트 안에다 넣어줌ㄷㄷ
# arr = [input()[0] for _ in range(int(input()))]


