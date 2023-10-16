hours = int(input())
minutes = int(input())
delivery = int(input())
total_hours = hours + delivery // 60
if total_hours > 24:
    total_hours = total_hours % 24
total_minutes = minutes + delivery % 60
if total_minutes >= 60:
    total_minutes = total_minutes - 60
    total_hours = total_hours + 1
if total_hours == 24:
    total_hours = 0
if total_hours < 10 and total_minutes < 10:
    print("0", total_hours, ":", "0", total_minutes, sep="")
elif total_hours > 10 and total_minutes < 10:
    print(total_hours, ":", "0", total_minutes, sep="")
elif total_hours < 10 and total_minutes > 10:
    print("0", total_hours, ":", total_minutes, sep="")

else:
    print(total_hours, ":", total_minutes, sep="")










