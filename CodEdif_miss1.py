# Function to find missing values in a sequencial coded field
def findmisscode(L):
    Lint = [int(i) for i in L]
    Lint.sort()
    Lmiss = [i for i in range(1, len(Lint)+1) if i not in Lint]
    return Lmiss

# print(findmisscode(L))
