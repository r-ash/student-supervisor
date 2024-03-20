import random
from matching.games import HospitalResident

def allocate_students(student_prefs, supervisor_capacity):
    ## TODO: Clean student prefs
    ## Clean supervisor prefs (remove those with 0? allocations?)

    ## Supervisor to project mappings
    supervisor_to_capacity = {
        name: capacity for _, (name, capacity) in supervisor_capacity.iterrows()}

    ## Build student prefs
    supervisor_names = supervisor_capacity["name"].values

    student_to_preferences = {}
    for _, (student, *prefs) in student_prefs.iterrows():
        student_preferences = []
        for supervisor in prefs:
            if supervisor in supervisor_names and \
                    supervisor not in student_preferences:
                student_preferences.append(supervisor)

        if student_preferences:
            student_to_preferences[student] = student_preferences

    ## Supervisor preferences
    ## Note we could sort them based on some ranking
    ## or who submitted their preferences first!
    ## For now we will go with a random rank
    student_ranks = list(student_to_preferences.keys())
    random.seed(10)
    random.shuffle(student_ranks)
    supervisor_to_preferences = {supervisor: student_ranks
                                 for supervisor in supervisor_names}

    game = HospitalResident.create_from_dictionaries(
        student_to_preferences,
        supervisor_to_preferences,
        supervisor_to_capacity
    )

    return game.solve(optimal="resident")
