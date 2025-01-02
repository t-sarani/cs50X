# جدا کردن اجزای عبارت
def calculate(expression):
    parts = expression.split()
    x = int(parts[0])
    operator = parts[1]
    z = int(parts[2])
# انجام محاسبات بر اساس عملگر
    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/' and z != 0:  # اطمینان از اینکه مخرج صفر نباشد
        result = x / z
    else:
        result = 0  # در صورت وجود خطا، صفر را برگردانید

# چاپ نتیجه با یک رقم اعشار
    print(f"{result:.1f}")

def main():
    expression = input("لطفاً یک عبارت حسابی وارد کنید: ")
    calculate(expression)


if __name__ == "__main__":
    main()
