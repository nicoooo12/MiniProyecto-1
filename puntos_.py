def getPuntos(PUNTOS_DIR):
    PUNTOS_ = open(PUNTOS_DIR)

    PUNTOS = PUNTOS_.read()
    PUNTOS_.close()

    Puntos = PUNTOS.split('\n')
    Puntos = [i.split(' ') for i in Puntos]
    nPuntos = [i[1] for i in Puntos]

    return Puntos, nPuntos


def addScore(name, score, PUNTOS_DIR):
    
    PUNTOS_ = open(PUNTOS_DIR)

    PUNTOS = PUNTOS_.read()

    PUNTOS_.close()

    Puntos_ = PUNTOS.split('\n')
    Puntos = [i.split(' ') for i in Puntos_]
    
    score = score[:-1]
    if name in [i[0] for i in Puntos]:
        newArr = [i if name not in i else i if float(score) >= float(i[1][:-1]) else [name, f'{score}s'] for i in Puntos]
        newArr = sorted(newArr, key=lambda puntos : puntos[1][:-1])
    else:
        newArr = [[i[0], i[1][:-1]] for i in Puntos]
        newArr.append([name, f'{score}s'])
        newArr = sorted(newArr, key=lambda puntos : puntos[1][:-1])
        newArr.pop()
    txt = ''
    for score_ in range(len(newArr)):        
        txt = txt+ str(f'{newArr[score_][0]} {newArr[score_][1]}')
        txt = txt+ ('' if score_ == (len(newArr)-1) else '\n')
    with open(PUNTOS_DIR, 'w') as PUNTOS_:
        PUNTOS_.write( txt )
    Puntos = newArr
    return newArr