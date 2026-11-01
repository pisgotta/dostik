# decision_logic.py
import random
from typing import List, Optional


class DecisionMaker:
    @staticmethod
    def parse_options(text: str) -> List[str]:
        """Очищает ввод от пустых строк и лишних пробелов."""
        return [line.strip() for line in text.splitlines() if line.strip()]

    @staticmethod
    def validate_options(options: List[str]) -> bool:
        """Проверяет, достаточно ли вариантов для случайного выбора."""
        return len(options) >= 2

    @staticmethod
    def choose(options: List[str]) -> Optional[str]:
        """Возвращает случайный элемент или None, если список пуст."""
        if not DecisionMaker.validate_options(options):
            return None
        return random.choice(options)