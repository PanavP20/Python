real_name=input("Enter your name: ") 
faviroute_gadget=input("Enter your faviroute gadget:")
print("My name is",real_name,"and my faviroute gadget is",faviroute_gadget)
agents_number=int(input("Enter your agent number"))
speed_rating=float(input("Enter your speed rating"))
mission_count=int(input("Enter your mission count"))
height=6.5
active_status=True
print("agents_number",type(agents_number),agents_number)
print("speed_rating",type(speed_rating),speed_rating)
print("mission_count",type(mission_count),mission_count)
print("height",type(height),height)
print("active_status",type(active_status),active_status)
#  typecasting
agents_number=str(agents_number)
speed_rating=str(speed_rating)
print("agents_number",type(agents_number),agents_number)
print("speed_rating",type(speed_rating),speed_rating)
secret_id=agents_number[0:5]+real_name[0:3]
print("secret_id",type(secret_id),secret_id)