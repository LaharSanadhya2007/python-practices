def gen_table(n):
    table=""
    for i in range(1,11):
        table+=f"{n} x {i} = {n*i}\n"
    with open(f"tables/table{n}_txt","w") as f:
        f.write(table)
for i in range(15,21):
    gen_table(i)
