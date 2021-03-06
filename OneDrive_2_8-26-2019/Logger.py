from datetime import *

class Logger:
    def __init__(self, path):
        self.path = path    
        self.log_list = ''

    def add_log(self, log_type: object, log_msg: object) -> object:
        self.log_list += '\n' + '[' + \
                        datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ']' + \
                        '[' + log_type + ']:' + log_msg

    def add_log_details(self, log_msg):
        self.log_list += '\n'+ (' '*28) + log_msg

    def append_sublog(self, log):
        self.log_list += log

    def get_log(self):
        return self.log_list

    def print_log(self):
        log_file = self.path + '\\tsql_convert_' + datetime.now().strftime('%m-%d-%Y_%H-%M-%S') + '.log'
        with open(log_file, 'w') as f:
            f.write(self.get_log())