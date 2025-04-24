class Trainer:
    def __init__(self, name, max_level):
        self.name = name
        self.max_level = max_level

def read_data():
    seeeeeeeeet = set()
    trainers = []
    with open("contest.txt", "r") as file:
        for line in file:
            mx = -1
            trainer, *pakuris = line.split(",")
            for pakuri in pakuris:
                name, level = pakuri.split("-")
                level = int(level)
                seeeeeeeeet.add(name)
                if level >= mx:
                    mx = level
            trainers.append(Trainer(trainer, mx))
    return trainers, seeeeeeeeet

def main():
    t, p = read_data()
    winner = t[0]
    for i in t[1:]:
        if i.max_level > winner.max_level:
            winner = i
    with open("winner.txt", "w") as file:
        file.write(winner.name)
    with open("pakuri.txt", "w") as file:
        srted =  sorted(p)
        for i in srted:
            file.write(i + "\n")


if __name__ == "__main__":
    main()