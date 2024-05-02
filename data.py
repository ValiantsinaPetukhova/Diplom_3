class Urls:
    # Базовый URL эндпоинтов API
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    USER_CREATION_ENDPOINT = f"{BASE_URL}/api/auth/register"
    LOGIN_URL = f"{BASE_URL}/login"
    USER_ENDPOINT = f"{BASE_URL}/auth/user"
    RECOVER_URL = f"{BASE_URL}/forgot-password"
    FEED_URL = f"{BASE_URL}/feed"
    ORDERS_HISTORY_URL = f"{BASE_URL}/account/order-history"
    PROFILE_URL = f"{BASE_URL}/account/profile"

class TestData:
    password_class_name = 'input__placeholder-focused'
    ingredients = [
        '61c0c5a71d1f82001bdaaa6d',
        '61c0c5a71d1f82001bdaaa72',
        '61c0c5a71d1f82001bdaaa70',
    ]
    buns_id = ('61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6c')
    sauces_id = ('61c0c5a71d1f82001bdaaa72', '61c0c5a71d1f82001bdaaa73',
                 '61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa75')
    fillings_id = ('61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa70',
                   '61c0c5a71d1f82001bdaaa71', '61c0c5a71d1f82001bdaaa6e',
                   '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa77',
                   '61c0c5a71d1f82001bdaaa78', '61c0c5a71d1f82001bdaaa79',
                   '61c0c5a71d1f82001bdaaa7a')
    ingredient_counter = "/div/p"

    ingredient_type = [("Bun", 2), ("Sauce", 1), ("Filling", 1)]
