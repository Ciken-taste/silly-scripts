import urllib3
import datetime

manager = urllib3.PoolManager()
responce = manager.request('GET', 'https://www.foreca.fi/Finland/Lapua/10vrk')

def date_stringer(day, month):
    return str(day) + "." + str(month)


finnish_weekdays = {
    0:"Ma ",
    1:"Ti ",
    2:"Ke ",
    3:"To ",
    4:"Pe ",
    5:"La ",
    6:"Su ",
    7:"Ma "
}

finnish_wind_directions = {
    "N": "Pohjoinen",
    "NE": "Koillinen",
    "E": "Etelä",
    "SE": "Kaakko",
    "S": "Etelä",
    "SW": "Lounas",
    "W": "Länsi",
    "NW": "Luode"
}


# DATE: Index 0 = month, Index 1 = day
date = str(datetime.datetime.now()).split()[0].split('-')
date.pop(0)
if int(date[0]) < 10:
    date[0] = date[0][1:]
if int(date[1]) < 10:
    date[1] = date[1][1:]


current_weekday = datetime.datetime.now().weekday()

current_data = str(responce.data).split(finnish_weekdays[current_weekday] + date_stringer(date[1], date[0]))
current_data = current_data[1]

date_tmr = int(date[1]) + 1

current_data = str(current_data).split(finnish_weekdays[current_weekday + 1] + date_stringer(date_tmr, date[0]))
current_data = current_data[0]

current_data = current_data.split('"')

#for i in range(len(current_data)):
#    print(i-1, current_data[i - 1])


cloudy = current_data[15]
highest = current_data[22]
lowest = current_data[26]
wind_dir = current_data[37]
wind_speed = current_data[42]
average_wind = wind_speed.split()[0]
wind_peaks = wind_speed.split()[1]

cloudy = cloudy.replace('\xc3\xa4', 'a')

highest = highest.split(";")[0].replace("&deg", " C")
lowest = lowest.split(";")[0].replace("&deg", " C")
average_wind = average_wind.replace("><p><em>", "").replace("</em>", " m/s")
wind_peaks = wind_peaks.replace("(", "").replace(")</p><p", " m/s")

for i in range(5): print(" ")
print("Sää ennuste päivälle", finnish_weekdays[current_weekday], str(datetime.datetime.now()).split()[0])
print("PILVIÄ", cloudy)
print("KORKEIMMILLAAN", highest)
print("ALIMMILLAAN", lowest)
print("TUULEN SUUNTA", finnish_wind_directions[wind_dir], "(" + wind_dir + ")")
print("KESKIVERTO TUULEN NOPEUS", average_wind)
print("TUULIPUUSKIEN NOPEUS", wind_peaks)