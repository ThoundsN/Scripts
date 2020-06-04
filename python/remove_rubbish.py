import sys
import datetime

rubbish = """Words: 4
Words: 7
Words: 1395
Words: 24
Words: 637
Status: 403
Words: 5
Words: 19
Words: 14
Words: 5529
Words: 671
Words: 180
Words: 12"""
rubbish = rubbish.split('\n')

print(rubbish)


def main():
    input_file = sys.argv[1]
    currenttime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    outputfilename = "ffuf_" + currenttime+'.txt'

    with open(outputfilename, 'w', encoding='utf-8') as output:
        with open(input_file, 'r', encoding='utf-8') as input:
            lines = input.readlines()
            for line in lines:
                if not any(bad_word in line for bad_word in rubbish):
                    output.write(line.replace('[2K',''))



if __name__ == '__main__':
  main()
