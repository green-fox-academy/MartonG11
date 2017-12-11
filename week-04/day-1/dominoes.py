# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...


from domino import Domino

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()

def sort(dominoes_list):
    new_dominoes = []
    new_dominoes.append(dominoes[0])
    while (not len(new_dominoes) == len(dominoes_list)):
        for same in range(len(dominoes)):
            if dominoes[same].values[0] == new_dominoes[- 1].values[1]:
                new_dominoes.append(dominoes[same])
    return new_dominoes


print(sort(dominoes))
