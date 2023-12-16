
import sys
sys.path.insert(1, 'Setup')
import input
import io
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
    number = [None, None]
    soil = [[None, None]]
    fertilizer = [[None, None]]
    water = [[None, None]]
    light = [[None, None]]
    temperature = [[None, None]]
    humidity = [[None, None]]
    location = [[None, None]]
    def __init__(self, numList):
        self.number = [int(numList[0]), int(numList[0]) + int(numList[1])]
        self.soil = []
        self.fertilizer = []
        self.water = []
        self.light = []
        self.temperature = []
        self.humidity = []
        self.location = []

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

                if startRange != None and endRange != None:
                    hold.seed_list.append(seedObj([startRange, endRange]))
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

def map_values(seed, sourceValues, mapping_list, source_attr, dest_attr):
    flag_allMapped = False
    for map in mapping_list:
        delta_start_source = sourceValues[0] - map.sourceRange_start
        delta_end_source = map.sourceRange_end - sourceValues[1]
        if delta_start_source >= 0 and delta_end_source >= 0:
            getattr(seed, dest_attr).append([map.destRange_start + delta_start_source, map.destRange_end - delta_end_source])
            flag_allMapped = True
            break
        elif delta_start_source > 0 and delta_end_source < 0 and abs(delta_end_source) < abs(sourceValues[0] - sourceValues[1]):
            getattr(seed, dest_attr).append([map.destRange_start + delta_start_source, map.destRange_end])
            sourceValues[0] = map.sourceRange_end + 1
        elif delta_start_source < 0 and delta_end_source > 0 and abs(delta_start_source) < abs(sourceValues[0] - sourceValues[1]):
            getattr(seed, dest_attr).append([map.destRange_start, map.destRange_end - delta_end_source])
            sourceValues[1] = map.sourceRange_start - 1
    if flag_allMapped == False:
        getattr(seed, dest_attr).append(sourceValues)
    #print(getattr(seed, dest_attr))

def mapSeeds(hold: holdList):
    locationReturn = float('inf')
    for seed in hold.seed_list:
        #print(seed.number)
        map_values(seed, seed.number, hold.seed2soil_list, "number", "soil")
        #print(seed.soil)
        for soilValue in seed.soil:
            map_values(seed, soilValue, hold.soil2fertilizer_list, "soil", "fertilizer")
        #print(seed.fertilizer)
        for fertilizerValue in seed.fertilizer:
            map_values(seed, fertilizerValue, hold.fertilizer2water_list, "fertilizer", "water")
        #print(seed.water)
        for waterValue in seed.water:
            map_values(seed, waterValue, hold.water2light_list, "water", "light")
        #print(seed.light)
        for lightValue in seed.light:
            map_values(seed, lightValue, hold.light2temperature_list, "light", "temperature")
        #print(seed.temperature)
        for tempValue in seed.temperature:
            map_values(seed, tempValue, hold.temperature2humidity_list, "temperature", "humidity")
        #print(seed.humidity)
        for humidityValue in seed.humidity:
            map_values(seed, humidityValue, hold.humidity2location_list, "humidity", "location")
        #print(seed.location)
    for seed in hold.seed_list:
        seed.location = sorted(seed.location, key=lambda x: x[0])
        checkLocation = seed.location[0]
        if checkLocation[0] < locationReturn:
            locationReturn = seed.location[0][0]
        #print(locationReturn)
    return locationReturn

if __name__ == '__main__':
    puzzle = input.getPuzzleInput('2023', 'Day_5')
    control = input.getControlInput('2023', 'Day_5')
    hold = createObj_P2(puzzle)
    print(mapSeeds(hold))

################################################################
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('2023', 'Day_5')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))
    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('2023', 'Day_5')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))
        
    def test_seedRange(self):
        seedRange = seedObj(['1\n', '2'])
        self.assertEqual([1, 3], seedRange.number)
    
    def test_createObj_P2(self):
        control = input.getControlInput('2023', 'Day_5')
        hold = createObj_P2(control)
        self.assertEqual([79, 79+14], hold.seed_list[0].number)
        self.assertEqual([55, 55+13], hold.seed_list[1].number)
        self.assertEqual(50, hold.seed2soil_list[0].destRange_start)

    def test_mapSeeds(self):
        control = input.getControlInput('2023', 'Day_5_b')
        hold = createObj_P2(control)
        self.assertEqual([50, 80], hold.seed_list[0].number)
        mapSeeds(hold)