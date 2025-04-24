# Taken from mission Lightbulb Intro

from datetime import datetime
from typing import List
def sum_light(els: List[datetime]) -> int:
    summa = 0
    for episode in range(0, len(els), 2):
        summa += (els[episode + 1] - els[episode]).total_seconds()
    #print (summa)
    return summa
    return 0


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ]
        )
    )
    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
            ]
        )
        == 610
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ]
        )
        == 1220
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 12, 10, 10),
            ]
        )
        == 4820
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 1),
            ]
        )
        == 1
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 13, 11, 0, 0),
            ]
        )
        == 86410
    )
    print(
        "The first mission in series is completed? Click 'Check' to earn cool rewards!"
    )


from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    #print('---------------- NEW --------------------')
    #print(els, start_watching)
    summa = 0
    epoch_time = datetime(1970, 1, 1)
    #print((start_watching - datetime(1970, 1, 1)).total_seconds())
    if start_watching is None:
        #print('start_watching is None !!!')
        summa = 0
        for episode in range(0, len(els), 2):
            summa += (els[episode + 1] - els[episode]).total_seconds()
        return summa


    for episode in range(0, len(els), 2):
        if (els[episode] - epoch_time).total_seconds() < (start_watching - epoch_time).total_seconds() and \
        (els[episode + 1] - epoch_time).total_seconds() >= (start_watching - epoch_time).total_seconds():
            summa += (els[episode + 1] - epoch_time).total_seconds() - (start_watching - epoch_time).total_seconds()
            #print('Начало отсчета времени с start_watching', start_watching, els[episode + 1], summa)
        elif (els[episode + 1] - epoch_time).total_seconds() < (start_watching - epoch_time).total_seconds():
            #print('Старт отсчета еще не начался', els[episode + 1], '  Старт отсчета:', start_watching)
            continue
        else:
            summa += (els[episode + 1] - epoch_time).total_seconds() - (els[episode] - epoch_time).total_seconds()
            #print ('Начало отсчета времени с ', els[episode], els[episode + 1],summa)
    return summa
    return 0


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 5),
        )
    )

    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 5),
        )
        == 5
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 610
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 600
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
        )
        == 620
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 10, 11),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 9, 11),
        )
        == 60
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10)
            ]
        )
        == 1220
    )

    print("The second mission in series is done? Click 'Check' to earn cool rewards!")