import random  # برای انتخاب تصادفی حرکت کامپیوتر

def get_computer_choice():
    """
    انتخاب تصادفی یکی از گزینه‌های:
    s = سنگ
    k = کاغذ
    g = قیچی
    """
    choices = ['s', 'k', 'g']
    return random.choice(choices)

def moghaiese(user, computer):
    """
    مقایسه انتخاب کاربر و کامپیوتر
    و مشخص کردن برنده
    """
    if user == computer:
        return "mosavi"  # مساوی
    elif (user == 's' and computer == 'g') or \
         (user == 'k' and computer == 's') or \
         (user == 'g' and computer == 'k'):
        return "user barande shod"  # کاربر برنده شد
    else:
        return "computer barande shod"  # کامپیوتر برنده شد

def play_game():
    """
    تابع اصلی اجرای بازی
    مدیریت امتیازها و ورودی کاربر
    """
    computer_score = 0
    user_score = 0

    # پیام خوش‌آمدگویی
    print("--------------------------")
    print("Be bazi Sang, Kaghaz, Gheychi khosh amadid")
    print("s = sang | k = kaghaz | g = gheychi")
    print("Type kon 'exit' baraye khoroj az bazi")
    print("--------------------------")

    # حلقه اصلی بازی
    while True:
        user_select = input("Entekhab konid (s/k/g): ").lower()

        # خروج از بازی
        if user_select == "exit":
            print("Bazi payan yafte shod 👋")
            break

        # بررسی معتبر بودن ورودی
        if user_select not in ['s', 'k', 'g']:
            print("Voroodi na motabar ast! Lotfan s, k ya g vared konid.")
            continue

        # انتخاب کامپیوتر
        computer_select = get_computer_choice()
        print("Entekhab computer:", computer_select)

        # محاسبه نتیجه
        result = moghaiese(user_select, computer_select)
        print("Natije:", result)

        # به‌روزرسانی امتیازها
        if result == "user barande shod":
            user_score += 1
        elif result == "computer barande shod":
            computer_score += 1

        # نمایش امتیازها
        print(f"Emtiaz shoma: {user_score} | Emtiaz computer: {computer_score}")
        print("-------------------------------------")

# اجرای بازی
play_game()
