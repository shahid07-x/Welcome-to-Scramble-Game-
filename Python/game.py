import random
import time

def run_scramble_game():
    # Expanded list to 20 words
    word_list = [
        "python", "github", "data", "excel", "tableau", "analytics", 
        "coding", "science", "project", "resume", "learning", "design", 
        "student", "skills", "forage", "report", "digital", "market", 
        "success", "binary"
    ]
    
    print("--- Welcome to the Word Scramble Game! ---")
    time.sleep(1)
    
    while True:
        secret_word = random.choice(word_list)
        
        word_as_list = list(secret_word)
        random.shuffle(word_as_list)
        scrambled_word = "".join(word_as_list)

        print(f"\nYour scrambled word is: {scrambled_word.upper()}")
        print("Try to guess the original word!")

        attempts = 0
        max_attempts = 3
        
        while attempts < max_attempts:
            user_guess = input(f"Guess ({attempts + 1}/{max_attempts}): ").strip().lower()
            attempts += 1
            
            if user_guess == secret_word:
                # Happy Emoji when you win
                print(f"\n🎉 *** CORRECT! You unscrambled '{secret_word}'! 😊 *** 🎉")
                break
            elif attempts == max_attempts:
                # Sad Emoji when you lose (run out of attempts)
                print(f"\n😔 Out of attempts! The correct word was: {secret_word} 😭")
            else:
                print("Incorrect. Try again.")

        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    run_scramble_game()