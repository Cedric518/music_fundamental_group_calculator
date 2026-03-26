
from pizzas.utilities import greek_labels
# get greek labels according to the length needed


# check if each element has same length
def is_uniform(li):
    return all(len(li[0]) == len(t) for t in li) if li else True

# pi_1
def individual_pi_1(li, dim):
    if is_uniform:
        a_1=[]
        a_2=[]

        if li[-1] != li[0]:
            li.append(li[0])         # making sure start == end

        dimension = len(li[0])

        a_2.append(greek_labels(dimension))
        
        for i in range((len(li)-1)):
            for u in range(dimension):
                a_1.append((li[i+1][u] - li[i][u]) // dim)         # checks the n and n+1 element and store them in an array
            a_2.append(a_1)
            a_1 = []
            # store the strcutre generated into an 2 dimensional array
            # each element represents structure generated
            # for instance a_2[x][0] are all the betas, a_2[x][0] are all the alphas
        return a_2

# get total structure
# only take inputs after run by individual_pi_1
def total_pi_1(li):
    transposed = [list(row) for row in zip(*li)]
    for n, i in enumerate(transposed):
        transposed[n][1] = sum(i[1:])
        transposed[n] = transposed[n][0:2]
    return transposed

