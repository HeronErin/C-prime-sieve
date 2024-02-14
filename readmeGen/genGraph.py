#  Copyright (C) 2024  HeronErin

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.

#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import matplotlib.pyplot as plt
import datetime, os

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