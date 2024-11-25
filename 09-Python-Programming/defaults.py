
def jump(age, weight=100):
    print("age:", age, "weight:", weight)
  

def hop(age=50, weight=200, country="canada"): 
    print("age:", age, "weight:", weight, "country:", country)


print("jump calls...")
jump(26)  #should use default weight
jump(45, 63)

#try this
#jump(weight=34)


print("\nhop calls...")
hop()
hop(56, 24)

hop(country="brazil", weight=999, age=99)

#try this
#hop(country="brazil", 45)