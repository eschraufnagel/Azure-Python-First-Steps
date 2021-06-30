print('What is the temperature in farenheit?')
farenheit = input()

if farenheit.isnumeric() == False:
    print('Input is not a number')
    exit()

farenheit = int(farenheit)

celsius = round((farenheit - 32) * (5 / 9), 1)

print('Temperature in celsius is ' + str(celsius))