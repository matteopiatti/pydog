from pydog import setup_game, step
from agent.cli import render
from agent.humanagent import HumanAgent


def main():
    agents = [
        HumanAgent(),
        HumanAgent(),
        HumanAgent(),
        HumanAgent(),
    ]
    rules = {
        "include_split": False,
        "include_swap": False,
        "include_switch_team_cards": False,
    }
    state = setup_game(num_players=4, agents=agents, rules=rules)
    while not state.finished:
        render(state)
        step(state)

    if state.finished:
        render(state)
        print(f"Game over! The winning team is: {state.winner}")


if __name__ == "__main__":
    main()
