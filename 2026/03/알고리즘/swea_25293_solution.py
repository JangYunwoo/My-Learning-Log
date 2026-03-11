def init(N, K, mId, sId, eId, mInterval):
    global traininfo
    traininfo = {}
    for i in range(K):
        traininfo[mId[i]] = [sId[i], eId[i], mInterval[i]]

    return

def add(mId, sId, eId, mInterval):
    traininfo[mId] = [sId, eId, mInterval]
    return


def remove(mId):
    traininfo.pop(mId)
    return


def calculate(sId, eId):
    q = []
    visitedstation = {}
    for nexttrain in traininfo: 
        if traininfo[nexttrain][0]<=sId<=traininfo[nexttrain][1] and (sId - traininfo[nexttrain][0]) % traininfo[nexttrain][2] == 0:
            q.append(nexttrain)
            visitedstation[nexttrain] = 1
    trans = 0
    while q:
        newq = q
        q = []
        for ctrain in newq:
            if traininfo[ctrain][0]<=eId<=traininfo[ctrain][1] and (eId - traininfo[ctrain][0])%traininfo[ctrain][2] == 0:
                return trans
            for nexttrain in traininfo:
                if visitedstation.get(nexttrain):
                    continue
                if traininfo[nexttrain][0] > traininfo[ctrain][1] or traininfo[nexttrain][1] < traininfo[ctrain][0]:
                    continue
                if traininfo[nexttrain][0] >= traininfo[ctrain][0]:
                    fronttrain = nexttrain
                    behindtrain = ctrain
                else:
                    fronttrain = ctrain
                    behindtrain = nexttrain

                cstation = traininfo[fronttrain][0]
                start = cstation
                end = min(traininfo[fronttrain][1], traininfo[behindtrain][1])
                trynum = traininfo[behindtrain][2]
                for _ in range(trynum):
                    if start<=cstation<=end:
                        if (cstation - traininfo[behindtrain][0]) % traininfo[behindtrain][2] == 0 and not visitedstation.get(nexttrain):
                            q.append(nexttrain)
                            visitedstation[nexttrain] = 1
                        else:
                            cstation += traininfo[fronttrain][2]
                    else:
                        break
        trans += 1
    return -1