import random
import time

def getRandomDate(startDate, endDate ):
    print("Printing random date between", startDate ,"and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomtime = startTime + randomGenerator * (startTime - endTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomtime))
    return randomDate

print("RandomDate = ", getRandomDate("1/1/2016", "12/12/2018"))