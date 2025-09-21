from datetime import datetime, timedelta

#1 Current dat and time
now = datetime.now()
print(f"Now: {now}")

#2 Specific date (e.g., January 1, 2023)
specific_date = datetime(2023, 1, 1, 15, 36, 20)
print(f"Specific Date: {specific_date}")

#3 Format date to string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

other_formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"Other Formatted Date: {other_formatted_date}")

#4 Operaciones de fecha ( fecha + 7 días etc)
one_week_later = now + timedelta(weeks=1)
print(f"One Week Later: {one_week_later}")
yesterday = datetime.now() - timedelta(days=1)

#5 Obtener componentes individuales
year = now.year
print(f"Year: {year}")
month = now.month
print(f"Month: {month}")

#6 Calcular la diferencia entre 2 fechas
date1 = datetime(2023, 1, 1)
date2 = datetime(2023, 12, 31)
difference = date2 - date1
print(f"Difference in days: {difference.days}")

#7 Sel local date to chinese format
import locale
now = datetime.now()
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
spanish_formatted_date = now.strftime("%A %d de %B de %Y, %H:%M")
print(f"Spanish Formatted Date: {spanish_formatted_date}")

