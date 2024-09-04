print('''
*******************************************************************************
                     .^.,*.
                    (   )  )
                   .~       "-._   _.-'-*'-*'-*'-*'-'-.--._
                 /'             `"'                        `.
               _/'                                           `.
          __,""                                                ).--.
       .-'       `._.'                                          .--.\
      '                                                         )   \`:
     ;                                                          ;    "
    :                                                           )
    | 8                                                        ;
     =                  )                                     .
      \                .                                    .'
       `.            ~  \                                .-'
         `-._ _ _ . '    `.          ._        _        |
                           |        /  `"-*--*' |       |  mb
                           |        |           |       :
 ~~~~~~~---   ~-~-~-~   -~-~-~-~-~-~~~~~~  ~~~~  ~-~-~-~-~-~-~-
------~~~~~~~~~----------~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
 ~~~~~~~~~   ~~~~~~~~~       ~~~~~~~   ~~~~~~~~~  ~~~~~~~~~~~~~~~
*******************************************************************************
''')
print("Welcome to Jumanji! Oh... no wrong game baby.")
print("Your mission is to... what was your mission now?") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_choice = input("You're lying naked at a crossroads, between rocky mountains and red sands. Do you want to go left or right? ")
if first_choice.lower() == "left":
          print("By effect you chose to die... a gigantic pidegon appears. You die. Gnam")
          print("But in that moment, a young lady approach you. She is young and... probably stupid. \nShe offers you a ride to the treasure island. You accept. You get in the car and drive to Las Vegas.") 
          print(f"You are now in the middle of the desert. \nYou have no idea how to get to Las Vegase.")
          second_choice = input("Do you want to walk or drive? ")
          if input("Do you want to go left or right? ").lower() == "drive":
                    print(f"She says: 'Look! That's the city! Goodbye idiot!")
          else:
                    print ("Oh no, you are dead. You are dead. You are dead. You...")
elif first_choice.lower() == "right":
          print ("A jolly pink desert hippo appears and eats you. You are somehow alive")
          

