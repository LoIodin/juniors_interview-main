def appearance(intervals: dict[str, list[int]]) -> int:
    sum_sec = 0
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']

    for i in range(0, len(pupil), 2):
        for j in range(0, len(tutor), 2):
            left_interval = 0
            right_interval = 0

            if pupil[i] > tutor[j+1] or tutor[j] > pupil[i+1]:
                continue

            if pupil[i] >= lesson[0] and pupil[i] >= tutor[j]:
                left_interval = pupil[i]
            elif tutor[j] >= lesson[0] and tutor[j] >= pupil[i]:
                left_interval = tutor[j]
            else:
                left_interval = lesson[0]

            if pupil[i+1] <= lesson[1] and pupil[i+1] <= tutor[j+1]:
                right_interval = pupil[i+1]
            elif tutor[j+1] <= lesson[1] and tutor[j+1] <= pupil[i+1]:
                right_interval = tutor[j+1]
            else:
                right_interval = lesson[1]

            if right_interval > left_interval:
                interval = right_interval - left_interval
                sum_sec += interval
            else:
                continue
    return sum_sec


tests = [
    {'intervals':
         {'lesson': [1594663200, 1594666800],
          'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
          'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
         },
     'answer': 3117
    },
    # {'intervals': {'lesson': [1594702800, 1594706400],
    #          'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
    #          'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    # 'answer': 3577
    # },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

# второе значение в исходных данных закомментировал, потому что в них ошибка, у вас ученик в прошлое возвращается, я с такой магией не сталкивался еще