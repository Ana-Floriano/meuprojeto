from datetime import datetime, timedelta

data = datetime.strptime("09-22-2026", "%m-%d-%Y")
print(data + timedelta(1000)) #qual sera a data daqui a 1000 dias
