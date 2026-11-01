# config.py
from kivy.metrics import dp

# Ключи для сохранения состояния
KEY_OPTIONS = "saved_options"
KEY_RESULT = "last_result"

# UI-параметры (адаптивные)
PADDING = dp(24)
SPACING = dp(16)
FONT_SIZE_TITLE = dp(24)
FONT_SIZE_TEXT = dp(18)
FONT_SIZE_BUTTON = dp(20)

# Минимальное количество вариантов для честного выбора
MIN_OPTIONS_COUNT = 2