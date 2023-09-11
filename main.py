import random

def play_game():
    green_areas = [1, 2]  # Two green areas
    total_areas = 100
    red_black_ratio = (total_areas - len(green_areas)) // 2
    bot_chips = 1000
    min_bet = 100
    games_to_play = 1

    bot_total_wins = 0
    bot_total_losses = 0
    bot_chips_won = 0
    bot_chips_lost = 0

    while bot_chips >= min_bet and bot_total_wins < games_to_play:
        current_game = 1
        bot_bet = min(bot_chips, min_bet)

        while current_game <= games_to_play:
            # Determine the outcome
            outcome = random.randint(1, total_areas)
            if outcome in green_areas:
                result = "green"
            elif outcome <= red_black_ratio:
                result = "black"
            else:
                result = "red"

            if result == "black":
                bot_chips += bot_bet
                bot_bet = min(bot_chips, min_bet)  # Reset bet amount after a win
                bot_chips_won += bot_bet
                bot_total_wins += 1
                break
            else:
                bot_chips_lost += bot_bet
                bot_chips -= bot_bet
                bot_bet *= 2  # Double the bet after a loss

                if bot_chips < bot_bet:
                    # If the bot doesn't have enough chips to double the bet, set the bet to remaining chips
                    bot_bet = bot_chips

            current_game += 1

        bot_total_losses = games_to_play - bot_total_wins

    print(f"Bot's Total Wins: {bot_total_wins}")
    print(f"Bot's Total Losses: {bot_total_losses}")
    print(f"Winning Percentage: {bot_total_wins / games_to_play * 100:.2f}%")
    print(f"Losing Percentage: {bot_total_losses / games_to_play * 100:.2f}%")
    print(f"Bot's Total Chips Won: {bot_chips_won}")
    if bot_total_losses == games_to_play:
        print(f"Bot's Total Chips Lost: {bot_chips_lost}")
    else:
        print("Bot won all games. No chips lost.")

if __name__ == "__main__":
    play_game()
