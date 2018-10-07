import webbrowser
import time
print("\n\n\nWell done! \nYou completed the Libary Escape Game!\n\n\n")
time.sleep(2)
print("""|@@@@|     |####|
|@@@@|     |####|
|@@@@|     |####|
\@@@@|     |####/
 \@@@|     |###/
  `@@|_____|##'
       (O)
    .-'''''-.
  .'  * * *  `.
 :  *       *  :
: ~   Libary ~  :
: ~   Escape ~  :
 :  *       *  :
  `.  * * *  .'
    `-.....-'\n\n\n""")
import sys
animation = "Thanks For Playing"

for i in range(18):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
time.sleep(5)
webbrowser.open("https://jam772.github.io/")
print("By James, Owen and Matthew")
