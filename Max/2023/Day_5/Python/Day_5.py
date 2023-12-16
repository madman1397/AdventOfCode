
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

    def __init__(self):
        self.seed_list = []
        self.seed2soil_list = []
        self.soil2fertilizer_list = []
        self.fertilizer2water_list = []
        self.water2light_list = []
        self.light2temperature_list = []
        self.temperature2humidity_list = []
        self.humidity2location_list = []

class seedObj:
    number = None
    number_start = None
    number_end = None
    soil = None
    fertilizer = None
    water = None
    light = None
    temperature = None
    humidity = None
    location = None
    def __init__(self, *args):
        if len(args) == 1:
            self.number = int(args[0])
        elif len(args) == 2:
            self.number_start = int(args[0])
            self.number_end = int(args[1])
        else:
            raise ValueError("Invalid number of arguments")

    def getNumList(self):
        return [self.destRange_start, self.sourceRange_start, self.rangeLength]

class mapObj:
    destRange_start = None
    destRange_end = None
    sourceRange_start = None
    sourceRange_end = None
    rangeLength = None
    mapName = None
    
    def __init__(self, mapName, strLine):
        self.mapName = mapName
        self.line2ranges(strLine)
        self.destRange_end = self.destRange_start + self.rangeLength
        self.sourceRange_end = self.sourceRange_start + self.rangeLength

    def getNumList(self):
        return [self.destRange_start, self.sourceRange_start, self.rangeLength]

    def line2ranges(self, strLine):

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
            for cNum in seeds:
                hold.seed_list.append(seedObj(cNum))
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

def createObj_P2(listLines):
    hold = holdList()
    mapName = None

    for idx, strLine in enumerate(listLines):
        if idx == 0:
            seeds = getSplitLine(strLine)[1].split()
            startRange = None
            endRange = None
            for cNum in seeds:
                if startRange == None:
                    startRange = int(cNum)
                elif endRange == None:
                    endRange = int(cNum)
                else:
                    hold.seed_list.append(seedObj(startRange, endRange))
                    startRange = None
                    endRange = None
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

def map_values(seed, mapping_list, source_attr, dest_attr):
    for mapping in mapping_list:
        if getattr(seed, source_attr) >= mapping.sourceRange_start and getattr(seed, source_attr) <= mapping.sourceRange_end:
            delta_source = mapping.sourceRange_end - getattr(seed, source_attr)
            setattr(seed, dest_attr, mapping.destRange_end - delta_source)
            break
    if getattr(seed, dest_attr) == None:
        setattr(seed, dest_attr, getattr(seed, source_attr))

def mapSeeds(hold: holdList):
    for seed in hold.seed_list:
        map_values(seed, hold.seed2soil_list, 'number', 'soil')
        map_values(seed, hold.soil2fertilizer_list, 'soil', 'fertilizer')
        map_values(seed, hold.fertilizer2water_list, 'fertilizer', 'water')
        map_values(seed, hold.water2light_list, 'water', 'light')
        map_values(seed, hold.light2temperature_list, 'light', 'temperature')
        map_values(seed, hold.temperature2humidity_list, 'temperature', 'humidity')
        map_values(seed, hold.humidity2location_list, 'humidity', 'location')

def mapSeeds_P2(hold: holdList):
    pass

if __name__ == '__main__':

    control = input.getControlInput('2023', 'Day_5')
    hold = createObj(control)
    mapSeeds(hold)
    lowest_location = hold.seed_list[0].location
    lowest_location_seed = hold.seed_list[0].number
    for seed in hold.seed_list:
        if seed.location < lowest_location:
            lowest_location = seed.location
            lowest_location_seed = seed.number
    print('--- CONTROL P1 ---')
    print('lowest location: ' + str(lowest_location))
    print('for seed number: ' + str(lowest_location_seed))

    puzzle = input.getPuzzleInput('2023', 'Day_5')
    hold = createObj(puzzle)
    mapSeeds(hold)
    lowest_location = hold.seed_list[0].location
    lowest_location_seed = hold.seed_list[0].number
    for seed in hold.seed_list:
        if seed.location < lowest_location:
            lowest_location = seed.location
            lowest_location_seed = seed.number
    print('--- PUZZLE P1 ---')
    print('lowest location: ' + str(lowest_location))
    print('for seed number: ' + str(lowest_location_seed))

    hold = createObj_P2(puzzle)
    print(mapSeeds_P2(hold))
    lowest_location = hold.seed_list[0].location
    lowest_location_seed = hold.seed_list[0].number
    print('--- PUZZLE P2 ---')
    print('lowest location: ' + str(lowest_location))
    print('for seed number: ' + str(lowest_location_seed))

                
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
        hold = createObj(control)
        hold = createObj(control)
        self.assertEqual(79, hold.seed_list[0].number)
        self.assertEqual(4, len(hold.seed_list))
        self.assertEqual([50, 98, 2], hold.seed2soil_list[0].getNumList())
        self.assertEqual([52, 50, 48], hold.seed2soil_list[1].getNumList())

    def test_getSplitLines(self):
        control = 'seeds: 79 14 55 13\n'
        self.assertEqual(['seeds', '79 14 55 13\n'], getSplitLine(control))

    def test_mapSeeds(self):
        control = input.getControlInput('2023', 'Day_5')
        hold = createObj(control)
        mapSeeds(hold)
        self.assertEqual(81, hold.seed_list[0].soil)
        self.assertEqual(14, hold.seed_list[1].soil)
        self.assertEqual(57, hold.seed_list[2].soil)
        self.assertEqual(13, hold.seed_list[3].soil)
        self.assertEqual(82, hold.seed_list[0].location)
        self.assertEqual(35, hold.seed_list[3].location)
