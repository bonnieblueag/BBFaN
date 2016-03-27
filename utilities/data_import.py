from core.models import Cultivar, Species, Location, FruitUse
import csv

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









