from dateutil.parser import parse


def driver(data):
    lic = ""
    if len(data[2]) >= 5:
        lic += data[2][:5]
    else:
        lic += data[2]
        while len(lic) < 5:
            lic += "9"
    lic += (str(parse(data[3]).year))[2]
    month = parse(data[3]).month
    if data[4] == "F":
        month += 50
    month = str(month)
    if len(month) == 1:
        month = "0" + month
    lic += month
    day = str(parse(data[3]).day)
    if len(day) == 1:
        day = "0" + day
    lic += day
    lic += (str(parse(data[3]).year))[3]
    lic += data[0][:1]
    if (data[1]) != "":
        lic += data[1][:1]
    else:
        lic += "9"
    lic += "9AA"

    return lic.upper()


# test
driver_data = ["John", "James", "Smith", "01-Jan-2000", "M"]
print(driver(driver_data))
