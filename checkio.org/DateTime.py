# Подсчет количества суббот и воскресений между двумя датами
from datetime import date, timedelta

def checkio(from_date, to_date):
    print('------------------------------------------')
    print(from_date, to_date)
    count = 0
    for i in range(int ((to_date - from_date).days) + 1):
        #print (from_date + timedelta(i))
        #print ((from_date + timedelta(i)).weekday())
        if (from_date + timedelta(i)).weekday() == 5 or (from_date + timedelta(i)).weekday() == 6:
           count += 1
      
    print(count)
    return count


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"