import os

#
class SSH:
    @staticmethod
    def execit(cmd):
        output = os.system(cmd)
        return output
