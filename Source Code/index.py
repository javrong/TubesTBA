def check_token(token):
    switcher = {
        "p": 1,
        "q" : 1,
        "r" : 1,
        "s" : 1,
        "not" : 2,
        "and" : 3,
        "or" : 4,
        "xor" : 5,
        "if" : 6,
        "then" : 7,
        "iff" : 8,
        "(" : 9,
        ")" : 10 
    }

    return switcher.get(token, "error")


def validation(tokenLexic):
    numThen = 0
    numKurung = 0
    i = 0
    idxEnd = len(tokenLexic)
    tokenValid = False

    while i < idxEnd:

        if (i < idxEnd) and (tokenLexic[i] == 2):
            i += 1
            tokenValid = False
            while (i < idxEnd) and (tokenLexic[i] == 2):
                i += 1

        elif (i < idxEnd) and (tokenLexic[i] == 1):
            i += 1
            tokenValid = (numThen == 0 and numKurung == 0)
            if (i < idxEnd) and (tokenLexic[i] in [1, 2]):
                tokenValid = False
                break
            elif (i < idxEnd) and (tokenLexic[i] in [3, 4, 5, 8]):
                i += 1
                tokenValid = False
                if (i < idxEnd) and (tokenLexic[i] in [3, 4, 5, 8]):
                    break
            elif (i < idxEnd) and (tokenLexic[i] == 7):
                i += 1
                tokenValid = False
                if (numThen == 0):
                    break
                else:
                    numThen -= 1
            elif (i < idxEnd) and (tokenLexic[i] == 10):
                i += 1
                if (numKurung == 0):
                    break
                else:
                    numKurung -= 1
                    tokenValid = True
                    if (i < idxEnd) and (tokenLexic[i] == 1):
                        tokenValid = False
                        i += 1
                        break

        elif (i < idxEnd) and (tokenLexic[i] == 6):
            i += 1
            numThen += 1
            tokenValid = False

        elif (i < idxEnd) and (tokenLexic[i] == 9):
            i += 1
            numKurung += 1
            tokenValid = False

        else:
            break

    print(tokenValid)


def input_string():
    inputString = input("Input: ")
    inputString = inputString.split()
    tokenLexic = []
    err = False
    for x in inputString:
        tokenLexic.append(check_token(x))
        if (tokenLexic[-1] == "error"):
            err = True
            break

    return tokenLexic, err

def main():
    tokenLexic, err = input_string()
    if (err):
        print(tokenLexic)
        print("False")
    else:
        print(tokenLexic)
        validation(tokenLexic)


main()