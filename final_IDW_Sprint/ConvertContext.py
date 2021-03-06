from Logger import Logger

class ConvertContext():
    def __init__(self, in_arg):
        self.source_db = in_arg['source_db']
        self.target_db = in_arg['target_db']
        self.platform = in_arg['platform']
        self.in_code_type = in_arg['in_code_type']
        self.out_code_type = in_arg['out_code_type']
        self.source_dir = in_arg['source_dir']
        self.target_dir = in_arg['target_dir']
        self.logger = Logger(self.target_dir)

    def validate(self):
        #todo
        pass
        
    def showContext(self):
        return ' '*30 + 'source_db : ' + self.source_db + "\n" + ' '*30 + \
               'target_db : ' + self.target_db + "\n" + ' '*30 + \
               'platform : ' + self.platform + "\n" + ' '*30 + \
               'in_code_type : ' + self.in_code_type + "\n" + ' '*30 + \
               'out_code_type : ' + self.out_code_type + "\n" + ' '*30 + \
               'source_dir : ' + self.source_dir + "\n" + ' '*30 + \
               'target_dir : ' + self.target_dir
               
