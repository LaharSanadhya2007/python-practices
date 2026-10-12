def temp_c_to_f(c):
    f=(c*9/5)+32
    return f
c=int(input("enter temperature in celcus: "))
print("temperature in fehrenheit: ",temp_c_to_f(c))
