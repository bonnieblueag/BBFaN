from django.db import models
from django.contrib.auth.models import User
import core.models as CoreModels

class NurseryLabelOrder(CoreModels.BaseModel):
    user = models.ForeignKey(User)

    def __str__(self):
        return '{0}: {1} - x{2}'.format(self.created_date.strftime('%Y%m%d-%H:%M:%S'), self.user.username,
                                     self.count_total_labels())

    def iterate_entries(self):
        return LabelEntry.objects.filter(order=self)

    def count_total_labels(self):
        labels = list(LabelEntry.objects.filter(order=self))
        count = 0
        for l in labels:
            count += l.count
        return count

class LabelEntry(CoreModels.BaseModel):
    order = models.ForeignKey(NurseryLabelOrder)
    cultivar = models.ForeignKey(CoreModels.Cultivar)
    rootstock = models.ForeignKey(CoreModels.Rootstock)
    count = models.PositiveIntegerField()

    def __str__(self):
        return '{0}x {1} - {2} on {3} Rootstock'.format(self.count, self.cultivar.species.name, self.cultivar.name,
                                                        self.rootstock.name)


