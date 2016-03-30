import core.models as CoreModels
import csv

class CSVGenerator:

    def generate_front(self, order, outputLocation):
        with open(outputLocation, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(['name', 'origin', 'ripens', 'date'])
            for entry in self.__order_entries(order.iterate_entries()):
                for i in range(entry.count):
                    data = [self.__get_formatted_name(entry.cultivar),
                            str(entry.cultivar.origin),
                            entry.cultivar.ripens,
                            entry.cultivar.origin_date,
                            ]
                    writer.writerow(data)
            pass
        pass

    def generate_back(self, order, outputLocation):
        with open(outputLocation, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(['name', 'spread'])
            for entry in self.__order_entries(order.iterate_entries()):
                for i in range(entry.count):
                    data = [entry.rootstock.name,
                            self.__create_spread_string(entry.rootstock)
                            ]
                    writer.writerow(data)
            pass
        pass

    def __create_spread_string(self, rootstock):
        return '{0}-{1}ft'.format(rootstock.min_width, rootstock.max_width)

    def __get_formatted_name(self, cultivar):
        return '{0} {1}'.format(cultivar.name, cultivar.species.name)

    def __order_entries(self, entries):
        return sorted(entries, key=lambda entry: entry.cultivar.name)
