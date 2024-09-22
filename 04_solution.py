#Functions ko define krte waqt ek syntax hota hai, ki return ke baad function execute hota hi nhi hai, mtlb function define krte samay jo bhi action krana hai vo return use krne se pehle hi kara dena uske baad mt krana.
#The round method... print any large decimal number upto any place of deciaml you want. round(number, place of decimal upto which you want to print it)
#if you want to round off a large deicmal value upto n deciaml values you can use the fromat method(syntax thoda intresting hai.). Then you can print it by assigning it to a variable.
#>>> "{:.3f}".format(9.99999999)
#'10.000'
#>>> formatted = "{:.5f}".format(9.999875698989)
#>>> print(formatted)
#9.99988
#>>> formatted = "{:.7f}".format(9.999875698989)
#>>> print(formatted)
#9.9998757
import math
def circle(radius):
    return {"Circumference":round(radius*math.pi*2, 2), "Area": round(radius**2*math.pi, 2)}
print(circle(2))