import sys
def sed(pattern,replacement,infile,outfile):
  try:
    file1=open(infile,'r')
    file2=open(outfile,'w')
    for line in file1:
      line=line.replace(pattern,replacement)
      file2.write(line)
    file1.close()
    file2.close()
  except:
    print("something went wrong \n try again")

##sed('programming','python','infile.txt','outfile.txt')
def main(name):
    pattern = ' Programming'
    replacement = ' python'
    infile = 'infile.txt'
    outfile = 'outfile.txt'
    sed(pattern, replacement, infile, outfile)


if __name__ == '__main__':
    main(*sys.argv)
