import canvas


def draw_map():
    canvas.set_stroke_color(1,1,1)
    canvas.set_size(200,200)
    canvas.draw_rect(40,100,40,40)
    canvas.draw_rect(120,100,40,40)
    for i in range(4):
        canvas.draw_rect(80,20+40*i,40,40)

def main():
    
    living_room()

def map_location(w,s):
    canvas.draw_text("👨‍🦳",w,s) 

def living_room ():  
    draw_map()  
    X = 1 #Creating an infinite loop
    while X == 1:
        map_location(90,150)
        a =  input("You are at the living room, where do you want to go? (you can go south)")
        if a == "south":
            canvas.clear()
            kitchen()
        else:
            print ("You need to choose another direction")
            

def kitchen (): #Different functions for each room
    draw_map()
    x=1
    while x == 1:
        map_location(90,110)
        a = input("You are at the kitchen, where would you like to go? (You can go east, west, or south)") #letting the user type where they would like to go
        if a == "north":
            canvas.clear()
            living_room()
        elif a == "east":
            canvas.clear()
            Pantry() 
        elif a == "west": # ELif statement needed because multiple places user can go
            canvas.clear()
            Dining_Room()
        elif a == "south":
            canvas.clear()
            MovRoom()
        else:
            print("Ouch, try again")
        
def MovRoom ():
    draw_map()
    x=1
    while x == 1:
        map_location(90,70)
        a = input("You are at the Movie Room, where would you like to go? (You can go south or north)")
        if a == "south":
            canvas.clear()
            garage()
        elif a == "north":
            canvas.clear()
            kitchen()
        else:
            print("Ouch, try again")
    
def garage ():
    draw_map()
    x=1
    canvas.draw_text("🚗",90,20) #This is the hidden surprise that appears after you get into the garage
    while x == 1:
        map_location(90,40)
        print("You now have found this fast red car!")
        a = input("You are at the Garage, where would you like to go? (you can go north)")
        if a == "north":
            canvas.clear()
            MovRoom()
        else:
            print("Ouch, try again")
    
    

def Pantry():
    draw_map()
    x=1
    while x == 1:
        map_location(130,110)
        a = input("You are  in the Pantry room, Which direction would you like to go (you can go west)")
        if a == "west":
            canvas.clear()
            kitchen()
        else:
            print("Can't you see there's a wall there")

    
def Dining_Room ():
    draw_map()
    x=1
    while x == 1:
        map_location(50,110)
        a = input("You are  in the dining room, Which direction would you like to go (you can go east)")
        if a == "east":
            canvas.clear()
            kitchen()
        else:
            print("Choose another direction, you are running into a wall")
  
    
main()
