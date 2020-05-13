import time

start_time = time.time()
def count_word(file):

    #open an input and output file
    infile = open(file,"r")
    outfile = open("result.txt","w")


    #dem tu trong string
    split_string = infile.read().split()
    string_dict = {}
    #first populate the dictionary with the keys being each word in the string, all having zero for their values.
    for word in split_string:
    #Then cycle through the split string again and if the word is one of the keys in the dictionary add 1 each time.
        if word in string_dict.keys():
            string_dict[word]=string_dict[word]+1
        else:
            string_dict[word]=1
    outfile.write(str(string_dict))
    #close the input and output file
    outfile.close()
    infile.close()

#Main Program
name_infile = input("Enter the name of a text file: ")
count_word(name_infile)
print ("result.txt was created successfully","--- %s seconds ---" % (time.time() - start_time))
