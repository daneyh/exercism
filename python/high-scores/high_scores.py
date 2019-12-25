def latest(scores):
   return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three = []
    while len(top_three) < 3 and len(scores) > 0:
        top_three.append(max(scores))
        scores.remove(max(scores))
        
    return top_three
