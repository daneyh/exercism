class Garden:
    
    def __init__(self, diagram, students=['Alice','Bob','Charlie','David','Eve','Fred','Ginny','Harriet','Ileana','Joseph','Kincaid','Larry']):
        self.diagram = diagram
        self.students = students
        self.students.sort()
        self.rows = diagram.split('\n')
        # #Alice, Bob, Charlie, David,
        #Eve, Fred, Ginny, Harriet,
        #Ileana, Joseph, Kincaid, and Larry.

    def plants(self,student):
        plant_dict = {'V':'Violets','C':'Clover','R':'Radishes','G':'Grass'}
        student_plants = []
        position = {}
        position[student] = (((self.students.index(student) + 1)*2)-1),((self.students.index(student) + 1)*2)
        for x in self.rows:
            for y in position[student]:
                student_plants.append(plant_dict[x[y-1]])
        return student_plants

            
        
            
        


   
