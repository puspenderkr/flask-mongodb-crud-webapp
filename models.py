from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient("mongodb://localhost:27017/")
db = client["student_database"]
students_collection = db["students"]


class Student:
    @staticmethod
    def create_student(data):
        result = students_collection.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def get_all_students():
        students = students_collection.find()
        return list(students)

    @staticmethod
    def get_student_by_id(student_id):
        student = students_collection.find_one({"_id": ObjectId(student_id)})
        return student

    @staticmethod
    def update_student(student_id, data):
        result = students_collection.update_one(
            {"_id": ObjectId(student_id)}, {"$set": data}
        )
        return result.modified_count > 0

    @staticmethod
    def delete_student(student_id):
        result = students_collection.delete_one({"_id": ObjectId(student_id)})
        return result.deleted_count > 0


student_model = Student()
