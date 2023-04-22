import glob
import os



class Filel:
    path = ''
    init_f = 1

    def __init__(self):
        self.path = Filel.path

    def setsf(self, string):
        self.path = string

    def last_f(self):  # '/home/NSO.LOC/bobav/share/Диск H/112/_Служба-112/_COVID/05.03.2023/справка/*'
        list_files = glob.glob(self.path)
        latest_file = max(list_files, key=os.path.getctime)
        print(latest_file)


def main():
    fs = Filel()
    fs.setsf('/home/NSO.LOC/bobav/share/Диск H/112/_Служба-112/_COVID/09.03.2023/справка/*')
    fs.last_f()


if __name__ == "__main__":
    main()
