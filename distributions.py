import criminal_data as cd 
from itertools import groupby
from operator import attrgetter
from collections import OrderedDict

def race_distribution(inmates):
    sorted_inmates = OrderedDict(sorted(inmates.items(), key = lambda x: attrgetter('race')(x[1])))
    for inmate, details in sorted_inmates.items():
        print inmate, details.race
    # print sorted_inmates

def prepare_distributions():
    how_many = 15
    inmates = cd.download_data(how_many) 
    race_distribution(inmates)
    print len(inmates)

if __name__ == '__main__':
    prepare_distributions()
