# main.py
from kivy.app import App
from kivy.core.window import Window
from kivy.storage.dictstore import DictStore
from kivy.lang import Builder
from kivy.animation import Animation  # Добавлен импорт

from decision_logic import DecisionMaker
import config


class DecisionApp(App):
    def build(self):
        return None

    def on_start(self):
        self.store = DictStore('decision_app.json')
        
        if self.store.exists('state'):
            state = self.store.get('state')
            self.root.ids.options_input.text = state.get(config.KEY_OPTIONS, "")
            self.root.ids.result_label.text = state.get(config.KEY_RESULT, "Нажмите кнопку, чтобы выбрать")
            if "Ваш выбор" in state.get(config.KEY_RESULT, ""):
                self.root.ids.result_label.color = 0.4, 0.8, 0.4, 1
            else:
                self.root.ids.result_label.color = 1, 1, 1, 1

    def on_stop(self):
        self.store.put('state',
                       options=self.root.ids.options_input.text,
                       result=self.root.ids.result_label.text)

    def on_pause(self):
        self.on_stop()
        return True

    def hide_keyboard(self):
        Window.release_all_keyboards()

    # Исправленная функция анимации
    def button_scale(self, button, target_size_hint):
        Animation(size_hint=(target_size_hint, target_size_hint), duration=0.1).start(button)

    def choose_option(self):
        options = DecisionMaker.parse_options(self.root.ids.options_input.text)
        result_label = self.root.ids.result_label

        if not DecisionMaker.validate_options(options):
            result_label.text = (f"Нужно минимум {config.MIN_OPTIONS_COUNT} "
                                 f"варианта{'а' if config.MIN_OPTIONS_COUNT > 2 else ''}")
            result_label.color = 1, 0.4, 0.4, 1
            return

        choice = DecisionMaker.choose(options)
        result_label.text = f"Ваш выбор:\n{choice}"
        result_label.color = 0.4, 0.8, 0.4, 1

        self.store.put('state', 
                       options=self.root.ids.options_input.text,
                       result=result_label.text)


if __name__ == "__main__":
    DecisionApp().run()