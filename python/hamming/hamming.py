def distance(strand_a, strand_b):
    distance = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are of two different lengths")
    else:
        for index in range(len(strand_a)):
            if strand_a[index] != strand_b[index]:
                distance += 1
    return distance

#strand_a = 'ABCDABCDABCDABCD'
#strand_b = 'DBCAABADACCDDBCD'
#5 diffs     ^  ^  ^  ^  ^

