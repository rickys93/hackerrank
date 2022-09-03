def timeConversion(s):
    # Write your code here
    if s[:2] == '12' and s[-2:] == 'AM':
        s = '00' + s[2:]

    if s[-2:] == 'PM' and s[:2] != '12':
        s = str(int(s[:2]) + 12) + s[2:]

    
    s = s[:-2]
    
    return s


t1 = '07:05:45PM'
t2 = '07:05:45AM'
t3 = '12:05:45AM'
t4 = '01:05:45AM'
t5 = '12:05:45PM'


print(timeConversion(t1))
print(timeConversion(t2))
print(timeConversion(t3))
print(timeConversion(t4))
print(timeConversion(t5))