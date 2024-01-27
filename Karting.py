def play_game(player1, player2, health1, health2, damage_A, damage_B, damage_C, rounds):
    score1, score2 = 0, 0

    for i in range(rounds):
        try:
            card1, card2 = input().split()

            damage1 = {'A': damage_A, 'B': damage_B, 'C': damage_C}[card1]
            damage2 = {'A': damage_A, 'B': damage_B, 'C': damage_C}[card2]

            if damage1 > damage2:
                score1 += 1
            elif damage2 > damage1:
                score2 += 1

            health2 -= damage1
            health1 -= damage2

        except ValueError as e:
            print("Invalid Command.")
            exit()

    return score1, health1, score2, health2


def main():
    try:
        player1, player2 = input().split()
        health1, health2 = input().split()
        health1 = int(health1)
        health2 = int(health2)
        damage_A, damage_B, damage_C = input().split()
        damage_A = int(damage_A)
        damage_B = int(damage_B)
        damage_C = int(damage_C)
        rounds = 3
    except ValueError as e:
        print("Invalid Command.")
        exit()

    score1, health1, score2, health2 = play_game(player1, player2, health1, health2, damage_A, damage_B, damage_C,
                                                 rounds)

    # Print results to terminal
    print(f"{player1} -> Score: {score1}, Health: {health1}")
    print(f"{player2} -> Score: {score2}, Health: {health2}")

    # Save results to result.txt file
    # with open("result.txt", "w") as f:
    #     f.write(f"{player1} -> Score: {score1}, Health: {health1}\n")
    #     f.write(f"{player2} -> Score: {score2}, Health: {health2}\n")


if __name__ == "__main__":
    main()
