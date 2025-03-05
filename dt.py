from datetime import datetime
date ="oct 16 2004 1:15PM"
print(type(date))
date_time=datetime.strptime(date, "%b %d %Y %I:%M%p")
print(date_time)
print(type(date_time))