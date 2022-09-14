import csv
from json.tool import main
from operator import itemgetter
print("--------Welcome To Matrimony--------")

class Matrimony:
    filename="assesment.csv"

    def __init__(self,name='',age='',salary='',religion='',hobby='',occupation='',gender=''):
        self.name=name
        self.age=age
        self.salary=salary
        self.religion=religion
        self.hobby=hobby
        self.occupation=occupation
        self.gender=gender
    def insertion(self):
        self.name=(input("enter name:"))
        self.age=input("enter DOB(dd/mm/yyyy):")
        self.occupation=input("enter occupation:")
        self.gender=input("enter gender:")
        self.religion=input("enter religion:")
        self.salary=input("enter your salary info:")
        self.hobby=input("enter your hobby:")

        with open(self.filename,'a',newline='')as file:
            csvwriter=csv.writer(file)
            csvwriter.writerow([self.name,self.age,self.occupation,self.gender,self.religion,self.salary,self.hobby])
        print("Details inserted")

    def retrival(self):
        with open(self.filename,'r')as file:
            data=csv.reader(file)
            for row in list(data):
                print("\n","name:",row[0],"\n","Date of Birth:",row[1],"\n","occupation:",row[2],"\n","Gender:",row[3],"\n","Religion:",row[4],"\n","Salary:",row[5],"\n","Hobby:",row[6],"\n")
        print("saved successfully")
    

    def searching(self):
        numb=input("enter name to find:")
        with open(self.filename,'r') as file:
            data = csv.reader(file)
            ml=list(data)
            searchresult=[memb for memb in ml if numb in memb]
            if len(searchresult)>0:
                for row in searchresult:
                    print("\n","name:",row[0],"\n","Date of Birth:",row[1],"\n","occupation:",row[2],"\n","Gender:",row[3],"\n","Religion:",row[4],"\n","Salary:",row[5],"\n","Hobby:",row[6],"\n")
    
    def deletion(self):
        dele=input("enter the person name to delete:")
        with open(self.filename,'r') as file:
            data=csv.reader(file)
            ml=list(data)
            delete_result=[memb for memb in ml if dele!=memb[0]]
        with open(self.filename,'w',newline='')as file:
            csvwr=csv.writer(file)
            csvwr.writerows(delete_result)
            if(len(delete_result)==len(ml)):
                print("No data such kind exist")
            else:
                print("updated data")


        
def main():
    a=Matrimony()

    while(1):
        print("menu")
        print("1.Insertion")
        print("2.Modification")
        print("3.Retrival")
        print("4.Searching")
        print("5.Recommandation")
        print("6.Deletion")

        b=int(input("\nEnter your choice:"))
        if(b==1):
            a.insertion()
        elif(b==2):
            a.modification()
        elif(b==3):
            a.retrival()
        elif(b==4):
            a.searching()
        elif(b==5):
            a.recommandation()
        elif(b==6):
            a.deletion()
        else:
            print("invalid choice")
main()

