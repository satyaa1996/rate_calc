def computepay(hrs,rate):
    if hrs < 40:
        total = hrs * rate
        return total
    elif hrs > 40 :
        exhrs = hrs - 40
        total = (40 * rate ) + (exhrs * rate * 1.5)
        return total
hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("enter rate")
rate = float(rate)
pa = computepay(hrs,rate)
print (pa)
