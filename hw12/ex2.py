import datetime
now = datetime.datetime.now()

D = dict(
    day = str(now.day),
    month = str(now.month),
    year= str(now.year),
    hour = str(now.hour),
    minute = str(now.minute),
    second = str(now.second)
)

fs = "{day}{sep1}{month}{sep1}{year} {hour}{sep2}{minute}{sep2}{second}"

s = fs.format(**D, sep1='.', sep2=':')


with open ('hw12_ex2.txt', 'w') as f:
    f.write(s)