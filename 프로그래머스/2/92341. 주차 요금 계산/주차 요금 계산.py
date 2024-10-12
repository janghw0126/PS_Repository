from collections import defaultdict
import math

def solution(fees, records):
    car_times = defaultdict(int)  # 차량별 누적 주차 시간을 저장
    in_times = {}  # 입차 시간을 기록
    
    # 기록 처리
    for record in records:
        time, car_num, action = record.split()
        time = int(time[:2]) * 60 + int(time[3:])  # 시간을 분 단위로 변환

        if action == "IN":
            in_times[car_num] = time
        else:
            car_times[car_num] += time - in_times.pop(car_num)  # 출차 후 누적 시간 계산
    
    # 출차 기록이 없는 차량 23:59 출차 처리
    for car_num, time in in_times.items():
        car_times[car_num] += 1439 - time  # 1439는 23:59를 분 단위로 변환한 값

    # 차량 번호순으로 정렬하고 요금 계산
    answer = []
    for car_num in sorted(car_times):
        total_time = car_times[car_num]
        if total_time <= fees[0]:
            answer.append(fees[1])
        else:
            extra_time = total_time - fees[0]
            extra_fee = math.ceil(extra_time / fees[2]) * fees[3]
            answer.append(fees[1] + extra_fee)

    return answer