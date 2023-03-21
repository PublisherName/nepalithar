PRODUCTION = True
if PRODUCTION:
    from nepalithar.helper import *
else:
    from helper import CasteHelper
import random

class Caste(CasteHelper):
    
    def detect(self, input_string):
        word_list = input_string.strip().split(" ")
        index = [(i, word) for i, word in enumerate(word_list) if self._is_present(word.upper())]
        return index

    def is_caste(self,caste):
        return self._is_present(caste)

    def get(self, n=1):
        return self._get_random_caste(n)

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
                if index + 1 < len(raw_name) and self._is_present(raw_name[index]) and self._is_present(raw_name[index + 1]):
                    pass
                else:
                    name_bucket.append(' '.join(raw_name[0 if len(name_bucket) == 0 else previous + 1:index + 1]))
                    previous = index
        return ([name.title() for name in name_bucket])