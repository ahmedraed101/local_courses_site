from os import listdir, path

class Courses():
    def __init__(self):
        self.courses = listdir('app/static/courses')
        
    
    def get_courses(self):
        return self.courses

class Course():
    def __init__(self, coursename):
        self.courseName = coursename
        self.courseContent = listdir(f'app/static/courses/{self.courseName}')
        
    def get_course_content(self):
        sortedContent = []
        for i in self.courseContent:
            if not i.endswith(".json"):
                sortedContent.append(i)
        sortedContent = sorted(sortedContent, key=self.order)
        return sortedContent

    def order(self,e):
        return int(e[0:2])


# if you want to run it remove 'app/' from the path  
# if __name__ == '__main__':
#     c = Courses()
#     print(c.get_courses())