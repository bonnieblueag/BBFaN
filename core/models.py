from django.db import models
from django.core.validators import RegexValidator
from core.common import STATE_FULL_TO_AB

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
    f = tuple([f for f in obj_type._meta.get_fields()])
    return f



class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Address(BaseModel):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=5)


class Customer(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.ForeignKey(Address, null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

class Order(BaseModel):
    customer = models.ForeignKey(Customer)
    customer_name = models.CharField(max_length=255)
    order_placed_date = models.DateTimeField(blank=True, null=True)
    order_fullfilled_date = models.DateTimeField(blank=True, null=True)
    order_shipped_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.id, self.customer_name)


class Location(BaseModel):
    center = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        if self.center and self.state:
            abbrevState = STATE_FULL_TO_AB[self.state]
            return '{0}, {1}'.format(self.center, abbrevState)
        if self.state:
            return self.state
        return self.country

    class Meta:
        unique_together = ('center', 'state', 'country')


class Species(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{0}'.format(self.name)


class Rootstock(BaseModel):
    species = models.ForeignKey(Species)
    name = models.CharField(max_length=255)
    min_width = models.PositiveIntegerField()
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

    def __str__(self):
        return self.use


class Cultivar(BaseModel):
    sources = models.ManyToManyField(ScionSource, blank=True, null=True)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    ripens = models.CharField(max_length=255)
    origin = models.ForeignKey(Location, on_delete=models.PROTECT)
    origin_date = models.CharField(max_length=255, blank=True, null=True, default='Unknown')
    uses = models.ManyToManyField(FruitUse, blank=True, null=True)
    is_pollen_sterile = models.BooleanField(default=False)

    class Meta:
        unique_together = ('species', 'name')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Scion(BaseModel):
    cultivar = models.ForeignKey(Cultivar, on_delete=models.PROTECT)
    on_hand = models.PositiveIntegerField()

    def __str__(self):
        return self.cultivar.name


class Pot(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    on_hand = models.PositiveIntegerField()
    volume = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class GraftedStock(BaseModel):
    scion = models.ForeignKey(Cultivar)
    rootstock = models.ForeignKey(Rootstock)
    on_hand = models.PositiveIntegerField()
    pot = models.ForeignKey(Pot, null=True, blank=True)
    name_denormalized = models.CharField(max_length=255)

    class Meta:
        ordering = ('name_denormalized',)

    def __str__(self):
        return self.name_denormalized


class SeedlingInfo(BaseModel):
    species = models.ForeignKey(Species)
    name = models.CharField(max_length=255)
    parentage = models.CharField(max_length=255)

    class Meta:
        unique_together = ('species', 'name')

    def __str__(self):
        return self.name



class SeedlingTree(BaseModel):
    info = models.ForeignKey(SeedlingInfo)
    min_size = models.PositiveIntegerField()
    max_size = models.PositiveIntegerField()
    on_hand = models.PositiveIntegerField()
    name_denormalized = models.CharField(max_length=255)

    def __str__(self):
        return self.name_denormalized


