from datetime import datetime

def random_numbers():
    number = 0
    time = datetime.now()
    bond = "{}".format(time.microsecond)
    for i in bond:
        number ^= int(i)
    bond = "0.{}{}".format(number,time.microsecond)
    return float(bond)

print(random_numbers())