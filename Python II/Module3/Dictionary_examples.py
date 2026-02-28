#The Python list stores a collection of objects in an ordered sequence. 
#In contrast, the dictionary stores objects in an unordered collection. 
#Give three examples of real-world objects that can be stored in a dictionary.

#I have created three examples of real-world objects that can be stored in a dictionary:

student = {
    "name": "Meera",
    "gender": "female",
    "date_of_birth": "01/02/2013",
    "school_name": "ABC school",
    "academic_year": "2023-2024",
    "grade": "5th",
    "score": {
        "maths": 90,
        "english": 85,
        "science": 92,
        "history": 88
    }
}
print(student)

Architecture = {
    "building_name": "Empire State Building",   
    "location": "New York City, USA",
    "height": "1,454 feet (443.2 meters)",
    "floors": 102,
    "year_completed": 1931,
    "architect": "Shreve, Lamb & Harmon",
    "occupied_by": {
        "offices": 85,
        "observation_deck": 15
    }    
}
print(Architecture)

Python_course = {
    "course_name": "Introduction to Python Programming",    
    "instructor": "John Doe",
    "duration": "10 weeks", 
    "level": "Beginner",
    "topics_covered": [
        "Python basics",
        "Data structures",
        "Object-oriented programming",
        "Web development with Python",
        "Data analysis with Python"
    ],
    "enrollment": { 
        "total_students": 150,
        "active_students": 120,
        "completed_students": 30
    }   
}
print(Python_course)

