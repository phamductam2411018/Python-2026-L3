import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self, course_list):
        if not self.marks:
            self.gpa = 0.0
            return 0.0
            
        mark_values = []
        credit_values = []
        
        for course in course_list:
            if course.id in self.marks:
                mark_values.append(self.marks[course.id])
                credit_values.append(course.credits)
                
        if len(credit_values) == 0:
            self.gpa = 0.0
            return 0.0
            
        marks_array = np.array(mark_values)
        credits_array = np.array(credit_values)
        
        weighted_sum = np.sum(marks_array * credits_array)
        total_credits = np.sum(credits_array)
        
        self.gpa = weighted_sum / total_credits
        return self.gpa