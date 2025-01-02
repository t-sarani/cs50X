def convert_to_snake_case(text):
  """
  این تابع نام متغیری را که در camel case دریافت می کند
  و آن را به snake case تبدیل می کند.
  """
  import re
  str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

# دریافت نام متغیر از کاربر
variable_name = input("نام متغیر را در camel case وارد کنید: ")

# تبدیل نام به snake case
snake_case_name = convert_to_snake_case(variable_name)

# چاپ نام متغیر در snake case
print(snake_case_name)
