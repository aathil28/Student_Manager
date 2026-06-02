#entry point to the application

def main():
    #to collect and store student information
    students = []
while True:
    print('====MENU====')
    print('1. Add student')
    print('2. View students')
    print('3. View all students')
    print('4. Exit')
    user_choice = input('enter your choice :')

    if (user_choice == '1'):
        ##method to add students
        pass
    elif (user_choice == '2'):
        ##method to add scholarship students
        pass
    elif (user_choice == '3'):
        ##display entries in 'students'
        print('Third choice selected.')
    elif (user_choice == '4'):
        status = False
        print('Exiting the programme...')
        break
    else :
        print('Invalid choice.')

main()
#initialize python project (starting point of the application)
if __name__ == '__main__':
    main()