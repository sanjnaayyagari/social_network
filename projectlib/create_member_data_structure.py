# read a nw_data1 file and create a member dictionary object

social_network = {}

"""
def create_dict(filename):
    print("I got the filename:" + str(filename))
    fileHandle = open(filename, "r")
    count = fileHandle.readline()  # first line is a number
    valueList = []

    while fileHandle:
        line = fileHandle.readline()
        # blank line means end of the file
        if line == '':
            break
        res = line.split(',')

        name1 = res[0].strip()
        name2 = res[1].strip()

        if name1 in social_network.keys():
            valueList = social_network.get(name1)
            valueList.append(name2)

        elif name1 not in social_network.keys():
            valueList.append(name2)

        social_network[name1] = valueList

        valueList = []

        if name2 != '':
            if name2 in social_network.keys():
                valueList = social_network.get(name2)
                valueList.append(name1)
            elif name2 not in social_network.keys():
                valueList.append(name1)

            social_network[name2] = valueList

        # print(social_network)

        valueList = []

    for key in social_network.keys():
        print(key + ": " + str(social_network.get(key)))

    print(social_network)

    fileHandle.close()

"""
def create_dict(filename):
    while True:
        try:
            print("I got the filename:" + str(filename))
            fileHandle = open(filename, "r")
            count = int(fileHandle.readline().strip())
            break

        except ValueError:
            filename = input("File is not in the correct format, please try another file: ")
            continue
        except FileNotFoundError:
            filename = input("File doesn't exist, please try again: ")
            continue
        except PermissionError:
            filename = input("Permission to read denied, please try again: ")
            continue
    # first line must be a number

        # first line is a number
    #count = int(fileHandle.readline())
    valueList = []

    while fileHandle:
        line = fileHandle.readline()
        # blank line means end of the file
        if line == '':
            break
        res = line.split(',')

        name1 = res[0].strip()
        name2 = res[1].strip()

        if name1 in social_network.keys():
            valueList = social_network.get(name1)
            valueList.append(name2)

        elif name1 not in social_network.keys():
            valueList.append(name2)

        social_network[name1] = valueList

        valueList = []

        if name2 != '':
            if name2 in social_network.keys():
                valueList = social_network.get(name2)
                valueList.append(name1)
            elif name2 not in social_network.keys():
                valueList.append(name1)

            social_network[name2] = valueList


        # print(social_network)

        valueList = []

    for key in social_network.keys():
        print(key + ": " + str(social_network.get(key)))

    print(social_network)

    fileHandle.close()









def getMembers():
    members = []
    for i in social_network:
        members.append(i)
    print("the members are: " + str(members))


def getFriends(name):
    friends = social_network.get(name)
    if name not in social_network.keys():
        print(name + " is not a member in the social network")

    elif friends == None :
        print(name + " has no friends")

    print(name + " friends are: " + str(friends))


def getFriends4All():
    for i in social_network:
        print(str(i) + " friends are: " + str(social_network.get(i)))



def getCommonFriends(name1, name2):
    friendsForName1 = social_network.get(name1)
    friendsForName2 = social_network.get(name2)
    commonFriends = []
    commonFriendCount = 0

    if name1 == name2:
        print("They are the same member")
        return

    for i in friendsForName1:
        for j in friendsForName2:
            if j == i:
                commonFriends.append(j)
                commonFriendCount += 1

    return commonFriendCount
   # print(commonFriends)
    # print(commonFriendCount)




def recommendFriends(name):
    commonFriendCountList = {}
    existingFriends = social_network.get(name)
    for member in social_network.keys():
        if member != name and member not in existingFriends:
            commonFriendCountList[member] = getCommonFriends(name, member)
    print(name + "'s mutuals")
    print(commonFriendCountList)

    key_list = list(commonFriendCountList.keys())
    val_list = list(commonFriendCountList.values())

    mostMutuals = max(commonFriendCountList.values())
    for i in commonFriendCountList:
        if mostMutuals == 0:
            print("There are no recommended friends")
            break
        elif mostMutuals == commonFriendCountList.get(i):
            print("The recommended friends: " + i)
    #position = val_list.index(mostMutuals)
    #print("The recommended friend is: " + key_list[position])

















