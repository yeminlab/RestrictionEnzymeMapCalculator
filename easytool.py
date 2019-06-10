def easyinput(a):
    a = '두'
    if a==1: a = '첫'
    temp = input(a+' 번째 제한 효소에 의한 전기 영동 결과와 제한효소 이름을 입력해주세요 ex)0.1,0.2,0.2,0.3,제한효소 이름\n')
    temp,name = temp.split(','),temp[-1] ; del(temp[-1])
    return temp, name

def checkform(a,b): #입력한 두 전기 영동 결과가 계산 가능한 값인지 판
    aa, bb = [],[]
    for i in a:
        aa.append(round(i,8))
    for i in b:
        bb.append(round(i,8)) #부동소수점 문제 해결
    if sum(a) == sum(b):
        size = round(sum(a),8)
        return size
    else:
        return False

print(checkform([0.1,0.3,0.4,0.5],[0.2,0.1,0.1,0.6,0.2]))
    
