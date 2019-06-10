E = [0.1, 0.4, 0.6, 0.2]
B = [0.2, 0.4, 0.1, 0.2]
size=(sum(E))

def make_input(): #전기 영동 결과를 인풋받는다
    return

def make_cut(a):
    s = sum(a)
    b = [0]
    c = []
    if len(a) > 1:
        for i in range(0,len(a)):
            if i == len(a)-1:
                break
            temp_sum = b[i]
            b.append(a[i]+temp_sum) #~전기영동정보를 자르는 위치로 변환
    del b[0] #연산을 위해 넣어줬던 0 값을 지움
    for i in b:
      c.append(round(i,8))
    return c


def combine(a,b): #a,b 제한효소 지도 자리를 합친다
    c = a+b
    c_f = []
    for i in c:
        c_f.append(round(i,8))
    return sorted(c_f) #효소 자리 순서에 맞게 리턴


def make_result(a,size): #제한 효소 cut정보를 전기영동 결과로 반환
    c,b=[],[]
    b.append(a[0])
    b.append(size-a[-1])
    for i in range(1,len(a)):
        b.append(a[i]-a[i-1])
    for i in b:
        c.append(round(i,8)) #데이터 연산에 의한 소수점 오류를 개선하기 위해 round사용(ex. 1.0000000004)
    c.sort()
    if c[0] == 0 or 0.0:
        del c[0]
    return sorted(c)


def D_permuatation(a): #유전자 제한 효소 지도 순서 미 제시 때
    import itertools
    temp = []
    mypermuatation = itertools.permutations(a)
    for i in mypermuatation:
        temp.append(list(i))
    return temp

E_allcase = D_permuatation(E)
B_allcase = D_permuatation(B)
answer=[0.1, 0.1, 0.1, 0.1, 0.2, 0.3, 0.4] #정답인 pcr결과
final = []
for i in E_allcase : 
    for j in B_allcase:
        a,b = make_cut(i),make_cut(j)
        temp = combine(a,b)
        final.append(str(make_result(temp,size))+'제한효소E:'+str(a)+'제한효소B:'+str(b))

#print(final)
for i in final:
    if str(sorted(answer)) in i:
        print(i)
