smallInt2Hex = {
    0:  "0",
    1:  "1",
    2:  "2",
    3:  "3",
    4:  "4",
    5:  "5",
    6:  "6",
    7:  "7",
    8:  "8",
    9:  "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}


def rgb(r, g, b):
    result = ""
    rgb = [ 0 if r < 0 else 255 if r > 255 else r,
            0 if g < 0 else 255 if g > 255 else g,
            0 if b < 0 else 255 if b > 255 else b]
    for value in rgb :
        result += smallInt2Hex[int(value / 16)]+smallInt2Hex[value % 16]
    return result

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

testing(rgb(0,0,0),"000000")
testing(rgb(1,2,3),"010203")
testing(rgb(255,255,300), "FFFFFF")
testing(rgb(254,253,252), "FEFDFC")
testing(rgb(-20,275,125), "00FF7D")