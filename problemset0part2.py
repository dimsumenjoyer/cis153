'''
Victor Van
Problem Set 0 part 2 - Due: 9/12/2023
function that calculates weekly wages
9/6/2023
I copied and paste my old code from an assignment from intro to CS,
instead of typing something like: print("Hello world!")
'''
def computepay():
    h = float(input("Enter Hours: "))
    r = float(input("Enter rate: "))

    if h == 40:
        print("Regular time pay: " + str(h * r))
    elif h > 40:
        oth = h - 40
        otr = r * 1.5
        print("Overtime pay: " + str(40 * r + (oth * otr)))
    elif h < 40:
        print("Part time pay: " + str(h * r))
        
    return

computepay()