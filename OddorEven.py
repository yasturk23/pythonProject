import time

Gameon = True
while Gameon:
    number = input('Choose an integer between 1 and 1000:')
    if number.isnumeric() and 0 < int(number) <= 1000:
        if int(number) % 2 == 0:
            print('The number is between 1 and 1000...')
            time.sleep(1)
            print('What an even number!')
            time.sleep(1)
        else:
            print('The number is between 1 and 1000...')
            time.sleep(1)
            print('Odd number!')
            time.sleep(1)
    else:
        print('Invalid input!')
        time.sleep(1)
