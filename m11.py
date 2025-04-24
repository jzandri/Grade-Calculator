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
    trainers, pakuri = read_data()
    winner = trainers[0]
    for t in trainers[1:]:
        if t.max_level > winner.max_level:
            winner = t
    with open("winner.txt", "w") as file:
        file.write(winner.name)
    with open("pakuri.txt", "w") as file:
        srted =  sorted(pakuri)
        for i in srted:
            file.write(i + "\n")

        file.write("\n".join(sorted(pakuri)))


if __name__ == "__main__":
    main()