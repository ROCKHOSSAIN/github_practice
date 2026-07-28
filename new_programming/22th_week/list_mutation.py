def mutate_string(string, position, character):
    new_string=list(string)
    new_string[position]=character
    joined_str="".join(new_string)

    return joined_str

if __name__ == '__main__':
    s = input()
    # i, c = input().split()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    
    print(s_new)