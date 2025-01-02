# تبدیل زمان به فرمت شناور
def convert(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours + minutes / 60

def main():
    time_str = input("لطفاً زمان را وارد کنید (به فرمت 24 ساعته): ")
    time_float = convert(time_str)

# تعیین وقت وعدههای غذایی
    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")
# اگر وقت غذا نرسیده، چیزی چاپ نمیشود

if __name__ == "__main__":
    main()
