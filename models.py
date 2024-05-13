class TimeEntry:
    def __init__(self, source, intensity, voltage):
        self.source = source
        self.intensity = intensity
        self.voltage = voltage

class Zone:
    def __init__(self):
        self.time_entries = {}

    def add_time_entry(self, timestamp, time_entry):
        self.time_entries[timestamp] = time_entry

class Site:
    def __init__(self):
        self.zones = {}

    def add_zone(self, zone_name):
        self.zones[zone_name] = Zone()

    def get_zone(self, zone_name):
        return self.zones.get(zone_name)

class Data:
    def __init__(self):
        self.sites = {}

    def add_site(self, site_name):
        self.sites[site_name] = Site()

    def get_site(self, site_name):
        return self.sites.get(site_name)
