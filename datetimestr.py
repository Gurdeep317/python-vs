# Program to Convert String to Datetime
# using datetime module
# import module
from datetime import datetime
string="31 May 2005 1:05 PM"
datetime=datetime.strptime(string,'%b %d %Y %I:%M%p')
print(type(datetime))
print(type(datetime))
print(datetime)