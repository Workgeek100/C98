def countwordsfromfile():
    filename = input("Enter the file name")
    file = open(filename,"r")
    number_of_words = 0
    for i in file :
        words = i.split()
        number_of_words = number_of_words+len(words)
    print(number_of_words)

countwordsfromfile()