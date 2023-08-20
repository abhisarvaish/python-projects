import re
import sys

devlopers = ['ABHISAR', 'ANISHA']

"""-p Takes an input file name with text and phone numbers and extracts
all the phone numbers then outputs a file containing a list of the
phone numbers only, e.g. -p inputfile.txt outputfile.txt"""


def dump_numbers(input_file, output_file):
    with open(input_file, 'r') as readFile:
        contents = readFile.read()
        number_list = re.findall('[0-9]+', contents)
        str_content = '\n'.join(number_list)

        with open(output_file, 'w')as writeFile:
            writeFile.write(str_content)
    print("BRAVO!! : Numbers have been posted!")


"""-b Takes an input file name for a binary file, copies and saves a
binary file to a new location (Note, should not be implemented with
built in functions like copyfile(3) or shutil.copy), e.g.
-b inputfile outputfile"""


# Reading and writing Line By Line

def duplicate_outputfile_copy(input_file, output_file):
    with open(input_file, 'r')as rFile:
        with open(output_file, 'a+') as wFile:
            for line in rFile.readlines():
                wFile.write(line)
    print("BRAVO!! : Backup Output File has been Created!")


""" -u Takes a comma separated list of integers and returns the number of
unique ones to the command line, e.g.
-u 1,2,2,3,4,5,4 returns "3" (1, 3, and 5 occur exactly
once)"""


def return_unique_number(val):
    values = val.split(',')
    counter_dict = {key: values.count(key) for key in values if values.count(key) == 1}
    return len(counter_dict.keys())


"""-c Takes two file names as input and prints “true” if the contents are
identical or “false” if not, e.g. -c fileA fileB"""


def cormapre_file(fileA, fileB):
    flag = True
    with open(fileA, 'r')as fileA:
        with open(fileB, 'r') as fileB:
            dataA, dataB = fileA.read(), fileB.read()
            if not dataA == dataB:
                flag = False
    return flag


# Call function as per command line argument
try:
    if sys.argv[1] == '-p':
        if sys.argv[2] and sys.argv[3]:
            dump_numbers(sys.argv[2], sys.argv[3])


    elif sys.argv[1] == '-b':
        if sys.argv[2] and sys.argv[3]:
            duplicate_outputfile_copy(sys.argv[2], sys.argv[3])


    elif sys.argv[1] == '-u':
        print("BRAVO!! Total Unique Values in The List are :", return_unique_number(sys.argv[2]))


    elif sys.argv[1] == '-c':
        if cormapre_file(sys.argv[2], sys.argv[3]):
            print(True)
        else:
            print(False)


    elif sys.argv[1] == '-h' or sys.argv[1] == '-help':
        print("""\n\n \t Supported Commands are: \n\n
                -p : \t Takes an input file name with text and phone numbers and extracts
                \t all the phone numbers then outputs a file containing a list of the
                \t phone numbers only, e.g. -p inputfile.txt outputfile.txt \n \n
                
                -b : \t Takes an input file name for a binary file, copies and saves a
                \t binary file to a new location (Note, should not be implemented with
                \t built in functions like copyfile(3) or shutil.copy), e.g.
                \t -b inputfile outputfile \n\n
                
                -u : \t Takes a comma separated list of integers and returns the number of
                \t unique ones to the command line, e.g.
                \t -u 1,2,2,3,4,5,4 returns "3" (1, 3, and 5 occur exactly
                \t once)\n\n
                
                -c : \t Takes two file names as input and prints “true” if the contents are
                \t identical or “false” if not, e.g. -c fileA fileB""")


    elif sys.argv[1].upper() in devlopers:
        print("Bow Down to Awsesome Develper!!")

    else:
        print("WHOOPS!! Command Not Supported!!")

except IndexError:
    print("WHOOPS!! Seems Like All Arguments are not Bieng Passed!!")

except FileNotFoundError:
    print("WHOOPS!! Mentioned File is Not Present!!")
