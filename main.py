from Game import Game

ECOSYSTEM = {
    (2, 2),
    (1, 2),
    (0, 2),
    (2, 1),
    (9, 9),
    (8, 9),
    (9, 8),
    (8, 10),
    (9, 10),
    (10, 10),
    (10, 9),
    (10, 8)
}

def main():
    game = Game(20, 20, ECOSYSTEM)
    print(game)

if __name__ == '__main__':
    main()