#GUESS THE NUMBER GAME
import random  

def get_range():  # get the range from the user
    while True:
        lower_range = int(input("Podaj dolny zakres: "))
        upper_range = int(input("Podaj górny zakres: "))
        if upper_range - lower_range <= 10:
            print("Zakres musi być większy niż 10. Spróbuj ponownie.")
            continue
        return lower_range, upper_range  # return the valid range

def guess_number(lower_range, upper_range):  # guessing game
    number = random.randint(lower_range, upper_range)  
    for attempt in range(1, 11):  # user has 10 attempts
        guess = int(input("Zgadnij liczbę: "))
        if guess == number:  # user guesses the number
            return attempt  
        elif guess < number:
            print("Za mało!")
        else:
            print("Za dużo!")
    return 10  # return 10 if the user didn't guess the number

def game():  # game function
    total_points = 0
    attempts_list = []
    best_score = 0

    print ("Gra zgadnij jaka liczba")

    for _ in iter(int, 1):  # game loop
        lower_range, upper_range = get_range() 
        attempt = guess_number(lower_range, upper_range)

        if attempt != 10:  # the user guessed the number
            print("Gratulacje! Zgadłeś liczbę!")
            points_for_game = (upper_range - lower_range) // attempt  # points for the game
            total_points += points_for_game  # add points to the total
            attempts_list.append(attempt) 
            if attempt < best_score or best_score == 0:  
                best_score = attempt  # update the best score
            print(f"Udało Ci się w {attempt} próbie. Zdobyłeś {points_for_game} punktów w tej grze.")

        continuation = input("Czy chcesz zagrać ponownie? (tak/nie) ")
        if continuation.lower() != "tak": 
            print(f"Twoja liczba punktów to: {total_points}")  
            print(f"Najlepszy wynik to: {best_score}")  
            break  # end the game

game()  # start the game