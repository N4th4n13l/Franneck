# Dictionarys Comp |

studenten = ['Jan', 'Horst', 'Peter']
noten = [1, 3 , 5]

stud_dict = {'Jan': 1, 'Horst': 2, 'Peter': 3}
print(stud_dict)

stud_dictNew = {key: val for key, val in zip(studenten, noten)}
print(stud_dictNew)