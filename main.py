import random, string

captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
print("Generated Captcha:", captcha)
