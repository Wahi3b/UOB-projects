from datetime import datetime,timedelta
data = datetime.today().date()
exist = datetime.today().date() + timedelta(days=1)
sub = exist - data 
print(int(sub.days))