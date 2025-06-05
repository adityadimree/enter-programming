def sum_all(*args):
    print(args)
    for variable in args:
        print(variable*3)
    return sum(args)

print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))
#so computer in args ko (ye jo multiple varibles hai) inhe as a tuple maan ke chalta hai (output dekho code ka, computer ne sbhi outputs- jo mene diye the- tuple ke form me print krke dediye...) or tuples to iterable hote hai.. as a result hamara loop kaam kiya...
#Along with that is sum keyword. Sum ko agar tum koi tuple ya fir koi list provide krr doge jiske andar sirf integers filled hai, to fir sum tumhe un sbhi ka sum calculate krr ke dedega.