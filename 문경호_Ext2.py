# 4개의 과목을 합계(개인합계, 전체합계) + 평균(개인평균 / 전체평균)
#홍길동1 '국' 95 '영' 90 '수' 80 '과' 50
#홍길동2 '국' 100 '영' 50 '수' 90 '과' 90
#홍길동3 '국' 99 '영' 60 '수' 100 '과' 40
#홍길동4 '국' 55 '영' 80 '수' 80 '과' 60
# 전체 4명의 합계, 평균
# for / while / if / elif
# 7가지 방법으로 코드를 작성 : 결과는 동일
# 개인 깃허브에 업데이트
# 폴더를 생성 후 파일을 올림
# 폴더명 MSA20220120

# 각 개인별 점수 합계와 평균
class Calculator:
    def add(lst):
        i = 0
        total = 0
        while i <len(lst):
            total += lst[i]
            i += 1
        everage = total / len(lst)
        return total, everage

a = [95, 90, 80, 50]
b = [100, 50, 90, 90]
c = [99, 60, 100, 40]
d = [55, 80, 80, 60]

홍길동1 = list(Calculator.add(a))
홍길동2 = list(Calculator.add(b))
홍길동3 = list(Calculator.add(c))
홍길동4 = list(Calculator.add(d))

temp = 0

# 전체 점수 합계와 평균
a = 홍길동1[0]
b = 홍길동2[0]
c = 홍길동3[0]
d = 홍길동4[0] 

e = (a,b,c,d)

전체 = list(Calculator.add(e))

temp = 0