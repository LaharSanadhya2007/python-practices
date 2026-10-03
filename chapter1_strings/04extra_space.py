t=input("enter sentence to remove extra space: ")
def extra_space(e):
    return " ".join(e.split())
print(extra_space(t))