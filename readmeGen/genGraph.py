import matplotlib.pyplot as plt
import datetime, os
# datetime_object = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S')

y = {}
x = {}
tests = []

with open(os.path.dirname(__file__)+"/../historicData.csv", "r") as output:
    output.readline()
    for line in output.readlines():
        if not line.strip(): continue
        date, test, comptime = line.strip().split(",")
        timeOfRun = datetime.datetime.strptime(date, '%m/%d/%Y %H:%M:%S')
        if not test in x:
            x[test] = []
            y[test] = []
            tests.append(test)
        x[test].append(timeOfRun)
        y[test].append(float(comptime))
for test in tests:
    fig, ax = plt.subplots( nrows=1, ncols=1 )

    plt.title(test + " Every 24 hours")
    plt.xlabel('Date')
    plt.ylabel('Secounds to run benchmark')

    ax.plot(x[test], y[test])
    
    fig.savefig(os.path.join(os.path.dirname(__file__), "..", "imgs", test.strip()+".png"))
    plt.close(fig)