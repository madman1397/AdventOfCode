
import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest
import unittest

class holdList:
    seed_list = []
    seed2soil_list = []
    soil2fertilizer_list = []
    fertilizer2water_list = []
    water2light_list = []
    light2temperature_list = []
    temperature2humidity_list = []
    humidity2location_list = []

class seedObj:
    def __init__(self, number):
            self.number = None
            try:
                self.number = int(number)
            except:
                print('Error in __init__')

class mapObj:
    def __init__(self, mapName, strLine):
        self.mapName = mapName
        self.line2ranges(strLine)

    def getNumList(self):
        return [self.destRange_start, self.sourceRange_start, self.rangeLength]

    def line2ranges(self, strLine):
        self.destRange_start = None
        self.sourceRange_start = None
        self.rangeLength = None
        strLine = strLine.split()
        if len(strLine) != 3:
            print('Error in line2ranges - wrong number count')
            raise Exception('Error in line2ranges - wrong number count')
        else:
            for idx, cNum in enumerate(strLine):
                try:
                    strLine[idx] = int(cNum)
                except:
                    print('Error in line2ranges - wrong number count')
            self.destRange_start = strLine[0]
            self.sourceRange_start = strLine[1]
            self.rangeLength = strLine[2]

def getSplitLine(strLine):
    strLineSplit = strLine.split(':')
    strLineSplit[1] = strLineSplit[1].replace(' ', '', 1)
    return strLineSplit

def createObj(listLines):
    hold = holdList()
    mapName = None

    for idx, strLine in enumerate(listLines):
        if idx == 0:
            seeds = getSplitLine(strLine)[1].split()
            for idx, cNum in enumerate(seeds):
                hold.seed_list.append(int(cNum))
        else:
            if ':' in strLine and strLine != '\n':
                mapName = strLine.split(' ')[0]
            elif strLine != '\n':
                if mapName == 'seed-to-soil':
                    hold.seed2soil_list.append(mapObj(mapName, strLine))
                elif mapName == 'soil-to-fertilizer':
                    hold.soil2fertilizer_list.append(mapObj(mapName, strLine))
                elif mapName == 'fertilizer-to-water':
                    hold.fertilizer2water_list.append(mapObj(mapName, strLine))
                elif mapName == 'water-to-light':
                    hold.water2light_list.append(mapObj(mapName, strLine))
                elif mapName == 'light-to-temperature':
                    hold.light2temperature_list.append(mapObj(mapName, strLine))
                elif mapName == 'temperature-to-humidity':
                    hold.temperature2humidity_list.append(mapObj(mapName, strLine))
                elif mapName == 'humidity-to-location':
                    hold.humidity2location_list.append(mapObj(mapName, strLine))
    return hold

                
if __name__ == '__main__':
    control = input.getControlInput('2023', 'Day_5')

                
################################################################
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('2023', 'Day_5')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))
    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('2023', 'Day_5')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))
        
    def test_objMap(self):
        seed = seedObj('1\n')
        self.assertEqual(1, seed.number)

        map = mapObj('seed2soil', '50 98 2\n')
        self.assertEqual('seed2soil', map.mapName)
        self.assertEqual(50, map.destRange_start)
        self.assertEqual(98, map.sourceRange_start)
        self.assertEqual(2, map.rangeLength)

    def test_createObj(self):
        control = input.getControlInput('2023', 'Day_5')
        self.assertEqual([79, 14, 55, 13], createObj(control).seed_list)
        self.assertEqual([50, 98, 2], createObj(control).seed2soil_list[0].getNumList())

    def test_getSplitLines(self):
        control = 'seeds: 79 14 55 13\n'
        self.assertEqual(['seeds', '79 14 55 13\n'], getSplitLine(control))
