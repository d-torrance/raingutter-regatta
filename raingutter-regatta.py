import double_elimination
import sys

class Regatta:
    def __init__(self, participant_file):
        with open(participant_file) as f:
            participants = [line.strip() for line in f]
        self.tournament = double_elimination.Tournament(participants)

    def print_bracket(self):
        print("Current bracket")
        print("---------------")
        for match in self.tournament.get_matches():
            (left, right) = tuple(match.get_participants())
            match_info = f"{left.get_competitor()} v. {right.get_competitor()}"
            winner = match.get_winner_participant().get_competitor()
            if winner != None:
                match_info += f" -> {winner}"
            print(match_info)
        print()


    def run_match(self, match):
        (left, right) = tuple(match.get_participants())
        participants = {
            "a" : left.get_competitor(),
            "b" : right.get_competitor()}
        print(f"(a) {participants['a']}")
        print(f"(b) {participants['b']}\n")
        sure = "n"
        while sure != "y":
            winner = ""
            while not(winner == 'a' or winner == 'b'):
                winner = input("Winner? (a/b): ")
            print(f"The winner is {participants[winner]}.")
            sure = input("Is this correct? (y/n) ")
        match.set_winner(participants[winner])

    def run_tournament(self):
        print("Beginning the Raingutter Regatta!")
        print("=================================\n")
        round = 1
        while len(self.tournament.get_active_matches()) > 0:
            self.print_bracket()
            print(f"Round {round}")
            print((len(str(round)) + 6) * '-')
            current_match = self.tournament.get_active_matches()[0]
            self.run_match(current_match)
            round += 1
            print()
        print("Winners")
        print("-------")
        print(f"1. {self.tournament.get_matches()[-1].get_winner_participant().get_competitor()}")
        print(f"2. {self.tournament.get_matches()[-1].get_loser_participant().get_competitor()}")
        print(f"3. {self.tournament.get_matches()[-2].get_loser_participant().get_competitor()}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("expected a single filename")
    regatta = Regatta(sys.argv[1])
    regatta.run_tournament()
