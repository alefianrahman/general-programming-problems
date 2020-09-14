def zoo(total_head, total_legs, animal_legs=[2, 4]):
    """
    Find the number of kangaroo and tiger in a zoo.
    For example:

    zoo(6, 16) -> (4, 2)
    zoo(8, 20, [4, 2, 2]) -> (2, 0, 6)

    Parameters 
    ----------
    total_head: int 
                Total number of animals
    total_legs: int 
                Total number of animals'legs
    animal_legs: list 
                 A list of animal legs. The length of the list is either 2 or 3.

    Returns 
    -------
    tuple
        The number of animals in each animal type (based on the given 
        animal_legs). Return None if there is no solution.
    """
    animal_num = len(animal_legs)
    if animal_num == 2:
        animal_0_leg = animal_legs[0]
        animal_1_leg = animal_legs[1]

        for animal_0_num in range(total_head + 1):
            animal_1_num = total_head - animal_0_num
            animal_total_legs = animal_0_leg * animal_0_num \
                                + animal_1_leg * animal_1_num
            if animal_total_legs == total_legs:
                return animal_0_num, animal_1_num 
        return None, None
    elif animal_num == 3:
        animal_0_leg = animal_legs[0]
        animal_1_leg = animal_legs[1]        
        animal_2_leg = animal_legs[2]

        for animal_0_num in range(total_head + 1):
            for animal_1_num in range(total_head + 1 - animal_0_num):
                animal_2_num = total_head - animal_0_num - animal_1_num
                animal_total_legs = animal_0_leg * animal_0_num \
                                    + animal_1_leg * animal_1_num \
                                    + animal_2_leg * animal_2_num
                if animal_total_legs == total_legs:
                    return animal_0_num, animal_1_num, animal_2_num 
        return None, None, None 
    else:
        print("The allowed number of animal types is 2 or 3 only.")
