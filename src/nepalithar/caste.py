from nepalithar.helper import *
import random

class Caste(CASTE_HELPER):
       
    def is_true(self, caste):
        if not isinstance(caste, str):
            raise TypeError("Input parameter must be a string")
        if caste.strip():
            return caste.strip().upper() in self.get_caste_list()
        return False
    
    def detect(self, input_string):
        word_list = input_string.strip().split(" ")
        index = [(i, word) for i, word in enumerate(word_list) if word.upper() in self.get_caste_list()]
        return index

    def get(self, n=1):
        return random.sample(self.get_caste_list(), n)

    def get_position(self, string):
        caste_in = self.detect(string)
        caste_in_list = [position for position, _ in caste_in]
        return caste_in_list
    
    def split_name(self, string):
        name_bucket = []
        string = string.strip()
        raw_name = string.split(" ")
        caste_index = self.get_position(string)
        total_caste_found = len(caste_index)
        if total_caste_found <= 1:
            name_bucket.append(string)
        elif (total_caste_found > 1):
            previous = 0
            for _, index in enumerate(caste_index):
                if index + 1 < len(raw_name) and self.is_true(raw_name[index]) and self.is_true(raw_name[index + 1]):
                    pass
                else:
                    name_bucket.append(' '.join(raw_name[0 if len(name_bucket) == 0 else previous + 1:index + 1]))
                    previous = index
        return ([name.title() for name in name_bucket])
