# start from 90052
filename = "90052.txt"

while 1:
    with open('txt/' + filename, "r") as f:
        text = f.read()
        text = text.split(' ')
        text = text[-1]
        print text
        filename = text + '.txt'
