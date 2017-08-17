import distributions as db
from matplotlib import pyplot as plt

def prepare_barplot(d):
    ''' prepares a bar chart from a dictionary '''
    n = len(d)
    fig = plt.figure(figsize=(8, 6))
    if d.keys()[0].isdigit():
        keys = map(int, d.keys())
        plt.bar(keys, d.values(), align = 'center')
    else:
        keys = range(n)
        plt.bar(range(n), d.values(), align = 'center')
        plt.xticks(range(n), d.keys())
    return fig

def show_distributions():
    ''' prepares plots with distributions '''
    attributes = db.prepare_distributions()
    names = ['age', 'race', 'sex']
    for i, attr in enumerate(attributes):
        fig = prepare_barplot(attr)
        fig.savefig('plots/'+ names[i] +'.png')
        # plt.show()

if __name__ == '__main__':
    show_distributions()
