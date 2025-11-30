import random
import time
import json
import uuid
from concurrent.futures import ThreadPoolExecutor


names = ['tushar', 'rishabh', 'vishvesh', 'karan', 'harsh', 'aman', 'naman']
courses = ['BCA', "Btech", "BBA", "MBA", "Bftech", "BJMC"]
ages = [19, 20, 21, 22, 23, 24]
genders = ['male', 'female']
locations = ['delhi', 'noida', "gurugram", 'harayna', 'punjab', 'sikkim']


def create_student():
    name_of_student = random.choice(names)
    course_of_student = random.choice(courses)
    age_of_student = random.choice(ages)
    gender_of_student = random.choice(genders)
    location_of_student = random.choice(locations)
    time.sleep(2)
    data = dict()
    data['id'] = str(uuid.uuid4())
    data['name'] = name_of_student
    data['course'] = course_of_student
    data['age'] = age_of_student
    data['gender'] = gender_of_student
    data['location'] = location_of_student
    file_name = f"{name_of_student}_{course_of_student}_{location_of_student}.json"

    with open(f"data/{file_name}", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"{file_name} saved")


def multiple(n: int):
    for i in range(n):
        create_student()


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(multiple(100))
