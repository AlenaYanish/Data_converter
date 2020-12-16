from django.db import models
from simple_history.models import HistoricalRecords

from business_register.models.kved_models import Kved
from data_ocean.models import DataOceanModel, Status, Authority, TaxpayerType


class Fop(DataOceanModel):
    fullname = models.CharField("повне ім'я", max_length=175)
    address = models.CharField('адреса', max_length=500, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='статус')
    registration_date = models.DateField('дата реєстрації', null=True, blank=True)
    registration_info = models.CharField('реєстраційні дані', max_length=300, null=True, blank=True)
    estate_manager = models.CharField(max_length=125, null=True, blank=True)
    termination_date = models.DateField(null=True, blank=True)
    terminated_info = models.CharField(max_length=300, null=True, blank=True)
    termination_cancel_info = models.CharField(max_length=275, null=True, blank=True)
    contact_info = models.CharField('контакти', max_length=200, null=True, blank=True)
    vp_dates = models.CharField(max_length=240, null=True, blank=True)
    authority = models.ForeignKey(Authority, on_delete=models.CASCADE,
                                  verbose_name='орган реєстрації', null=True, blank=True)
    code = models.CharField(max_length=675, db_index=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.fullname

    class Meta:
        ordering = ['id']
        verbose_name = 'фізична особа-підприємець'


class FopToKved(DataOceanModel):
    fop = models.ForeignKey(Fop, related_name='kveds', on_delete=models.CASCADE, db_index=True,
                            verbose_name='ФОП')
    kved = models.ForeignKey(Kved, on_delete=models.CASCADE, verbose_name='КВЕД')
    primary_kved = models.BooleanField('зазначений як основний', default=False)

    def __str__(self):
        return f"{self.kved} (зазначений як основний)" if self.primary_kved else f"{self.kved}"

    class Meta:
        verbose_name = 'КВЕДи ФОП'


class ExchangeDataFop(DataOceanModel):
    fop = models.ForeignKey(Fop, related_name='exchange_data', on_delete=models.CASCADE,
                            db_index=True, verbose_name='ФОП')
    authority = models.ForeignKey(Authority, null=True, on_delete=models.CASCADE,
                                  verbose_name='орган реєстрації')
    taxpayer_type = models.ForeignKey(TaxpayerType, null=True, on_delete=models.CASCADE,
                                      verbose_name='тип платника податків')
    start_date = models.DateField(null=True)
    start_number = models.CharField(max_length=30, null=True)
    end_date = models.DateField(null=True)
    end_number = models.CharField(max_length=30, null=True)
