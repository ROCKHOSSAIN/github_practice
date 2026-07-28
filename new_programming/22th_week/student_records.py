dic={}
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        dic[name]=scores
        student_marks[name] = scores
    query_name = input()

for key,value in dic.items():
    if(key==query_name):
        total_sum=sum(value)/3
        
        print(f"{total_sum:.2f}")
