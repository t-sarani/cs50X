def convert(input_str):
    return input_str.replace(':)', '\U0001F642').replace(':(', '\U0001F641')
# جایگزینی چهرههای خندان و اخمو با ایموجیهای مربوطه


def main():
    user_input = input("Please enter your text: ")
# چاپ نتیجه تبدیل شده
    print(convert(user_input))


main()
