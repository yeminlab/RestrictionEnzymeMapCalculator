def easyinput(): #두 제한효소를 입력 받는다.(이름과 전기 영동 결과)
    dic = {'size': 0,'a': list(map(float,input('첫 번째 제한 효소에 의한 전기 영동 결과를 입력해주세요 ex)0.1,0.2,0.2,0.3\n').split(','))),
           'aname': input('제한 효소의 이름을 입력해주세요'), 'b': list(map(float,input('두 번째 제한 효소에 의한 전기 영동 결과를 입력해주세요 ex)0.1,0.2,0.2,0.3\n').split(','))),
           'bname': input('제한 효소의 이름을 입력해주세요'), 'c': list(map(float,input('두 제한효소의 조합에 의한 전기 영동결과를 입력해주세요 ex)0.1,0.2,0.2,0.3\n').split(',')))}
    return dic
def checkform(dic): #입력한  전기 영동 결과가 계산 가능한 값인지 판단한다.(전기 영동 결과의 합으로 길이 계산) 아닐 경우 false 리턴.
    print(round(sum(dic['a']),8), round(sum(dic['b']),8), round(sum(dic['c']),8))
    if round(sum(dic['a']),8) == round(sum(dic['b']),8) and round(sum(dic['b']),8) == round(sum(dic['c']),8): #부동소수점 오류 때메 반올림 사용.
        dic['size'] = round(sum(dic['a']),8)
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
            temp_sum = b[i] #결과가[0.1,0.2,0.3]이면 [0.1,0.2+0.1, 0.3+0.2]이런식으로 변환하여 계산에 용이하게 바꿈
            b.append(a[i]+temp_sum) #~전기영동결과를 자르는 위치로 변환
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
    for i in range(1,len(a)): #제한 효소 자리가 [0.1,0.2,0.4]이고 길이가 0.5이면 [0.1, 0.2-0.1, 0.4-0.2, 0.5-0.4]이런 식으로 변환
        b.append(a[i]-a[i-1])
    for i in b:
        c.append(round(i,8)) #데이터 연산에 의한 소수점 오류를 개선하기 위해 round사용(ex. 1.0000000004) 실제로 처리하지 않을 경우 에러가 뜸.
    c.sort()
    if c[0] == 0 or 0.0: #전기 영동 결과에 0이 들어가는 것을 방지한다. (의미없는 데이터 삭제
        del c[0]
    return sorted(c)


def D_permuatation(a): #전기 영동 결과로 만들 수 있는 모든 조합을 구한다.
    import itertools
    temp = []
    mypermuatation = itertools.permutations(a)
    for i in mypermuatation:
        temp.append(list(i))
    return temp #모든 조합이 담긴 리스트를 리턴한다.


def calc_return(a,b, aname,bname,size, answer): #가능한 모든 조합을 만든 후 가능한 제한 효소 자리 리턴한다.
    a_allcase, b_allcase,final,r_final = D_permuatation(a), D_permuatation(b), [], [] #가능한 경우의수를 계산해주는 코드이다.
    for i in a_allcase :
        for j in b_allcase :
            ta, tb = make_cut(i), make_cut(j)
            temp = combine(ta, tb)
            final.append(str(make_result(temp,size))+aname+':'+str(ta)+bname+':'+str(tb))
    for i in final: #사용자가 입력한 전기영동결과와 일치하는 제한효소 자리만 리턴한다
        if str(sorted(answer)) in i:
            r_final.append(i)
    r_final = list(set(r_final))
    return r_final

def calc_print(a, b,aname,bname, size, answer): #calc_return의 결과를 표시하여 준다.
    d = []
    
    for i in calc_return(a, b,aname,bname, size, answer):              
        replaced_i = i.replace(str(sorted(list(map(float,answer)))),"") 
        d.append(replaced_i)
        print(replaced_i)
    print('---------------모든 가능한 제한 효소 자리---------------')  # 사용자에게 가능한 제한효소 지도의 모든 경우의 수를 보여준다.
    temp = input('사용자 지정 제한 효소 자리와 일치하는 결과를 찾으시겠습니까? Y/N입력')  # 사용자가 제한효소 지도의 일부븐을 알고 있을때 사용할수 있도록 사용자 지정 옵션을 추가 하였따.
    if temp == 'Y':
        aa = sorted(list(map(float,input('제한 효소 자리를 입력해주세요 예)0.2,0.4,0.5').split(',')))) 
        aaname = input('제한 효소의 이름을 입력해주세요') # 실제로 일정부분의 지도를 알고 있는 상태에서 추가적으로 지도를 넓혀가는 방식이기 때문에 매우 유용하다.
        aa = aaname + ':' + str(aa)
        for i in d:
            if aa in i:
                print(i)
                
                #추가적으로 matplotlib이나 vpython과 연계하여 등을 사용하여 한눈에 볼수 있도록 구현하면 좋을 것 같다.
           
    

a=easyinput()
a=checkform(a)
calc_print(a['a'],a['b'],a['aname'],a['bname'], a['size'], a['c'])
