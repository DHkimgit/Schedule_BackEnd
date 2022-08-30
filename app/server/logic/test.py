from typing import List
from dateutil.parser import parse
import datetime 

# 근무 시간 배열, 근무 순서 배열, 오늘 날짜
def MakeDailyScheduleGroup_Foward(array_time : List[int], array_roster = List[str], roster_pointer = int, todaydate = str) -> List:
    result = []
    returned_pointer = roster_pointer
    # 시간 포맷팅 [630, 830] => ['06:30 - 08:30' ...]
    for i in range(len(array_time) - 1):
        start_time = str(array_time[i])
        end_time = str(array_time[i + 1])
        if len(start_time) != 4:
            start_time = start_time.zfill(4)
        if len(end_time) != 4:
            end_time = end_time.zfill(4)
        result.append([f'{start_time[0]}{start_time[1]}:{start_time[2]}{start_time[3]} - {end_time[0]}{end_time[1]}:{end_time[2]}{end_time[3]}'])
    
    for i in range(len(result)):
        if returned_pointer > len(array_roster) - 1:
            returned_pointer = 0
        result[i].append(array_roster[returned_pointer])
        returned_pointer += 1

    today_date = parse(todaydate)
    oneday = datetime.timedelta(days=1)
    tommorow = str(today_date + oneday)
    nextdate = f'{tommorow[5]}{tommorow[6]}-{tommorow[8]}{tommorow[9]}'

    return result, returned_pointer, nextdate

def MakeDailyScheduleGroup_BackWard(array_time : List[int], array_roster = List[str], roster_pointer = int, todaydate = int) -> List:
    result = []
    # 시간 포맷팅 [630, 830] => ['06:30 - 08:30' ...]
    for i in range(len(array_time) - 1):
        start_time = str(array_time[i])
        end_time = str(array_time[i + 1])
        if len(start_time) != 4:
            start_time = start_time.zfill(4)
        if len(end_time) != 4:
            end_time = end_time.zfill(4)
        result.append([f'{start_time[0]}{start_time[1]}:{start_time[2]}{start_time[3]} - {end_time[0]}{end_time[1]}:{end_time[2]}{end_time[3]}'])
    
    for i in range(len(result)):
        result[i].append(array_roster[i])

    return result

def MakeDailySchedule_TimeFormatting(array_time : List[int]) -> List:
    result = []
    for i in range(len(array_time) - 1):
        start_time = str(array_time[i])
        end_time = str(array_time[i + 1])
        if len(start_time) != 4:
            start_time = start_time.zfill(4)
        if len(end_time) != 4:
            end_time = end_time.zfill(4)
        result.append([f'{start_time[0]}{start_time[1]}:{start_time[2]}{start_time[3]} - {end_time[0]}{end_time[1]}:{end_time[2]}{end_time[3]}'])

    return result

def MakeWeekelySchedule_group(array_time : List[int], array_roster = List[str], monday_date = str) -> dict:
    weekly_roster = {}
    monday_list, monday_ponter, tuesday_date = MakeDailyScheduleGroup_Foward(array_time, array_roster, 0, monday_date)
    tuesday_list, tuesday_ponter, wednesday_date = MakeDailyScheduleGroup_Foward(array_time, array_roster, monday_ponter, tuesday_date)
    wednesday_list, wednesday_ponter, thursday_date = MakeDailyScheduleGroup_Foward(array_time, array_roster, tuesday_ponter, wednesday_date)
    thursday_list, thursday_ponter, friday_date = MakeDailyScheduleGroup_Foward(array_time, array_roster, wednesday_ponter, thursday_date)
    friday_list, friday_ponter, saterday_date = MakeDailyScheduleGroup_Foward(array_time, array_roster, thursday_ponter, friday_date)
    weekly_roster["Monday"] = monday_list
    weekly_roster["Tuesday"] = tuesday_list
    weekly_roster["Wednesday"] = wednesday_list
    weekly_roster["Thursday"] = thursday_list
    weekly_roster["Friday"] = friday_list

    return weekly_roster

def MakeWeekelySchedule_returnlist(array_time : List[int], array_roster = List[str], monday_date = str):
    monday_list, monday_ponter, tuesday_date = MakeDailyScheduleGroup_Foward(array_time, array_roster, 0, monday_date)
    tuesday_list, tuesday_ponter, wednesday_date = MakeDailyScheduleGroup_Foward(array_time, array_roster, monday_ponter, tuesday_date)
    wednesday_list, wednesday_ponter, thursday_date = MakeDailyScheduleGroup_Foward(array_time, array_roster, tuesday_ponter, wednesday_date)
    thursday_list, thursday_ponter, friday_date = MakeDailyScheduleGroup_Foward(array_time, array_roster, wednesday_ponter, thursday_date)
    friday_list, friday_ponter, saterday_date = MakeDailyScheduleGroup_Foward(array_time, array_roster, thursday_ponter, friday_date)

    return monday_list, tuesday_list, wednesday_list, thursday_list, friday_list

def MakeWeekelySchedule_returnGroups(array_time : List[int], array_roster = List[str], monday_date = str) -> List:
    # array_time = [[600, 800], [800, 1000, 1200, 1400, 1600, 1800], [1800, 2000], [2000, 2200]]
    # array_roster = 
    tmp = []
    for i in range(len(array_time)):
        monday_list, tuesday_list, wednesday_list, thursday_list, friday_list = MakeWeekelySchedule_returnlist(array_time[i], array_roster, monday_date)
        tmp.append([monday_list, tuesday_list, wednesday_list, thursday_list, friday_list])
    
    return tmp

def MakeWeekelySchedule(Groups : List):
    weekly_roster = {}
    weekly_roster["Monday"] = []
    weekly_roster["Tuesday"] = []
    weekly_roster["Wednesday"] = []
    weekly_roster["Thursday"] = []
    weekly_roster["Friday"] = []
    for i in range(len(Groups)):
        for j in range(len(Groups[i][0])):
            weekly_roster["Monday"].append(Groups[i][0][j])
    for i in range(len(Groups)):
        for j in range(len(Groups[i][0])):
            weekly_roster["Tuesday"].append(Groups[i][1][j])
    for i in range(len(Groups)):
        for j in range(len(Groups[i][0])):
            weekly_roster["Wednesday"].append(Groups[i][2][j])
    for i in range(len(Groups)):
        for j in range(len(Groups[i][0])):
            weekly_roster["Thursday"].append(Groups[i][3][j])
    for i in range(len(Groups)):
        for j in range(len(Groups[i][0])):
            weekly_roster["Friday"].append(Groups[i][4][j])

    return weekly_roster

