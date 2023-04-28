cost_ground = 0
cost_ground_premium = 125.00
cost_drone = 0

weight = 41.5

#Ground shipping

if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
elif weight >= 11:
  cost_ground = weight * 4.75 + 20

print(cost_ground)
print(cost_ground_premium)
 
#Drone shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
elif weight >= 11:
  cost_drone = weight * 14.25

print("Cost of ground shipping: " + str(cost_ground))
print("Cost of premium shipping: " + str(cost_ground_premium))
print("Cost of drone shipping " + str(cost_drone))
