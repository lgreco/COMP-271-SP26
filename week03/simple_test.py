if __name__ == "__main__": 

    test_data = [
        ["Harry", "Potter", "Student"],
        ["Hermione", "Granger", "Student"],
        ["Ron", "Weasley", "Student"],
        ["Albus", "Dumbledore", "Headmaster"],
        ["Severus", "Snape", "Professor"],
        ["Minerva", "McGonagall", "Professor"],
        ["Rubeus", "Hagrid", "Gamekeeper"],
        ["Draco", "Malfoy", "Student"],
        ["Neville", "Longbottom", "Student"],
        ["Luna", "Lovegood", "Student"],
        ["Ginny", "Weasley", "Student"],
        ["Fred", "Weasley", "Student"],
        ["George", "Weasley", "Student"],
        ["Dolores", "Umbridge", "Professor"],
    ]

    test = Cast("Harry Potter")
    for item in test_data:
        # Magic values ok for brevity
        test.add_character(item[0], item[1], item[2])

    # add_unique
    print(test.add_unique("Dolores", "Umbridge", "Professor"))  # expect false
    print(test.add_unique("Rubeus", "Hagrid", "Gamekeeper"))  # expect false
    print(test.add_unique("Sirius", "Black", "Wizard"))  # expect true
    print(test.add_unique("Sirius", "Black", "Wizard"))  # expect false

    # remove
    print(test.remove("Leo", "Irakliotis", "Annoying Professor"))  # expect none
    print(test.remove("Sirius", "Black", "Wizard"))  # expect SBW