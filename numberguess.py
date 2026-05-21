import random
import time

# ======================================
# ADVANCED NUMBER GUESSING GAME
# ======================================

print("=" * 50)
print("🎮 WELCOME TO THE ULTIMATE NUMBER GUESSING GAME 🎮")
print("=" * 50)

player_name = input("Enter your name: ")

# Difficulty Levels
print("\nChoose Difficulty Level:")
print("1. Easy   (1 - 50)")
print("2. Medium (1 - 100)")
print("3. Hard   (1 - 200)")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    max_number = 50
elif choice == "2":
    max_number = 100
else:
    max_number = 200

number_to_guess = random.randint(1, max_number)

attempts = 0
start_time = time.time()

# Score System
score = 100

# Hint Feature
hint_used = False

print(f"\nHello {player_name}!")
print(f"Guess the secret number between 1 and {max_number}")
print("Type 'hint' if you want a hint (costs 10 points)")
print("Type 'exit' to quit the game\n")

while True:

    user_input = input("Enter your guess: ")

    # Exit Feature
    if user_input.lower() == "exit":
        print("\n🚪 Game Exited.")
        print(f"The number was {number_to_guess}")
        break

    # Hint Feature
    if user_input.lower() == "hint":
        if not hint_used:
            hint_used = True
            score -= 10

            if number_to_guess % 2 == 0:
                print("💡 Hint: The number is EVEN")
            else:
                print("💡 Hint: The number is ODD")
        else:
            print("⚠️ You already used your hint!")
        continue

    try:
        guess = int(user_input)
        attempts += 1

        # Score decreases with attempts
        score -= 2

        if guess < number_to_guess:
            print("📉 Too low! Try again.\n")

        elif guess > number_to_guess:
            print("📈 Too high! Try again.\n")

        else:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)

            print("\n🎉 CONGRATULATIONS 🎉")
            print(f"✅ You guessed the number {number_to_guess}")
            print(f"🧠 Total Attempts: {attempts}")
            print(f"⭐ Final Score: {score}")
            print(f"⏱️ Time Taken: {total_time} seconds")

            # Performance Message
            if attempts <= 3:
                print("🔥 Genius Level Guessing!")
            elif attempts <= 7:
                print("👏 Great Job!")
            else:
                print("🙂 Nice Try! Keep Practicing!")

            break

    except ValueError:
        print("❌ Please enter a valid number.\n")