class SchoolAdmission:

    def __init__(self, file):
        self.capacity = int(input())
        self.applicants = [line.split() for line in file.read().split('\n')]
        self.departments = dict(Biotech=[], Chemistry=[], Engineering=[], Mathematics=[], Physics=[])
        self.registered = []
        self.place_applicants()

    def place_applicants(self):
        for priority in range(7, 10):
            for choice in self.departments:
                applicants = self.sort_applicants(choice, priority)
                for applicant in applicants:
                    if applicant[:2] not in self.registered and len(self.departments[choice]) < self.capacity:
                        student = f'{applicant[0]} {applicant[1]} {float(applicant[2])}'
                        self.departments[choice].append(student)
                        self.registered.append(applicant[:2])
                    else:
                        pass
        self.display_departments()
        self.save_results()

    def sort_applicants(self, choice, priority):
        applicants = []
        for student in self.applicants:
            if student[priority] == choice:
                index = self.review_exam(choice)
                grade = (int(student[index[0]]) + int(student[index[1]])) / 2
                applicants.append(student[:2] + [max(grade, int(student[6]))])
        applicants.sort(key=lambda x: (-float(x[2]), x[0]))
        return applicants

    @staticmethod
    def review_exam(choice):
        if choice == 'Physics':
            return [2, 4]
        elif choice == 'Mathematics':
            return [4, 4]
        elif choice == 'Engineering':
            return [5, 4]
        elif choice == 'Chemistry':
            return [3, 3]
        else:
            return [3, 2]

    def display_departments(self):
        for department in self.departments:
            self.departments[department].sort(key=lambda x: (-float(x.split()[2]), x.split()[0]))
            print(department, *self.departments[department], sep='\n', end='\n\n')

    def save_results(self):
        for department in self.departments:
            self.departments[department].sort(key=lambda x: (-float(x.split()[2]), x.split()[0]))
            with open(f'{department.lower()}.txt', 'w') as file:
                for applicant in self.departments[department]:
                    file.write(applicant + '\n')


if __name__ == '__main__':
    file = open('applicants.txt', 'r')
    SchoolAdmission(file)
    file.close()
