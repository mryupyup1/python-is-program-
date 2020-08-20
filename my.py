import pyttsx3 # importing pyttsx3 module
import os  # importing os module
while True: 

   pyttsx3.speak("what i can do for you")
   print("what i can do for you")
   p = input()

   if((("text editor" in p )or("notepad" in p))and (("open" in p )or("run" in p))): # for opening notepad 
     pyttsx3.speak("launching notepad")
     os.system("notepad")

   elif((("chrome" in p )or("browser" in p ))and(("start "in p)or("run" in p)or("launch" in p))): # for opening chrome web browser
      pyttsx3.speak("launching chrome")
      os.system("start chrome")  

   elif((("media" in p)and("player" in p))and(("start" in p )or("run" in p)or("launch" in p))): # for opening windows media player
       pyttsx3.speak("launching windows media payer")
       os.system("wmplayer")

   elif(("exit" in p)or("quit" in p)):    
       pyttsx3.speak("are you shure type yes") # for closing the current program
       print("are you shure type yes")
       k = input() # type yes if you are shure
       if("yes" in k):
          pyttsx3.speak("leaving this progam")
          break
       else:
          pyttsx3.speak("dont support") 
          print("dont support")

   elif(("date" in p)and(("tell" in p)or("todays" in p))): # to tell the today's date 
        from datetime import date
        a = date.today()
        pyttsx3.speak("todays date is ")
        pyttsx3.speak(a)      

   elif(("time" in p)and(("tell"in p)or("current" in p))): # to tell the current time
       import datetime 
       b= datetime.datetime.now()
       pyttsx3.speak("current time is") 
       pyttsx3.speak(b)

   elif (("calculator" in p)and(("open" in p)or("start" in p)or("execute"in p))): # for calculator
       pyttsx3.speak("launching calculator")
       os.system("calc")     

   else:
      pyttsx3.speak("dont support sorry") # dont suport your choice
      print("dont support sorry")


# end of program
