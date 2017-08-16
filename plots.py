import distributions as db
from matplotlib import pyplot as plt

def prepare_plot(d):
    ''' prepares a bar chart from a dictionary '''
    n = len(d)
    plt.bar(range(n), d.values(), align = 'center')
    plt.xticks(range(n), d.keys())
    plt.show()

def show_distributions():
    ''' prepares plots with distributions '''
    age, race, sex = db.prepare_distributions()
    prepare_plot(age)

if __name__ == '__main__':
    show_distributions()
