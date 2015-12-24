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


class CriteriaSingle(Criteria):

    def meet_criteria(self, person_list):
        single_person_list = []
        for person in person_list:
            if person.get_marital_status() == "Single":
                single_person_list.append(person)
        
        return single_person_list

class CriteriaOr(Criteria):

    def __init__(self, criteria, other_criteria):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def meet_criteria(self, person_list):
        first_criteria_items = self.criteria.meet_criteria(person_list)
        second_criteria_items = self.other_criteria.meet_criteria(person_list)

        for person in other_criteria_items:
            if person not in first_criteria_items:
                first_criteria_items.append(person)

        return first_criteria_items


class CriteriaAnd(Criteria):

    def __init__(self, criteria, other_criteria):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def meet_criteria(self, person_list):
        first_criteria_items = self.criteria.meet_criteria(person_list)
        return self.other_criteria.meet_criteria(first_criteria_items)


if __name__ == '__main__':
    person_list = []
    person_list.append(Person('A','Male', 'Single'))
    person_list.append(Person('B','Female', 'Married'))

    male = CriteriaMale()
    female = CriteriaFemale()
    single = CriteriaSingle()




