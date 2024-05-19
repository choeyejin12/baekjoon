# 코드, 제조일, 최대수량, 현재수량 순으로 구성된 데이터
# 조건을 입력하면 만족하는 데이터만 뽑아서 정렬하려한다. 인덱스로 접근해야하려나?
# 거의 SQL 을 코드로 구현하는 느낌이네
# ext 에 오는 조건이 val_ext 보다 작은 데이터만 뽑고, sort_by 에 해당하는 값을 기준으로 "오름차순" 정렬하여 리턴.


def solution(data, ext, val_ext, sort_by):
    answer = []
    data_name= ["code","date","maximum","remain"]

    ext_idx = data_name.index(ext) # 인덱스를 반환
    sort_idx = data_name.index(sort_by)

    for i in data :
        if i[ext_idx] < val_ext :
            answer.append(i)
    
    answer.sort(key=lambda x: x[sort_idx])
    print(answer)
    
    
    return answer