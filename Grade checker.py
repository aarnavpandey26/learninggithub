def main():
    marks1=input("Enter marks of subject1: ")
    if not marks1.isdigit():
        print("Enter digits only")
        return
    marks2=input("Enter marks of subject2: ")
    if not marks2.isdigit():
        print("Enter digits only.")
        return
    marks3=input("Enter marks of subject3: ")
    if not marks3.isdigit():
        print("Enter digits only.")
        return
    marks4=input("Enter marks of subject4: ")
    if not marks4.isdigit():
        print("Enter digits only.")
        return

    marks1=int(marks1)
    marks2=int(marks2)
    marks3=int(marks3)
    marks4=int(marks4)

    sum=marks1+marks2+marks3+marks4
    grade=(sum/400)*100

    if grade>=90:
        print("You have gotten an A",grade)
    elif grade >=80 and grade<90:
        print("You have gotten a B",grade)
    elif grade>=70 and grade<80:
        print("You have gotten a C",grade)
    else:
        print("You have Failed bro",grade)


if __name__=='__main__':
    main()