"""
distance is upto 5km, delivery charge is 0
above 5 km ==> 8% od order as delivery charge
"""

distance=float(input("Enter the distance: "))
order=float(input("Enter the order cost: "))
deliveryFee=0.0

if distance <= 5.0:
    fare=order+deliveryFee
else:
    deliveryFee=(8/100 * order)
    fare=order + deliveryFee
print(fare)