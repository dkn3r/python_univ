from django.db import models


# Create your models here.
class Blogger:
    def __init__(self, name, category, description, social_media_link):
        self.name = name
        self.category = category
        self.description = description
        self.social_media_link = social_media_link


blogger1 = Blogger("Міша", "Блогер", "Дуже позитивна людина,допомагає ЗСУ.Його сторіс дуже веселі і легко піднімає настрій на весь день.", "https://www.instagram.com/misha_lebiga/reels/")
blogger2 = Blogger("Сергій", "Блогер", "Від нього можно почути та подивитися нові новини про Україну. ", "https://www.youtube.com/@STERNENKO/videos")

bloggers = {
    "blogger1": blogger1,
    "blogger2": blogger2,
}
