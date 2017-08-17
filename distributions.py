import criminal_data as cd 
from itertools import groupby
from operator import attrgetter
from collections import OrderedDict

def distribution(inmates, attribute):
    ''' prepares distribution data wrt attribute '''
    dist = dict()
    sorted_inmates = OrderedDict(sorted(inmates.items(), 
                     key = lambda x: attrgetter(attribute)(x[1])))
    for attr, gr in groupby(sorted_inmates.items(), 
                            key = lambda x: attrgetter(attribute)(x[1])):
        dist[attr] = len(list(gr))
    return dist

def prepare_distributions():
    ''' prepares distributions of inmates wrt to age, race and sex '''
    how_many = 5
    inmates = cd.download_data() 
    # inmates = cd.download_data(how_many) 
    age  = distribution(inmates, 'age')
    race = distribution(inmates, 'race')
    sex  = distribution(inmates, 'sex')
    return age, race, sex

if __name__ == '__main__':
    prepare_distributions()

