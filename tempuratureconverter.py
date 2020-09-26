"""
@author: micha

Temperature converter, pretty straightforward...
"""

fahrenheitTempurature = float(input("Enter a tempurature in Fahrenheit: "))

celciusTempurature = ((fahrenheitTempurature-32)*5)/(9)

if fahrenheitTempurature<-500:
    print("Input out of range (-500 deg. F to 500 deg. F)")
elif fahrenheitTempurature>500:
    print("Input out of range (-500 deg. F to 500 deg. F)")
else:
    print(str('%.2f' % fahrenheitTempurature) + " degrees F is " +str('%.2f' % celciusTempurature) + " degrees C")
