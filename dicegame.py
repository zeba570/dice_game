import random
import time

# ======================================
# 🎲 ULTIMATE DICE ROLLING GAME 🎲
# ======================================

print("=" * 50)
print("🎮 WELCOME TO THE ULTIMATE DICE GAME 🎮")
print("=" * 50)

player_name = input("Enter your name: ")

roll_count = 0
highest_score = 0
start_time = time.time()

# Lucky number feature
lucky_number = random.randint(2, 12)

print(f"\n🎯 Lucky Number for this game is: {lucky_number}")
print("If your dice total matches the lucky number, you win BONUS points!\n")

while True:

    choice = input("Roll the dice? (y/n): ").lower()

    if choice == 'y':

        # Rolling animation
        print("\n🎲 Rolling dice...", end=" ")
        time.sleep(1)

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        total = die1 + die2
        roll_count += 1

        print(f"\n✨ Dice Result: ({die1}, {die2})")
        print(f"📊 Total = {total}")

        # Score system
        if total > highest_score:
            highest_score = total

        # Special messages
        if die1 == die2:
            print("🔥 DOUBLE! Lucky roll!")

        if total == lucky_number:
            print("🎉 JACKPOT! You hit the lucky number!")

        if total == 12:
            print("👑 Maximum Roll!")

        elif total <= 3:
            print("😢 Tough luck!")

        print(f"🎯 Total Rolls: {roll_count}")
        print("-" * 40)

    elif choice == 'n':

        end_time = time.time()
        total_time = round(end_time - start_time, 2)

        print("\n🏁 GAME SUMMARY 🏁")
        print(f"👤 Player Name : {player_name}")
        print(f"🎲 Total Attempts/Rolls : {roll_count}")
        print(f"🏆 Highest Score : {highest_score}")
        print(f"⏱️ Time Played : {total_time} seconds")

        print("\n🙏 Thanks for playing!")
        break

    else:
        print("❌ Invalid choice! Please enter y or n.\n")