import projectlib.create_member_data_structure as cd

def main():
    print("Hello World!")
    filename = input("Enter the filename: ")
    #filename = "/Users/sanjna/PycharmProjects/paradigms_social_network/resources/nw_data1.txt"
    cd.create_dict(filename)

    #cd.getMembers()
    #cd.getFriends("Bob")
    #cd.getFriends4All()
    #cd.getCommonFriends("Bob", "Bob")
    #cd.recommendFriends("Mia")


if __name__ == '__main__':
    main()





