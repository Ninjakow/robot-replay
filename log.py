import csv
import time

from networktables import NetworkTables


class Log:

    def __init__(self, team):
        NetworkTables.startClientTeam(team)
        # NetworkTables.initialize(server="localhost")
        match_type = NetworkTables.getTable("FMSInfo").getValue("MatchType",
                                                                defaultValue="")
        self.file_name = "logs/" + str(time.time()) + str(match_type) + ".csv"
        self.writer = csv.writer(open(self.file_name, "w"), delimiter=",")
        self.reader = csv.reader(open(self.file_name, "r"), delimiter=",")

    def log(self):
        """Get all entries from NetworkTables and log to csv file."""
        entries = NetworkTables.getEntries("")
        for entry in entries:
            # print(entry.key, entry.value)
            self.writer.writerow([entry.key, entry.value])

    def read(self):
        return list(self.reader)


# logging = Log(4774)
# for x in range(100):
#     logging.log()
#     time.sleep(1/50)
# print(logging.read())
