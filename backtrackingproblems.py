def is_valid_state(state):
    # check if it is a valid solution
    return True

# Candidate function finds the list of cnadidates that can be used to construct the next function

def get_candidates(state):
    return []

# Searching the state recursive
# we make deep copy of the state to make continous improvements

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # we exhaust all valid solution
        # if we need only one valid solution we will just return here
        # return

    # if the state is not a valid solution then we find candidates
    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)

def solve(): # this is the entry problwm to our program
    solutions = []
    state = set()
    search(state, solutions)
    return solutions