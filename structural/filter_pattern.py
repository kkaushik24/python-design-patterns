from abc import ABCMeta, abcmethod
class Person:

    def __init__(self, name, gender, marital_status):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status

    def get_name(self):
        return self.name
    
    def get_gender(self):
        return self.gender

    def get_marital_status(self):
        return self.marital_status


class Criteria:

   __metaclass__ = ABCMeta

    @abcmethod
    def meet_criteria(self, person_list):
        pass

    

class CriteriaMale(Criteria):

    def meet_criteria(self, person_list):
        male_person_list = []
        for person in person_list:
            if person.get_gender() == "Male":
                male_person_list.append(person)
        
        return male_person_list


class CriteriaFemale(Criteria):

    def meet_criteria(self, person_list):
        female_person_list = []
        for person in person_list:
            if person.get_gender() == "Female":
                female_person_list.append(person)
        
        return female_person_list


        
