import pyttsx3
import os

pyttsx3.speak("Welcome to Computer World")
pyttsx3.speak("How can I help you")
pyttsx3.speak("Tell me about your requirement")
while True:
       print("chat with me about your requirement: ",end='')
       y = input()

       

       if (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("chrome" in y) or ("Chrome" in y)):
        if (("do not" in y) or ("Do not" in y)  or ("dont" in y) or ("Dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("chrome")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("firefox" in y) or ("Firefox" in y) or ("mozilla" in y) or ("Mozilla" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("firefox")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("Internet" in y) or("internet" in y)) and (("Explore" in y) or ("explore" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("iexplore")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("camera" in y) or("Camera" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("start microsoft.windows.camera:")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("Calculator" in y) or("calc" in y) or ("CALCULATOR" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)): 
         print("Request Granted")
        else:
         os.system("calc")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("Store" in y) or("store" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("start ms-windows-store:")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("File" in y) or("file" in y)) and (("explorer" in y) or ("Explorer" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("explorer")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("Skype" in y) or("skype" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("lync")



       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("notepad" in y) or ("Notepad" in y) or ("edititor" in y) or ("Edititor" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("notepad")


       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("word" in y) or ("Word" in y)  or ("WORD" in y) or ("msword" in y) or ("MS Word" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("winword")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("access" in y) or ("Access" in y)  or ("ACCESS" in y) or ("msaccess" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("msaccess")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("powerpoint" in y) or ("Powerpoint" in y)  or ("POWERPOINT" in y) or ("ppt" in y) or ("PPT" in y) or ("mspowerpoint" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("powerpnt")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("excel" in y) or ("Excel" in y) or ("EXCEL" in y) or ("msexcel" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("excel")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("outlook" in y) or ("Outlook" in y) or ("OUTLOOK" in y) or ("msoutlook" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("outlook")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("onenote" in y) or ("Onenote" in y) or ("ONENOTE" in y) or ("msonenote" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("onenote")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("publisher" in y) or ("Publisher" in y) or ("PUBLISHER" in y) or ("mspublisher" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("mspub")


       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("vlc" in y) or ("VLC" in y)) and (("player" in y) or ("Player" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("vlc")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("windows" in y) or ("Windows" in y) or ("media" in y) or ("Media" in y)) and (("player" in y) or ("Player" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("wmplayer")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("Control" in y) or ("control" in y)) and (("Panel" in y) or ("panel" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("control panel")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("Adobe" in y) or ("adobe" in y) or ("Reader" in y) or ("reader" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("acrord32")

       elif (("run" in y) or ("launch" in y) or ("open" in y) or ("execute" in y)) and (("winrar" in y) or ("WinRar" in y) or ("WINRAR" in y)):
        if (("dont" in y) or ("not" in y) or ("Not" in y)):
         print("Request Granted")
        else:
         os.system("winrar")

       elif (("exit" in y) or ("Exit" in y) or ("terminate" in y) or ("Terminate" in y) or ("stop" in y) or ("Stop" in y) or ("close" in y) or ("Close" in y)):
         break

       else:
        print("Inavalid Request")

