def organizingContainers(container):
    # Write your code here
    # find out amount of each ball type and total balls per container
    amountPerType = []
    amountPerContainer = []
    for con in container:
        amountPerContainer.append(sum(con))
        for i in range(len(con)):
            if i >= len(amountPerType):
                amountPerType.append(con[i])
            else:
                amountPerType[i] += con[i]

    # if these are equal that means there is space for each ball type in each container
    return 'Possible' if sorted(amountPerType) == sorted(amountPerContainer) else 'Impossible'
        






if __name__ == '__main__':
    container = [[1,1],[1,1]]
    container = [[1,3,1],[2,1,2],[3,3,3]]

    print(organizingContainers(container))
