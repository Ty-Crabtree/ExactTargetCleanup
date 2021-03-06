#pit-ftphost-02 /mnt/datastorage/ftphome/vanguardetproduction is where the files reside

import os
import glob
from csv import reader
import logging

class CLeanup:

    def __init__(self):
        self.base_path = '/mnt/datastorage/ftphome/vanguardetproduction'
        self.csv_list = []
        self.files_to_search = []
        self.logger = logging.getLogger('Cleanup')
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('cleanup.log')
        fh.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)

    def get_files_from_directory(self, test_path=None):
        if test_path:
            self.base_path = test_path
        self.files_to_search = glob.glob(self.base_path+'/*')

    def get_csv_files(self):
        with open('cleanup.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                self.csv_list.append(row[0])

    def delete_files(self):
        for file in self.files_to_search:
            for csv_file in self.csv_list:
                #self.logger.debug(file+" comparing to "+csv_file)
                #print(file+" comparing to "+csv_file)
                if csv_file in file:
                    self.logger.debug("Removing "+file)
                    print("Removing "+file)
                    try:
                        pass
                        #os.remove(file)
                    except Exception as e:
                        self.logger.debug("Couldn't remove file!")
                        self.logger.debug(e)

                        print("Couldn't remove file!")
                        print(e)

    def controller(self):
        print("Starting Cleanup on "+self.base_path)
        self.logger.debug("Starting Cleanup on "+self.base_path)
        self.get_files_from_directory()
        self.get_csv_files()
        self.delete_files()


if __name__ == '__main__':
    clean = CLeanup()
    clean.controller()
