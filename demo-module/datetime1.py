from datetime import datetime

simdi = datetime.now()

result = datetime.now().hour

result = datetime.ctime(simdi)

result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%X')
result = datetime.strftime(simdi,'%d')
result = datetime.strftime(simdi,'%A')
result = datetime.strftime(simdi,'%B')
result = datetime.strftime(simdi,'%Y %B %A')

t = '14 May 2023 hour 12:10:30'

dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
dt = dt.year
# print(dt)

birthday = datetime(1984,12,23,5,30,00)

result = datetime.timestamp(birthday) #saniye
result = datetime.fromtimestamp(result) # saniye to datetime

birthday = datetime(1970,1,1,3,0,0)
result = datetime.timestamp(birthday)
result = datetime.fromtimestamp(0)

result = simdi - birthday #timedelta
#result = result.days
result = result.seconds

from datetime import timedelta

result = simdi + timedelta(days=12)



print(result) 




#print(result)

