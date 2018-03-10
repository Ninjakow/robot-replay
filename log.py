import csv
import time

from networktables import NetworkTables


class Log:

    def __init__(self, team):
        NetworkTables.startClientTeam(team)
        match_type = NetworkTables.getTable("FMSInfo").getValue("MatchType",
                                                                defaultValue="")
        self.file_name = "logs/" + time.strftime("%H-%M-%S %d-%m-%y") + \
            str(match_type) + ".csv"
        self.writer = csv.writer(open(self.file_name, "w"), delimiter=",")
        self.reader = csv.reader(open(self.file_name, "r"), delimiter=",")

    def log(self):
        """Get all entries from NetworkTables and log to csv file."""
        entries = NetworkTables.getEntries("")
        current_time = time.monotonic()
        for entry in entries:
            self.writer.writerow([entry.key, entry.value, current_time])

    def read(self):
        return list(self.reader)
