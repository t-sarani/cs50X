def shorten_tweet(text):
  """
  این تابع یک رشته را به عنوان ورودی دریافت می کند و تمام حروف صدادار (A، E، I، O و U) را از آن حذف می کند.
  """
  vowels = "AEIOUaeiou"
  result = ""
  for char in text:
    if char not in vowels:
      result += char
  return result

def main():
  """
  این تابع اصلی برنامه کوتاه کننده توییت است.
  """
  user_text = input("متن خود را برای کوتاه کردن توییت وارد کنید: ")
  shortened_text = shorten_tweet(user_text)
  print(f"توییت کوتاه شده: {shortened_text}")

if __name__ == "__main__":
  main()
