from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    minutes = int(time[:2]) * 60 + int(time[3:]) - 360
    if minutes < 0 or minutes > 720:
        return 'I don\'t see the sun!'
    #print (minutes * 0.25)
    return minutes * 0.25


print("Example:")
print(sun_angle("07:00"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

print("The mission is done! Click 'Check Solution' to earn rewards!")