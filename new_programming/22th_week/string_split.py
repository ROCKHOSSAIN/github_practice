def split_and_join(line):
    a=line.split(" ")
    print(a)
    res="-".join(a)
    return res
    # rep=line.replace(" ","-")
    # return rep
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)