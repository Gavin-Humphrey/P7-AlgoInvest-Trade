import csv
from dataclasses import dataclass
from time import perf_counter
import time



 
start_time = time.time()

@dataclass(frozen=True)
class Action:
    """Represents an action"""
    name: str
    cost: float
    percent: float
    
    @property
    def profit(self) -> float:
        """Compute a return profit from cost and percent"""
        return self.cost * self.percent / 100

    def __str__(self):
        return f"{self.name} | cost: {self.cost}€ | percent: {self.percent}% | profit: {self.profit:.2f}€"

    def __lt__(self, other_action: "Action"):
        """Allows to sort list of Action on percent profit"""
        return self.percent < other_action.percent
        

def performance(func):
    """Monitor process time for a function"""

    def wrapper(*args, **kawrgs):
        t1 = perf_counter()
        result = func(*args, **kawrgs)
        t2 = perf_counter()
        print(f"\nThe function {func.__name__} took {round(t2 - t1, 5)} s")
        return result

    return wrapper

@performance
def get_actions_objects_from_csv(file_name: str) -> list[Action]:
    """Return a list of Action object from a csv file"""
    actions = []
    with open(file_name, newline="") as csv_File:
        reader = csv.reader(csv_File, delimiter=",")
        for row in reader:
            cost = float(row[1])
            percent = float(row[2])
            if cost <= 0.0 or percent <= 0:
                continue

            action = Action(row[0], cost, percent)
            actions.append(action)

    return actions

@performance
def best_cost_profit(actions: list[Action]):
    """Returns the best actions with total invest and total profit"""
    actions.sort(reverse=True)
    max_invest = 500
    total_profit: float = 0
    total_invest: float = 0
    best_actions = []

    for action in actions:
        if action.cost <= max_invest:
            max_invest -= action.cost
            total_invest += action.cost
            total_profit += action.profit
            best_actions.append(action)

    return best_actions, total_invest, total_profit


def main():

    actions = get_actions_objects_from_csv("data/dataset2.csv")
    best_actions, invest, profit = best_cost_profit(actions)
    print("")
    print(f"Computed {len(actions)} Shares")
    print("")
    print(f"Total Invest: {invest:.2f}€\nTotal Profit: {profit:.2f}€\nN° Of Most Profitable Shares: {len(best_actions)}")
    print("")
    for action in best_actions:
        print(action)

    print("\nTime elapsed : ", time.time() - start_time, "seconds\n")


if __name__ == '__main__':
   main()
