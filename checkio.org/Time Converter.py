def time_converter(time: str) -> str:
    time_in = time.split(':')
    #print(time_in)
    time_out = []
    if time_in[0] == '00':
        time_out.append('12')
        time_out.append(time_in[1]  + ' a.m.')
    elif int(time_in[0]) == 12:
        time_out.append(time_in[0])
        if time_out[0][:1] == '0':
            time_out[0] = time_out[0][1:]
    #        print(time_out[0])
        time_out.append(time_in[1]  + ' p.m.')
    elif int(time_in[0]) > 12:
        time_out.append(str(int(time_in[0]) - 12))
    #    print(time_out[0])
        if time_out[0][:1] == '0':
            time_out[0] = time_out[0][1:]
    #        print(time_out[0])
        time_out.append(time_in[1]  + ' p.m.')
    else:
        time_out.append(time_in[0])
        if time_out[0][:1] == '0':
            time_out[0] = time_out[0][1:]
    #        print(time_out[0])
        time_out.append(time_in[1]  + ' a.m.')
    #print('-------' + time_out[0] + ':' + time_out[1])
    return time_out[0] + ':' + time_out[1]


print("Example:")
print(time_converter("12:30"))

assert time_converter("12:30") == "12:30 p.m."
assert time_converter("09:00") == "9:00 a.m."
assert time_converter('00:00') == '12:00 a.m.'

print("The mission is done! Click 'Check Solution' to earn rewards!")
