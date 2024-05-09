from abc import ABC, abstractmethod

# @brief Абстрактная фабрика
class TelegramChannelFactory(ABC):
    @abstractmethod
    def create_channel_info(self):
        pass


# @brief Абстрактный продукт - отображение информации о канале
class ChannelInfo(ABC):
    @abstractmethod
    def display_info(self):
        pass


# @brief Конкретные фабрики
class RussianTelegramChannelFactory(TelegramChannelFactory):
    def create_channel_info(self):
        return RussianChannelInfo()

class EnglishTelegramChannelFactory(TelegramChannelFactory):
    def create_channel_info(self):
        return EnglishChannelInfo()

class SpanishTelegramChannelFactory(TelegramChannelFactory):
    def create_channel_info(self):
        return SpanishChannelInfo()


# @brief Конкретные продукты
class RussianChannelInfo(ChannelInfo):
    def display_info(self):
        print("Информация о телеграм-канале МИЭМ на русском:\n\nt.me/miem_hse\nСсылка\n\nКанал для студентов, преподавателей и всех,\nкто причастен к МИЭМ НИУ ВШЭ.\n\n\nАктуальные новости, полезные материалы,\nинтервью с экспертами - все самое\nинтересное о факультете.\n\n\nСайт:https://miem.hse.ru/\nГруппа ВКонтакте:https://vk.com/miem_hse")

class EnglishChannelInfo(ChannelInfo):
    def display_info(self):
        print("Information about MIEM Telegram channel in English:\n\nt.me/miem_hse\nLink\n\nA channel for students, teachers and everyone\nwho is involved in MIEM NRU HSE.\n\n\nCurrent news, useful materials,\ninterviews with experts - all the most\ninteresting things about the faculty.\n\n\nWebsite: https://miem.hse.ru/\nVKontakte group: https://vk.com/miem_hse")

class SpanishChannelInfo(ChannelInfo):
    def display_info(self):
        print("Información sobre el canal de Telegram de MIEM en español:\n\nt.me/miem_hse\nEnlace\n\nUn canal para estudiantes, profesores y todos los\nque participan en MIEM NRU HSE.\n\n\nNoticias de actualidad, materiales útiles,\nentrevistas con expertos: todo lo\nmás interesante sobre la facultad.\n\n\nSitio web: https://miem.hse.ru/\nGrupo VKontakte: https://vk.com/miem_hse")

# Использование
def main():
    language = input("Выберите язык (ru, en, es): ")

    if language == "ru":
        factory = RussianTelegramChannelFactory()
    elif language == "en":
        factory = EnglishTelegramChannelFactory()
    elif language == "es":
        factory = SpanishTelegramChannelFactory()
    else:
        print("Выбран неподдерживаемый язык.")
        return

    channel_info = factory.create_channel_info()
    channel_info.display_info()

if __name__ == "__main__":
    main()