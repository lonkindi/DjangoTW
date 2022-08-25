from django.db import models

class Anket(models.Model):
    """
    Модель анкеты
    """
    external_id = models.PositiveIntegerField(verbose_name='Внешний ИД')
    state = models.PositiveIntegerField(verbose_name='Статус')
    content = models.JSONField(verbose_name='Содержимое анкеты')
    # url = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    # user = models.OneToOneField(MyUser, verbose_name='Пользователь',
    #                             blank=True, null=True,
    #                             on_delete=models.CASCADE)
    # state = models.BooleanField(verbose_name='Магазин работает?', default=True)
    # filename = models.FileField(upload_to=f'data/price/', verbose_name='Актуальный прайс-лист')

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = "Анкеты"
        ordering = ('-external_id',)

    # def __str__(self):
    #     return self.name