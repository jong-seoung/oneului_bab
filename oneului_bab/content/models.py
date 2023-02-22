from django.db import models

class FoodList(models.Model):
    MAIN_CHOICES = (("noodle", "면"), ("rice", "밥"), ("bread", "빵"))
    SOUP_CHOICES = (("yes", "국물 있음"), ("little", "국물 쪼금"), ("no", "국물 없음"))
    SPICY_CHOICES = (("spicy", "매움"), ("normal", "보통"), ("mild", "순함"))
    TEMPERATURE_CHOICES = (("cool", "차갑게"), ("warm", "적당히 따뜻하게"), ("hot", "뜨거울 정도로"))
    WEIGHT_CHOICES = (("heavy", "무거움"), ("light", "가벼움"))

    name = models.CharField('이름', max_length=50)
    main = models.CharField('메인분류', choices=MAIN_CHOICES, max_length=10)
    soup = models.CharField('국물', choices=SOUP_CHOICES, max_length=10)
    Spicy = models.CharField('맵기', choices=SPICY_CHOICES, max_length=10)
    temperature = models.CharField('온도', choices=TEMPERATURE_CHOICES, max_length=10)
    weight = models.CharField('무게', choices=WEIGHT_CHOICES, max_length=10)
    approved = models.BooleanField(default=False)

    # 데이터 표시 형식 변경 
    def __str__(self): 
        return '{}'.format(self.name)
