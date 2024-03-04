time = input().split()
ini_time = int(time[0])
end_time = int(time[1])
max_time = 23

if ini_time > max_time or end_time > max_time:
    print('FALSE')
else:
    if end_time > ini_time:
        duration = end_time - ini_time
    elif end_time == ini_time:
        duration = 24
    else:
        duration = end_time + 24 - ini_time

    print(f'O JOGO DUROU {duration} HORA(S)')
