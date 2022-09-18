import time

def climbingLeaderboard(ranked, player):
    
    # list to put answers in
    listPosition = list()

    # sort leaderboard into ascending
    ranked = sorted(set(ranked))
    lenRanked = len(ranked)

    # here we are cycling through each player score and finding where it falls on leaderboard
    i = 0
    lastI = i
    for score in player:
        # once reaches the end of the leaderboard, just keep the position the same as before
        if i >= lenRanked:
            pos = pos
        else:
            # if score higher than one on leaderboard, while loop stops
            while score > ranked[i]:
                i += 1
                if i == lenRanked:
                    pos = 1
                    break

        # score rank depends on whether the score is equal to the ranked score or not
        if i != lenRanked:    
            if score == ranked[i]:
                pos = lenRanked - i
            else:
                pos = lenRanked - i + 1


        listPosition.append(pos)

    return listPosition
        
        
if __name__ == '__main__':
    f = open('./climbingLeaderboard.txt', 'r')
    test = f.read()
    ranked = list(map(int, test.split('\n')[1].split(' ')))
    player = list(map(int, test.split('\n')[3].split(' ')))


    assert climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]) == [6, 4, 2, 1]
    print(climbingLeaderboard(ranked, player))
