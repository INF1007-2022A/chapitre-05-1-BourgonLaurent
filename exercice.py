#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = -number

    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = "JKLMNOPQ", "ack"

    return [p + suffixe for p in prefixes]


def prime_integer_summation() -> int:
    n = 0
    i = 0
    prime_sum = 0
    current_num = 2
    while n < 100:
        max_multiple = math.floor(math.sqrt(current_num)) + 1
        for i in range(max_multiple + 1):
            if i in (0, 1):
                continue
            if current_num % i == 0:
                break

        if i == max_multiple:
            prime_sum += current_num
            n += 1

        current_num += 1
    return prime_sum


# Utilise un générateur pour sauver
# de la place dans la mémoire et
# du temps de calcul
def fact_gen():
    accumulation = 1
    nombre = 1
    while True:
        accumulation *= nombre
        nombre += 1
        yield accumulation


def factorial(number: int) -> int:
    gen = fact_gen()
    for _ in range(1, number + 1):
        fact = next(gen)

    return fact


def use_continue() -> None:
    for num in range(1, 10 + 1):
        if num == 5:
            continue

        print(num)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    group_list: List[bool] = []
    for group in groups:
        ## Critère de taille
        # Si le groupe possède plus que 10 membres
        # ou 3 membres et moins, il n'est pas acceptable
        if not (3 <= len(group) <= 10):
            group_list.append(False)

        ## Critère d'âge
        # Si au moins un membre du groupe à exactement 25 ans,
        # alors le groupe est acceptable peut-importe les autres critères d'âges
        elif 25 in group:
            group_list.append(True)
        ## Critère d'âge
        # Si au moins un membre du groupe est mineur,
        # le groupe n'est pas acceptable
        elif any(age < 18 for age in group):
            group_list.append(False)

        ## Critère d'âge
        # Si un membre du groupe est plus vieux que 70 ans
        # et qu'un autre membre du groupe à exactement 50 ans,
        # le groupe n'est pas acceptable
        elif any(age > 70 for age in group) and any(age == 50 for age in group):
            group_list.append(False)

        else:
            group_list.append(True)

    return group_list


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72],
        [18, 24, 22, 50, 70],
        [25, 2],
        [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20],
        [70, 50, 26, 28],
        [75, 50, 18, 25],
        [13, 25, 80, 15],
        [20, 30, 40, 50, 60],
        [75, 50, 100, 28],
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == "__main__":
    main()
