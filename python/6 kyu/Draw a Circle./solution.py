def circle(radius):
    result = ""
    for i in range(radius*2-1) :
        for j in range(radius*2-1) :
            if (i-radius+1)**2+(j-radius+1)**2 >= radius**2 :
                result += " "
            else :
                result += "#"
        result += "\n"
    if radius == 0 :
        return "\n"
    return result

# print circle(1)
print circle(10)
