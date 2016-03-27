from django.db import models
from django.core.validators import RegexValidator

MONTH_CHOICES = (
    ('Jan', 'January'),
    ('Feb', 'February'),
    ('Mar', 'March'),
    ('Apr', 'April'),
    ('May', 'May'),
    ('Jun', 'June'),
    ('Jul', 'July'),
    ('Aug', 'August'),
    ('Sep', 'September'),
    ('Oct', 'October'),
    ('Nov', 'November'),
    ('Dec', 'December'),
)

DWARFING_CHOICES = (
    ('Dw', 'Dwarf'),
    ('Sd', 'Semi-Dwarf'),
    ('Fs', 'Full Size'),
)

def get_fields(obj_type):
    f = tuple([f for f in obj_type._meta.get_all_field_names()])
    return f



class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Location(BaseModel):
    center = models.CharField(max_length=255, blank=False, null=True)
    state = models.CharField(max_length=255, blank=False, null=True)
    country = models.CharField(max_length=255, blank=False, null=True)
    latitude = models.CharField(max_length=255, blank=False, null=True)
    longitude = models.CharField(max_length=255, blank=False, null=True)

    class Meta:
        unique_together = ('center', 'state', 'country')


class Species(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{0}'.format(self.name)


class Rootstock(BaseModel):
    species = models.ForeignKey(Species)
    name = models.CharField(max_length=255)
    max_height = models.PositiveIntegerField()
    max_width = models.PositiveIntegerField()
    dwarfing = models.CharField(max_length=2, choices=DWARFING_CHOICES)

    class Meta:
        unique_together=('species', 'name')

    def __str__(self):
        return self.name

class RootstockInventory(BaseModel):
    rootstock = models.ForeignKey(Rootstock)
    on_hand = models.PositiveIntegerField()


class ScionSource(BaseModel):
    contact = models.CharField(max_length=255)
    email = models.EmailField()
    phoneValidator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phoneValidator], blank=True)


class FruitUse(BaseModel):
    use = models.CharField(max_length=255, unique=True)


class Cultivar(BaseModel):
    sources = models.ManyToManyField(ScionSource)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    ripens = models.CharField(max_length=255)
    origin = models.ForeignKey(Location, on_delete=models.PROTECT)
    origin_date = models.CharField(max_length=255)
    uses = models.ManyToManyField(FruitUse)
    is_pollen_sterile = models.BooleanField(default=False)

    class Meta:
        unique_together = ('species', 'name')

    def __str__(self):
        return '{0}-{1}'.format(self.species.name, self.name)


class Scion(BaseModel):
    cultivar = models.ForeignKey(Cultivar, on_delete=models.PROTECT)
    on_hand = models.PositiveIntegerField()


class Pot(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    on_hand = models.PositiveIntegerField()
    volume = models.PositiveIntegerField(blank=True, null=True)


class GraftedTree(BaseModel):
    scion = models.ForeignKey(Cultivar)
    rootstock = models.ForeignKey(Rootstock)
    on_hand = models.PositiveIntegerField()
    pot = models.ForeignKey(Pot)


class SeedlingInfo(BaseModel):
    species = models.ForeignKey(Species)
    name = models.CharField(max_length=255)
    parentage = models.CharField(max_length=255)

    class Meta:
        unique_together = ('species', 'name')


class SeedlingTree(BaseModel):
    info = models.ForeignKey(SeedlingInfo)
    min_size = models.PositiveIntegerField()
    max_size = models.PositiveIntegerField()
    on_hand = models.PositiveIntegerField()


