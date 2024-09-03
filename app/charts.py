import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig('bar.png')
    plt.close()

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.axis()
    plt.savefig('pie.png')
    plt.close()

if __name__== '__main__':
    labels = ['a','b','c','d']
    values = [100,220,85,63.5]
    #generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)