# Write some code, that will flatten an array of arbitrarily nested arrays of integers into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].

def flattenList(dataList,returnList=[]):
    if not len(returnList):
        returnList = []
    for each in dataList:
        if type(each) is type([]):
            returnList= flattenList(each,returnList)
        else:
            returnList.append(each)
    return returnList

#usage
# this function can flatten any array into a flat array
if __name__ == '__main__':
    print flattenList([[1,2,[3]],4])
    print flattenList([[5,6,[7]],8])
    print flattenList([["VK","GUPTA","Male"],41,["India"]])


