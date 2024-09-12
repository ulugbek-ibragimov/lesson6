from django.db import models
from django.utils.translation import gettext_lazy as _

class Homiy(models.Model):
    class StatusHomiy(models.TextChoices):
        yangi = 'yangi', _('Yangi')
        moderatsiyada = 'moderatsiyada', _('Moderatsiyada')
        tasdiqlangan = 'tasdiqlangan', _('Tasdiqlangan')
        bekor_qilingan = 'bekor_qilingan', _('Bekor qilingan')

    f_i_sh = models.CharField(_('F.I.SH'), max_length=100)
    phone_number = models.CharField(_('Phone number'), max_length=16)
    homiylik_summa = models.IntegerField(_('Homiylik summasi'))
    sarflangan_summa = models.IntegerField(_('Sarflangan summa'))
    sana = models.DateTimeField(_('Sana'), auto_now_add=True)
    status = models.CharField(_('Holati'), choices=StatusHomiy, max_length=20)
    amallar = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _('Homiy')
        verbose_name_plural = _('Homiylar')
    def __str__(self):
        return self.f_i_sh

class Talaba(models.Model):
    class TalabalikTuri(models.TextChoices):
        bakalavr = 'bakalavr', _('Bakalavr')
        magistr = 'magistr', _('Magistr')
    OTM_list = [("O’zbekiston milliy universiteti", _("O’zbekiston milliy universiteti")),
                ("Toshkent davlat texnika universiteti", _("Toshkent davlat texnika universiteti")),
                ("Toshkent davlat iqtisodiyot universiteti", _("Toshkent davlat iqtisodiyot universiteti")),
                ("O’zbekiston davlat jahon tillari universiteti", _("O’zbekiston davlat jahon tillari universiteti")),
                ("Toshkent davlat sharqshunoslik instituti", _("Toshkent davlat sharqshunoslik instituti")),
                ("Toshkent arxitektura-qurilish instituti", _("Toshkent arxitektura-qurilish instituti")),
                ("Toshkent avtomobil-yo’llari instituti", _("Toshkent avtomobil-yo’llari instituti")),
                ("Toshkent moliya instituti", _("Toshkent moliya instituti")),
                ("Toshkent davlat pedagogika universiteti", _("Toshkent davlat pedagogika universiteti")),
                ("Samarqand davlat universiteti", _("Samarqand davlat universiteti"))
                ]
    f_i_sh = models.CharField(_('F.I.SH'), max_length=100)
    phone_number = models.CharField(_('Phone number'), max_length=16)
    otm = models.CharField(_('OTM'), choices=OTM_list, max_length=100)
    talabalik_turi = models.CharField(_('Talabalik turi'), choices=TalabalikTuri.choices, max_length=20)
    kontrakt_summa = models.IntegerField(_('Kontrakt summa'))
    atratilgan_summa = models.IntegerField(_('Ajratilgan summa'))
    homiylar = models.ManyToManyField(to=Homiy, verbose_name=_('Homiylar'), related_name='talabalar', through='TalabaVaHomiy')

    class Meta:
        verbose_name = _('Talaba')
        verbose_name_plural = _('Talabalar')
    def __str__(self):
        return self.f_i_sh

class TalabaVaHomiy(models.Model):
    talaba = models.ForeignKey(to=Talaba, on_delete=models.CASCADE, related_name='talaba_va_homiy')
    homiy = models.ForeignKey(to=Homiy, on_delete=models.CASCADE)
    ajratilgan_summa = models.IntegerField(null=True)

    def __str__(self):
        return self.homiy.f_i_sh
