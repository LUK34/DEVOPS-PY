# Write a test case to test the billing system

"""
online food app
payment
user ==> food with cost of 250
distance is upto 3km ==> 0 delivery fee
distance 4 to 6 km ==> Rs 4 per km
distance 6 to 10 km ==> Rs 7 per km
distance is above 10 km ==> Rs 10 per km

"""

order =float(input("Enter cost of the food: "))
distance=float(input("Enter the distance: "))
totalFare=0.0
deliveryFee=0.0

if distance <= 3.0:
    totalFare = order + deliveryFee
elif distance <=6.0:
    deliveryFee=(distance-3)*4
    totalFare= order + deliveryFee
else:
    d1=distance-3
    d2=d1-6
    deliveryFee=(d1)*4 + (d2)*7
    totalFare= order + deliveryFee
print(totalFare)



