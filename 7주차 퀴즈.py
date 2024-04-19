results=[]
matrix=[[1,2,3],[4,5,6],[7,8,9]]

for row in matrix:
    for num in row:
        if num % 2==0:
            results.append(num)

            print("짝수",results)
