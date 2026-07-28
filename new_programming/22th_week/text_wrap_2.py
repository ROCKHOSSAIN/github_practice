# import textwrap
def wrap(string, max_width):
    list_n=[]
    i=0
    while(i<len(string)):
        list_n.append(string[i:max_width+i])
        i+=max_width
    return "\n".join(list_n)
    # res=textwrap.fill(string , max_width)
    print(list_n)

    # return res
    return list_n

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)