import pdb
with open(r"/home/kestrel/Documents/Coding/AdventOfCode/2024/day1/data.txt") as file:
    data = file.readlines()

def remove_line_break_char(data):
    data = [d[:-1] for d in data]
    return data

clean_data = remove_line_break_char(data)


# data = ['12823   12823\n', '74540   88907\n', '37687   50218\n', '83750   57255\n', '43380   59171\n']

def get_lists(data):
    left = []
    right = []

    for d in data:
        left.append(int(d.split(' ')[0]))
        right.append(int(d.split(' ')[3]))
    return(sorted(left), sorted(right))



def get_distance(data):
    distance = 0
    i = 0

    while i < len(data[0]):    
        distance += abs(data[0][i] - data[1][i])
        i+=1
    return distance

# print(get_distance(get_lists(clean_data)))


def get_similarity_score(tuple):

    score = 0

    for x in tuple[0]:
        j = 0
        for y in tuple[1]:
            if x == y:
                j+=1
        score+=(x * j)

    print(score)

get_similarity_score(get_lists(clean_data))


 

