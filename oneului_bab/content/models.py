from django.db import models

class FoodList(models.Model):
    country_CHOICES = (("korean", "한식"), ("Japanese", "일식"), ("Chinese", "중식"), ("Western", "양식"), 
    ("Asian", "아시안"), ("Mexican", "맥시칸"))
    main_CHOICES = (("noodle", "면"), ("rice", "밥"), ("bread", "빵"))
    soup_CHOICES = (("yes", "국물 있음"), ("little", "국물 쪼금"), ("no", "국물 없음"))
    Spicy_CHOICES = (("spicy", "매움"), ("normal", "보통"), ("mild", "순함"))
    temperature_CHOICES = (("cool", "cool"), ("hot", "hot"))
    weight_CHOICES = (("heavy", "heavy"), ("light", "light"))

    name = models.CharField('이름', max_length=50, null=False, blank=True)
    country = models.CharField('나라',choices=country_CHOICES, max_length=50, null=False, blank=True)
    main = models.CharField('메인분류',choices=main_CHOICES, max_length=50, null=False, blank=True)
    soup = models.CharField('국물',choices=soup_CHOICES, max_length=50, null=False, blank=True)
    Spicy = models.CharField('맵기',choices=Spicy_CHOICES, max_length=50, null=False, blank=True)
    temperature = models.CharField('온도',choices=temperature_CHOICES, max_length=50, null=False, blank=True)
    weight = models.CharField('무게',choices=weight_CHOICES, max_length=50, null=False, blank=True)

    # 데이터 표시 형식 변경 
    def __str__(self): 
        return '{}'.format(self.name)
