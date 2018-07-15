import time
import sys

def printOut(m):
    l = list(m)
    for i in range(0,len(l)):
        print(l[i],end='',flush=True)
        time.sleep(0.009)
    print()


def bedroom():    # Bedroom
    sleptIn = 0
    inBedroom = 1
    wearSuit = 0
    wearPajamas = 0
    wearDenim = 0
    wearNothing = 0
    windowOpen = 0
    while inBedroom == 1:
        time.sleep(2.5)
        printOut("\nYour options are...\nCloset    Bed    Window    Door\n")
        options = input()


    
        if options.upper() == "CLOSET":    # Bedroom Closet
            options = input("\nYou go over to your walk-in closet. Should you get dressed?\nYes    No\n")
                
            if options.upper() == "YES":
                options = input("\nWhat should you wear?\nSuit    Pajamas    Denim\n")
                
                if options.upper() == "SUIT":
                    printOut("\nYou're feeling fancy, so you put on your favorite suit and tie.")
                    wearSuit = 1
                    wearPajamas = 0
                    wearDenim = 0
                    wearNothing = 0
                    
                elif options.upper() == "DENIM":
                    printOut("\nYou're feeling lazy, so you put on some loose pajamas.")
                    wearSuit = 0
                    wearPajamas = 1
                    wearDenim = 0
                    wearNothing = 0
                    
                elif options.upper() == "DENIM":
                    printOut("\nYou're feeling ordinary, so you put on some jeans and a shirt.")
                    wearSuit = 0
                    wearPajamas = 0
                    wearDenim = 1
                    wearNothing = 0
                    
            elif options.upper() == "NO":
                    
                if wearSuit == 0 and wearPajamas == 0 and wearDenim == 0:
                    printOut("You walk out of the closet, wearing nothing but your underwear.")
                    wearNothing = 1
                    
                elif wearNothing == 0:
                    printOut("You walk out of the closet.")


                  
        elif options.upper() == "BED":    # Bedroom Bed
            options = input("\nYou go back to bed. Sleep?\nYes    No\n")

            if options.upper() == "YES":

                def sleeping():
                    time.sleep(2)
                    printOut(".")
                    time.sleep(0.7)
                    printOut(".")
                    time.sleep(0.7)
                    printOut(".\n")
                    time.sleep(1.5)

                if sleptIn == 0:
                    printOut("You go back to bed.")
                    sleeping()
                    printOut("You wake up a couple of hours later.")
                    sleptIn = 1
                    
                elif sleptIn == 1:
                    printOut("You lie in bed, but fail to fall asleep.")
                
                elif sleptIn == -1:
                    printOut("Despite refusing earlier, you decide to sleep. Just a little nap...")
                    sleeping()
                    printOut("You wake up a couple of hours later.")
                    sleptIn = 1
            elif options.upper() == "NO":
                
                if sleptIn == 0:
                    printOut("You probably shouldn't sleep, as tempting as it looks.")
                    sleptIn = -1
                elif sleptIn == 1:
                    printOut("You decide not to. You've already slept enough, better not waste time!")


                    
        elif options.upper() == "WINDOW":    # Bedroom Window
            options = input("\nYou walk to the window. Open it?\nYes    No\n")
            if options.upper() == "YES":
                if windowOpen == 0:
                    printOut("You decide to let the cool breeze in.")
                    windowOpen = 1

                elif windowOpen == 1:
                    options = input("The window is already open! Close it?\nYes    No")
                    
                    if options.upper() == "YES":
                        printOut("You close the window.")
                        windowOpen = -1
                        
                    elif options.upper() == "NO":
                        printOut("No, leave it open.")
                        windowOpen = 1
                        
                elif windowOpen == -1:
                    printOut("You change your mind, welcoming the breeze back in.")
                    windowOpen = 1
                
            elif options.upper() == "NO":
                printOut("Maybe not...")


                
        elif options.upper() == "DOOR":    # Bedroom Door
            options = input("Exit your room?\nYes    No\n")
            
            if options.upper() == "YES":
                printOut("ERROR: GAME NOT CODED.")
                exit(0)
                
            elif options.upper().lower == "NO":
                printOut("You take some more time to get ready for the day.")

bedroom()
 
