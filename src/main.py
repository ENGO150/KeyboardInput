import pyautogui
import time
import sys

def main():
    text = ""
    times = 0
    wait = 0;

    # Get text
    if not len(sys.argv) > 1:
        text = input("What do you want to type?\n>>> ")
    else:
        for i in range(0, len(sys.argv)):
            if i != 0:
                text += sys.argv[i] + " "

        text = text[0:len(text) - 1] # Remove space (last letter)

    #Get times
    times = int(input("\nHow many times do you want to type that?\n>>> "))

    #Get wait
    wait = int(input("\nHow much do you want to wait between sending? (Miliseconds)\n>>> ")) / 1000

    for i in range(0, times):
        time.sleep(wait) # Wait

        pyautogui.write(text)
        pyautogui.press("enter") # ENTER

        print("Done: " + str(i + 1))

    input()

if __name__ == "__main__":
    main() # Run
