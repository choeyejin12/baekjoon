def solution(array, commands):
    answer = []

    for i in commands:
        _array = array[i[0]-1:i[1]] #자른다

        _array.sort()

        answer.append(_array[i[2]-1])

    return answer

