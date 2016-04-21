import core.models as CoreModels
from core.models import Cultivar, Species, Location, FruitUse
import csv


class InventoryImport:

    def import_inventory(self, fileName):
        entriesAdded = 0
        with open(fileName) as inFile:
            reader = csv.reader(inFile, delimiter=',', quotechar='"')
            first = True
            typeToSpecies = {}
            for row in reader:
                if first:
                    first = False
                    print('Skipping header')
                    continue
                type = row[0]
                name = row[1]
                seedling = row[2]
                m111 = row[3]
                g11 = row[4]
                g222 = row[5]
                if type not in typeToSpecies:
                    species = CoreModels.Species.objects.filter(name=type).first()
                    typeToSpecies[type] = species
                species = typeToSpecies[type]

                cultivar = CoreModels.Cultivar.objects.filter(species__id=species.id, name=name).first()
                if not cultivar:
                    raise Exception('Could not find cultivar with Type: {0}, Name:{1}}'.format(type, name))

                if seedling != '':
                    if species.name == 'Apple':
                        self.__insert(species, cultivar, 'Seedling', int(seedling))
                    else:
                        self.__insert(species, cultivar, 'Callery', int(seedling))
                if m111 != '':
                    if species.name == 'Apple':
                        self.__insert(species, cultivar, 'M-111', int(m111))
                    else:
                        self.__insert(species, cultivar, 'OHx333', int(m111))
                if g11 != '':
                    self.__insert(species, cultivar, 'G-11', int(g11))
                if g222 != '':
                    self.__insert(species, cultivar, 'G-222', int(g222))






    def __insert(self, species, cultivar, rootstockName, count):
        rootstock = CoreModels.Rootstock.objects.filter(species__id=species.id, name=rootstockName).first()
        if not rootstock:
            raise Exception('Rootstock with name {0} does not exist.'.format(rootstockName))
        graftedStock = CoreModels.GraftedStock.objects.filter(scion__id=cultivar.id,
                                                                  rootstock__id=rootstock.id).first()
        print('Inserting {0} {1}'.format(cultivar.name, rootstockName))
        if not graftedStock:
            graftedStock = CoreModels.GraftedStock()
            graftedStock.scion = cultivar
            graftedStock.rootstock = rootstock
            graftedStock.on_hand = 0
            graftedStock.name_denormalized = '{0} {1}'.format(cultivar.name, rootstockName)
            graftedStock.save()
        graftedStock.on_hand = count
        graftedStock.save()
        return




class LegacyScionImport:

    def __get_location(self, origin, state, country):
        if country == 'USA':
            country = 'United States'

        center = origin
        if ',' in origin:
            # NON US scenario
            if state is None:
                center, country = origin.split(',', 1)
            else:
                center, stateSmall = origin.split(',', 1)
        else:
            center = None

        location = Location.objects.filter(country=country)
        if state:
            location = location.filter(state=state)

        location = location.filter(center=center).first()

        if not location:
            location = Location()
            location.center = center
            if not state:
                state = None
            location.state = state
            location.country = country
            location.save()

        return location


    def import_scion(self, csvFilePath):
        entriesAdded = 0
        with open(csvFilePath) as inFile:
            reader = csv.reader(inFile, delimiter=',', quotechar='"')
            first = True
            for row in reader:
                if first:
                    first = False
                    print('Skipping header')
                    continue
                name = row[1]
                type = row[2]
                ripens = row[3]
                origin = row[4]
                state = row[5]
                country = row[6]
                date = row[7]
                primary_use = row[8]
                secondary_use = row[9]
                story = row[10]
                shortStatement = row[11]
                isAvailable = row[12]
                isPollenSterile= row[13]

                species = Species.objects.filter(name=type).first()
                if not species:
                    species = Species()
                    species.name = type
                    species.save()

                cultivar = Cultivar.objects.filter(name=name)

                # Only adding in new entries
                if not cultivar:
                    cultivar = Cultivar()
                    cultivar.species = species
                    cultivar.name = name
                    cultivar.ripens = ripens
                    cultivar.origin = self.__get_location(origin, state, country)
                    cultivar.origin_date = date

                    uses = []
                    if primary_use:
                        use = FruitUse.objects.filter(use=primary_use)
                        if not use:
                            use = FruitUse()
                            use.use = primary_use
                            use.save()
                            uses.append(use)
                    if secondary_use:
                        use = FruitUse.objects.filter(use=secondary_use)
                        if not use:
                            use = FruitUse()
                            use.use = secondary_use
                            use.save()
                            uses.append(use)

                    print(isPollenSterile)
                    if isPollenSterile.lower() == 't':
                        cultivar.is_pollen_sterile = True
                    cultivar.save()
                    entriesAdded += 1

                    for use in uses:
                        cultivar.uses.add(use)
                    cultivar.save()









