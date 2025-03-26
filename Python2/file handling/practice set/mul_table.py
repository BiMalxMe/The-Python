def multiplication(num):
    table=""
    for i in range(1,11):
        table+=f"{num} * {i} = {num*i}\n"
    with open(f"table/table_{num}.txt","w") as f:
        f.write(table)

     
for i in range(2,21):
    multiplication(i)