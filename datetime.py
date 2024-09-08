from datetime import datetime
date ="oct 16 2004 1:15PM"
print(type(date))

datetime=datetime.strptime(date, "%b %d %Y %I:%M%p")
print(datetime)
print(type(datetime))