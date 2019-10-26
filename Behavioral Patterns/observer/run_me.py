if __name__ == "__main__":

    from observer.observer import to_father, to_mother, to_hospital
    from observer.student import Student

    observers = [to_father, to_mother]

    call_to_parents = Student(
        'Harry',
        'James',
        'Lilian',
        'Princetown Hospital', observers=observers)

    observers = [to_hospital]

    call_to_hospital = Student(
        'Taylor',
        'Scott',
        'Suzan',
        'NY Hospital',
        observers=observers)
