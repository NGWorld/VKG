__author__ = 'VK Gupta'
# -*- coding: utf-8 -*-

'''
Write a class TempTracker with these methods insert records a new temperature get_max returns the highest temp we have seen so far get_min returns the lowest temp we have seen so far
get_mean returns the mean of all temps we've seen so far get_mean should return a float, but the rest of the getter functions can return integers. 
Temperatures will all be inserted as integers. 
We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0 to 110
'''

import os

class TempTracker():
    def __init__(self,data):
        self.data=[]
        self.dataFile = None
        self.degree = u'\N{DEGREE SIGN}'
        if type(data) is type([]):
            self.data = data
        else:
            self.data = self.getData(data)

    def getData(self,data):
        returnData = []
        if os.path.exists(data):
            file = open(data, "r")
            for each in file.readlines():
                returnData.append(int(each))
            file.close()
            self.dataFile = data
        return returnData

    def insert(self,value):
        if type(value) is not type(1):
            print "Pass an integer Value"
            return
        if value < 0 or value > 110:
            print "Valid Temperature Range is 0 to 110"
            return
        self.data.append(value)
        self.saveData(value)

    def get_max(self):
        return sorted(self.data)[-1]

    def get_min(self):
        return sorted(self.data)[0]

    def get_mean(self):
        return sum(self.data) / float(len(self.data))

    def saveData(self,newValue=None):
        if self.dataFile:
            file = open(self.dataFile, "a")
            if newValue:
                file.write("%s\n" % newValue)
                print "New temparature with Value %s Recorded"%newValue
            file.close()

    def formatValue(self,value):
        return '%s%sF'%(value,self.degree)


if __name__ == '__main__':
    myTemparatures = TempTracker("C:/Users/gupta/Desktop/temTracker.txt")
    myTemparatures.insert(66)
    print 'Minimum :%s'%myTemparatures.formatValue(myTemparatures.get_min())
    print 'Maximum :%s'%myTemparatures.formatValue(myTemparatures.get_max())
    print 'Mean :%s'%myTemparatures.formatValue(myTemparatures.get_mean())