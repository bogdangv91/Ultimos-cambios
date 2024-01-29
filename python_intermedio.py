#Date

from datetime import datetime # Estamos importando un modulo
now = datetime.now() # Estamos utilizando el método now() del módulo datetime para obtener la fecha y hora actuales y almacenarlas en la variable now.


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
print_date(now)



timestamp = now.timestamp() # timestamp(): Este método es parte del objeto datetime en Python y devuelve la marca de tiempo Unix correspondiente a la fecha y hora almacenadas en el objeto datetime. La marca de tiempo Unix es un valor numérico que representa el número de segundos transcurridos desde el 1 de enero de 1970 a las 00:00:00 UTC (también conocido como el "epoch").
print(timestamp)

year_2024 = datetime(2024, 1, 29) # Asi creariamos una fecha.
print(year_2024)



