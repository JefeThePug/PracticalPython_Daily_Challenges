#Challenge 42: Spelling Checker
from textblob import TextBlob
def spelling_checker():
    again = False
    while True:
        word = input(f'Enter {("a","the")[again]} word{(""," again")[again]}: ')
        suggestion = TextBlob(word).correct()
        if word == suggestion: 
            return word
        if input(f'Did you mean {suggestion}? (Y/N) ').upper() == 'Y':
            return suggestion
        again = True
        print('Try again...')

print(spelling_checker())


#Extra Challenge: Create an Alarm Clock
from playsound import playsound
from datetime import datetime

def alarm():
    hour = input("Please enter the hour for your alarm: ")
    minute = input("Please enter minute for your alarm: ")
    print(f'You have set alarm for {hour}:{minute}.')
    return f'{hour}:{minute}'

alarm_time = alarm()
alarm = 'alarm.wav'

#################################################################
# ! Potential to run a long time depending on when alarm is set.#
# For the purposes of this challenge only and not intended for  #
# actual use as an alarm clock. Only test with a time that is   # 
# one or two minutes away from the current time.                #
#################################################################

while True: 
    t = datetime.now().strftime('%H:%M')
    if alarm_time == t:
        playsound(alarm)
        break
