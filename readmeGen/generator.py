# Test on multiple optimization modes, update readme, and historicData.csv

# This should **NOT** be used with user input due to direct string formating with os.system() 


import os

from datetime import datetime, timedelta
from pytz import timezone

eastern = timezone('US/Eastern')
ranAt = datetime.now(tz=eastern).strftime('%m/%d/%Y %H:%M:%S')


def runTest(extent, flags):
    os.system(f"cd \"{os.path.dirname(__file__)}\"/.. && gcc main.c -o main -D EXTENT={extent} {flags} && ./main > /tmp/out")

    f = open("/tmp/out", "r")
    _, _, secs, _, numbs, *_ = f.read().split(" ")
    f.close()
    assert numbs == str(extent)
    
    return [numbs+" @ "+flags, secs]

results = [
        runTest(500_000, "-O0"),
        # runTest(500_000, "-O1"),
        # runTest(500_000, "-O2"),
        # runTest(500_000, "-O3"),

        # runTest(1_000_000, "-O0"),
        # runTest(1_000_000, "-O1"),
        # runTest(1_000_000, "-O2"),
        # runTest(1_000_000, "-O3"),

        # runTest(5_000_000, "-O0"),
        # runTest(5_000_000, "-O1"),
        # runTest(5_000_000, "-O2"),
        # runTest(5_000_000, "-O3"),
        ]

with open(os.path.dirname(__file__)+"/../historicData.csv", "a") as output:
    for test_name, r_time in results:
        print(test_name, r_time)
        output.write(f"{ranAt}, {test_name}, {r_time}\n")

with open(os.path.dirname(__file__)+"/../readme.md.template", "r") as template:
    with open(os.path.dirname(__file__)+"/../readme.md", "w") as output:
        while (line:=template.readline()) != "| :---          |          ---: |\n":
            output.write(line)
        for test_name, r_time in results:
            output.write(f"|{test_name}|{r_time}|\n")
        output.write(f"\n<sup><i>Generated at {ranAt} EST</i></sup>\n")
        output.write(template.read())