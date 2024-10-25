from django.db import models

class ATM(models.Model):
    name = models.CharField(max_length=100)
    bunker_size = models.IntegerField()
    expected_incoming = models.FloatField()
    expected_outgoing = models.FloatField()
    location = models.PointField()

    def __str__(self):
        return self.name

class Insurer(models.Model):
    name = models.CharField(max_length=100)
    group_id = models.IntegerField()
    start_location = models.PointField()
    end_location = models.PointField()
    working_hours = models.IntegerField()

    def __str__(self):
        return self.name

class Route(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    distance = models.FloatField()
    bunker_status = models.BooleanField()
    group_id = models.ForeignKey(Insurer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"
