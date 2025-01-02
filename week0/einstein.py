def calculate_energy(mass):
    speed_of_light = 299792458  # سرعت نور در متر بر ثانیه
    energy = mass * speed_of_light ** 2  # محاسبه انرژی با استفاده از فرمول E=mc^2
    return round(energy, -16)

def main():
    mass = int(input("Please enter the mass in kilograms: "))  # درخواست ورودی جرم از کاربر
    print(f"The equivalent energy is: {calculate_energy(mass)} joules")   # محاسبه و چاپ انرژی معادل


main()
