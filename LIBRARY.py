class multiFunction():

    def Subfields():
        list= ["Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in list:
            print(temp)
            
    def Elegible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))

        if (gender == "male") and (age >= 21):
            print("ELIGIBLE")
        elif (gender == "female") and (age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    def percentage():
        subject1=int(input("subject1="))
        subject2=int(input("subject2="))
        subject3=int(input("subject3="))
        subject4=int(input("subject4="))
        subject5=int(input("subject5="))
        total = subject1+subject2+subject3+subject4+subject5
        percentage= total/500 * 100
        print("Total:",(total))
        print("Percentage:",(percentage))
        
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        areaformula= (height*breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(areaformula))
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth2:"))
        Perimeterformula= height1+height2+breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",(Perimeterformula))
        
    def oddEven():
        oddEven=int(input("Enter a number: "))
        if (oddEven%2==0):
            print(oddEven,"is Even number")
        else:
            print(oddEven,"is odd number")
