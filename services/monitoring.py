import psutil


class CPU:
    @staticmethod
    def load():
        return psutil.cpu_percent()

    @staticmethod
    def temp():
        temps = psutil.sensors_temperatures()
        if 'k10temp' in temps:
            return temps['k10temp'][0].current
        return None


class RAM:
    GB = 1024 ** 3
    @staticmethod
    def total():
        return round(psutil.virtual_memory().total / RAM.GB, 2)

    @staticmethod
    def used():
        return round(psutil.virtual_memory().used / RAM.GB, 2)

    @staticmethod
    def used_per():
        return round(psutil.virtual_memory().percent, 2)

    @staticmethod
    def free():
        return round(psutil.virtual_memory().available / RAM.GB, 2)


class DISK:
    GB = 1024 ** 3

    @staticmethod
    def total():
        return round(psutil.disk_usage('/home').total / DISK.GB, 2)

    @staticmethod
    def used():
        return round(psutil.disk_usage('/home').used / DISK.GB, 2)

    @staticmethod
    def used_per():
        return round(psutil.disk_usage('/home').percent, 2)

    @staticmethod
    def free():
        return round(psutil.disk_usage('/home').free / DISK.GB, 2)


class SYST:
    @staticmethod
    def avg_load():
        return psutil.getloadavg()[0] * psutil.cpu_count() #  # pyright: ignore[reportOperatorIssue]
