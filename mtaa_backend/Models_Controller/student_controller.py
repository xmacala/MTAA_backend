from flask import Flask, jsonify, request


def create_student(students, student_schema, db,student_id):
    fullname = request.json['fullname']
    phonenumber = request.json['phonenumber']
    contacts = request.json['contacts']
    height = request.json['height']
    weight = request.json['weight']
    hobby = request.json['hobby']
    haircolor = request.json['haircolor']
    bodytype = request.json['bodytype']
    photo = request.json['photo']
    student = students(fullname, phonenumber, contacts, height, weight, hobby, haircolor, bodytype, photo, student_id)
    db.session.add(student)
    db.session.commit()
    return student_schema.jsonify(student)


def get_student(students, student_schema, student_id):
    student = students.query.get(student_id)
    return student_schema.jsonify(student)


def update_student(students, db, student_schema, id):
    student = students.query.get(id)
    fullname = request.json['fullname']
    phonenumber = request.json['phonenumber']
    contacts = request.json['contacts']
    height = request.json['height']
    weight = request.json['weight']
    hobby = request.json['hobby']
    haircolor = request.json['haircolor']
    bodytype = request.json['bodytype']
    photo = request.json['photo']
    student.fullname = fullname
    student.phonenumber = phonenumber
    student.contacts = contacts
    student.height = height
    student.weight = weight
    student.hobby = hobby
    student.haircolor = haircolor
    student.bodytype = bodytype
    student.photo = photo
    db.session.commit()
    return student_schema.jsonify(student)