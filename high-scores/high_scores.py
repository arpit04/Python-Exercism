def latest(scores):
    latest =  scores.pop()
    print(latest)

def personal_best(scores):
    personal_best = max(scores)
    print(personal_best)

def top_three(scores):
    top_three = sorted(scores)
    res = top_three.pop(),top_three.pop(),top_three.pop()
    print(res)

if __name__ == "__main__": 

    scores = [23, 43, 75, 97, 105, 45, 27]
    #function call
    latest(scores)
    personal_best(scores)
    top_three(scores)
