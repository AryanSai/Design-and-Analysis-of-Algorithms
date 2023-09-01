# the higher the number the better they are for the role
import random


def shuffle(number_list, n):
    random_numbers = random.sample(range(0, n**3), n)
    zipped_list = dict(zip(number_list, random_numbers))
    sortlist = sorted(zipped_list, key=lambda i: zipped_list[i])
    return sortlist


def hire(current_candidate, candidate_list):
    # interview cost is a must and lower than hiring cost. It is a constant for all the candidates
    total_cost = 0
    interview_cost = 50
    hiring_cost = 100
    for new_candidate in candidate_list:
        # conduct interview
        total_cost += interview_cost
        if new_candidate > current_candidate:
            # hire new_candidate if better than current
            total_cost += hiring_cost
            current_candidate = new_candidate
    return current_candidate, total_cost


n = 20

# the agency gives us the list of candiates in ascending order of skill
number_list = [i for i in range(1, n + 1)]
# we need to randomise the list to reduce the cost
candidate_list = shuffle(number_list, n)
print(candidate_list)

current_candidate = 0
the_best_candidate, total_cost = hire(current_candidate, candidate_list)
print("The best candidate is {}".format(the_best_candidate))
print("The total amount paid to the agency is {}".format(total_cost))
