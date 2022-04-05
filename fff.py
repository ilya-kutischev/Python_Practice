def lamp(lst: list):
    if len(lst)%2 ==1 :
        raise ValueError()
    total_time =0
    for i in range(len(lst)):
        lst[i] = lst[i].split(" ")
        day, month, year = lst[i][0].split(".")
        hour, minute = lst[i][1].split(":")
        if  i % 2 == 1:
            k=1
        else:
            k = -1
        total_time = total_time +k* ( int(minute)*60 + int(hour)*3600 + int(day)*86400 + int(month)*86400*30 + int(year)*86400*365.25)
    return  total_time


if __name__ == '__main__':
    ls = ["11.06.2021 18:00", "11.06.2021 19:00"]
    print(lamp(ls))