#import raw .txt source
sourceData = open("AdventOfCode\\Input\\Shayne\\2022\\Day_6.txt").readlines()
#----------------------------------------------------------------------------------------------------

packetWindow = []
messageWindow = []
SOPMarker = []
messageMarker = []
index = 0
messageIndex = 0
#finding Start-of-Packet marker (first 4 unique characters)
for char in sourceData[0]:
    packetWindow.append(char)
    index += 1
    if len(packetWindow) > 4: packetWindow.pop(0)
    if len(packetWindow) == 4:
        if len(set(packetWindow)) == len(packetWindow):
            SOPMarker.append(packetWindow)
            break
#----------------------------------------------------------------------------------------------------
#finding message marker (first 14 unique characters)
for char in sourceData[0]:
    messageWindow.append(char)
    messageIndex += 1
    if len(messageWindow) > 14: messageWindow.pop(0)
    if len(messageWindow) == 14:
        if len(set(messageWindow)) == len(messageWindow):
            messageMarker.append(messageWindow)
            break
print(messageMarker)
print(messageIndex)