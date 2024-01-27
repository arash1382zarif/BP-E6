def play_round(card1, card2, damage_a, damage_b, damage_c):
    damage1 = {'A': damage_a, 'B': damage_b, 'C': damage_c}.get(card1, 0)
    damage2 = {'A': damage_a, 'B': damage_b, 'C': damage_c}.get(card2, 0)

    return damage1, damage2


def play_game(health1, health2, damage_a, damage_b, damage_c, rounds):
    score1, score2 = 0, 0

    for _ in range(rounds):
        try:
            card1, card2 = input().split()
            damage1, damage2 = play_round(card1, card2, damage_a, damage_b, damage_c)

            if damage1 > damage2:
                score1 += 1
            elif damage2 > damage1:
                score2 += 1

            health2 -= damage1
            health1 -= damage2

        except ValueError:
            print("Invalid Command.")
            exit()

    return score1, health1, score2, health2


def main():
    try:
        player1, player2 = input().split()
        health1, health2 = map(int, input().split())
        damage_a, damage_b, damage_c = map(int, input().split())
        rounds = 3
    except ValueError:
        print("Invalid Command.")
        exit()

    score1, health1, score2, health2 = play_game(health1, health2, damage_a, damage_b, damage_c, rounds)

    # Print results to terminal
    print(f"{player1} -> Score: {score1}, Health: {health1}")
    print(f"{player2} -> Score: {score2}, Health: {health2}")

    # Save results to result.txt file
    # with open("result.txt", "w") as f:
    #     f.write(f"{player1} -> Score: {score1}, Health: {health1}\n")
    #     f.write(f"{player2} -> Score: {score2}, Health: {health2}\n")


if __name__ == "__main__":
    main()
