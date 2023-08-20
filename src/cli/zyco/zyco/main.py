import random
import sys
import inquirer
import time
import pyfiglet
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Zyco's Assistant Sir. Game is Under Development by Awesome Developer Abhisar , Thankyou")


def guess():
    previous_guess = 0
    current_guess = 0
    attempt = 1
    number = random.randint(11, 90)
    while True:
        try:
            current_guess = int(input('Enter Your Guess : '))
        except ValueError:
            print('Enter Int Only!')
            continue
        if 0 > current_guess or current_guess > 100:
            print('Invalid Guess')
            continue
        if current_guess == number:
            print(pyfiglet.figlet_format(f'CORRECT!'))
            print(f'Attempts: {attempt}')
            break
        if not previous_guess:
            if number + 10 > current_guess > number - 10:
                print('Warm')
            else:
                print('Cold')
            attempt += 1
        else:
            if abs(previous_guess - number) > abs(current_guess - number):
                print('Warmer')
            else:
                print('Colder')
            attempt += 1
        previous_guess = current_guess


def main():
    try:
        if sys.argv[1] == '--run':
            print(pyfiglet.figlet_format('Powered By ZYCO!'))
            unit = inquirer.list_input("Which Game you wanna play?", choices=['Guess Game', 'Wish Game'])
            if unit == 'Guess Game':
                time.sleep(1)
                guess()
            if unit == 'Wish Game':
                wishMe()
            print(pyfiglet.figlet_format('Bbye'))
    except Exception:
        print('Example: \n\t python main.py --run')


if __name__ == '__main__':
    main()
