# 최빈값구하기
# 만약 최빈값이 두개면은 두개 다 출력...



# import sys
# arr = sys.stdin.read().split() #이 둘의 차이점은?
# arr = sys.stdin.read().splitlines() #이거 제대로 숙지하기!
# for i in arr:
#     print(int(i.split()[0]) + int(i.split()[1]))


# import sys
# s = sys.stdin
# for i in s:
#     print(i.split())
# # 후 이건 뭐지...









# arr = [i for i in range(1,8)]
# cnt = 0
# i = 0
# while len(arr)!=0:
#     cnt +=1
#     if cnt==3:
#         print(i,arr,len(arr))
#         del arr[i]
#         cnt = 1
#     i += 1
#     if i==arr.index(arr[-1:][0]):
#         print('moyaho')
#         i = 0

# arr = [i for i in range(1,11)]
# for i in arr:
#     if i==4:
#         del arr[i]
#     if len(arr) == 9:
#         print(len(arr))
# print(arr)



# arr = [i for i in range(1,8)]
# cnt = 1
# i = 0
# while len(arr)!=0:
#     print(arr)
#     if cnt==3:
#         del arr[i]
#         cnt = 1
#     if i == arr.index(arr[-1:][0]):
#         i = 0
#     i += 1
#     cnt +=1

# 1 2 3 4 5 6



#
# arr = [1,2,3]
# i = 0
# cnt = 1
# while len(arr)!=1:
#     print(arr)
#     if cnt == 3:
#         del arr[i]
#     if i > len(arr):
#         print(i,len(arr))
#         print('moya')
#         i -= 2
#     if i == arr.index(arr[-1:][0]):
#         print('moya2')
#
#         i = -1
#     i +=1
#     cnt +=1






import sys
n = int(input())
for i in range(n):
    qnty, idx = map(int,input().split())
    queue = list(map(int,sys.stdin.readline().split()))
    cnt = 0
    while True:
        if queue[0]==max(queue):#가장 큰 수가 첫번째에 왔을때
            cnt += 1
            if queue.index(queue[0]) == idx:#인덱스끼리 비교. 숫자끼리 비교하면 안됨!조심!
                print(cnt)
                break
            queue.pop(0)
        else:
            queue.append(queue.pop(0))
        idx -=1     #제일 큰 수가 제거되거나, 땡겨지므로 idx에 -1을한다.
        if idx < 0: #BUT 인덱스가 0일때 마이너스면 맨 뒤로 보내주기.
            idx = len(queue)-1


# 약 50분 안에 풀었네..

