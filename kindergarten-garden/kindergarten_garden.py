students = {'Alice':'Violets Radishes Violets Radishes'
            ,'Bob':'Clover Grass Clover Clover'
            , 'Charlie':'Violet Violet Clover Grass'
            , 'David':'Radishes Violet Clover Radishes'
            , 'Eve':'Clover Grass Radishes Grass'
            , 'Fred':'Grass Clover Violet Clover'
            , 'Ginny':'Clover Grass Grass Clover'
            , 'Harriet':'Violet Radishes Radishes Violet'
            , 'Ileana':'Grass Clover Violet Clover'
            , 'Joseph':'Violet Clover Violet Grass'
            , 'Kincaid':'Grass Clover Clover Grass'
            , 'Larry':'Grass Violet Clover Violet'}

def Garden(plants):
    return "".join(plant[0] for plant in plants).upper()

def main(students):
    name = input("Enter Student Name : ")
    x = students[name]
    plants = x.split()
    print(f"{name}'s Plants {Garden(plants)}")

if __name__ == "__main__":
    main(students)
