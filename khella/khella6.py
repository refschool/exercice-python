k=2

def occurrence_kmer(seq,k):
    dico = {}
    i=0

    while(i < len(seq) - k +1):
        current_mer = seq[i:i+k]
        if current_mer in dico:
            dico[current_mer] += 1
        else:
            dico[current_mer] = 1
        i=i+1
    return dico

def frequence_kmer(dico,n):
    for key in dico:
        dico[key] = dico[key] / n
    return dico

def signature(seq,k):
    dico = occurrence_kmer(seq,k)
    n = len(seq) - k + 1
    dico = frequence_kmer(dico,n)
    return dico

def distance_signature(sig1,sig2):
    kdistance = 0
    for key in sig1:
        value1 = sig1[key]
        if(key in sig2):
            value2 = sig2[key]
        else:
            value2 = 0
        kdistance = kdistance + ((value1 - value2) ** 2)

    for key in sig2:
        value2 = sig2[key]
        if(key not in sig1):
            kdistance = kdistance + ((value2) ** 2)
    return kdistance


def distance_sequence(seq1,seq2,k):
    sig1 = signature(seq1,k)
    sig2 = signature(seq2,k)
    return distance_signature(sig1,sig2)

print(distance_sequence("ATC","AGC",2))