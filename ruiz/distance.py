the_number = 5
tries = 1
distance_precedente = 100
# guessing loop
while True:
    guess = int(input(' say a number between 1 and 10:'))

    if guess == the_number:
        print("you guessed it, the number was", the_number)
        print(" it only took you", tries, "tries")
        tries += 1
        break
    else:
        distance_courante = abs(guess - the_number)  # distance to the_number
        if distance_courante < distance_precedente:
            print('vous chaufez')
        else:
            print('vous etes froid')

        distance_precedente = distance_courante
        tries += 1