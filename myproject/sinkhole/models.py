from django.db import models

class SinkholeIncident(models.Model):
    date = models.DateField(verbose_name="발생일시")
    location = models.CharField(max_length=200, verbose_name="위치")
    cause = models.TextField(blank=True, verbose_name="발생 원인")
    depth = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="깊이(m)")
    # 필요에 따라 추가 필드 작성
    
    def __str__(self):
        return f"{self.date} - {self.location}"

class MaterialUsage(models.Model):
    incident = models.ForeignKey(SinkholeIncident, on_delete=models.CASCADE,
                                 related_name="materials", verbose_name="관련 사고")
    material = models.CharField(max_length=100, verbose_name="자재명")
    quantity = models.FloatField(verbose_name="수량")
    unit = models.CharField(max_length=50, default="개", verbose_name="단위")
    
    def __str__(self):
        return f"{self.material}: {self.quantity}{self.unit}"