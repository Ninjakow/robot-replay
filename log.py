import csv
import time

from networktables import NetworkTables


class Log:

    def __init__(self, team):
        # NetworkTables.startClientTeam(team)
        NetworkTables.initialize(server="localhost")
        now = "logs/" + str(time.time()) + ".csv"
        self.file = csv.writer(open(now, "w"), delimiter=" ")

    def log(self):
        entries = NetworkTables.getEntries("")
        for entry in entries:
            print(entry.key, entry.value)
            self.file.writerow(str(entry.key))
            # self.file.writelines(str(entry.value))


logging = Log(4774)
while True:
    logging.log()
    time.sleep(1 / 50)
