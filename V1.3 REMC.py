
def easyinput():
    dic = {'size': 0,'a': list(map(float,input('첫 번째 제한 효소에 의한 전기 영동 결과를 입력해주세요 ex)0.1,0.2,0.2,0.3\n').split(','))),
           'aname': input('제한 효소의 이름을 입력해주세요'), 'b': list(map(float,input('두 번째 제한 효소에 의한 전기 영동 결과를 입력해주세요 ex)0.1,0.2,0.2,0.3\n').split(','))),
           'bname': input('제한 효소의 이름을 입력해주세요'), 'c': list(map(float,input('두 제한효소의 조합에 의한 전기 영동결과를 입력해주세요 ex)0.1,0.2,0.2,0.3\n').split(',')))}
    return dic
def checkform(dic): #입력한  전기 영동 결과가 계산 가능한 값인지 판
    print(round(sum(dic['a']),8), round(sum(dic['b']),8), round(sum(dic['c']),8))
    if round(sum(dic['a']),8) == round(sum(dic['b']),8) and round(sum(dic['b']),8) == round(sum(dic['c']),8):
        dic['size'] = round(sum(dic['a']),8)
        print(dic)
        return dic
    else:
        return False

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


def calc_return(a,b, aname,bname,size, answer):
    a_allcase, b_allcase,final,r_final = D_permuatation(a), D_permuatation(b), [], []
    for i in a_allcase :
        for j in b_allcase :
            ta, tb = make_cut(i), make_cut(j)
            temp = combine(ta, tb)
            final.append(aname+':'+str(ta)+bname+':'+str(tb))
            #final.append(str(make_result(temp,size))+aname+':'+str(ta)+bname+':'+str(tb))
    for i in final:
        if str(sorted(answer)) in i:
            r_final.append(i)
    r_final = list(set(r_final))
    return r_final

def calc_print(a, b,aname,bname, size, answer):
    for i in calc_return(a, b,aname,bname, size, answer):
        print(i)

a = easyinput()
a = checkform(a)
#print(easyinput()['1a'][2])
calc_print(a['a'],a['b'],a['aname'],a['bname'], a['size'], a['c'])
