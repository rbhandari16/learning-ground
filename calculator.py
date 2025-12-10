# building a simple calculator 
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return "Error: Division by zero" if b==0 else a/b

ops = {'+': add, '-': sub, '*': mul, '/': div}

def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number"); return
    op = input("Enter operation (+, -, *, /): ").strip()
    if op not in ops:
        print("Invalid operation"); return
    print(f"{a} {op} {b} = {ops[op](a,b)}")

if __name__ == "__main__":
    main()
    