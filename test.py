from nepalithar import Caste


caste_obj = Caste()
print(caste_obj.get(1))
print(caste_obj.detect("Rajhesh hamal Subash Ghimire"))
print("घिमिरे",caste_obj.is_caste(" घिमिरे "))
print(caste_obj.get_position("शुभस घिमिरे Madhu Bhattarai"))
print(caste_obj.split_name("Rajesh Hamal Madhu Bhattarai"))
