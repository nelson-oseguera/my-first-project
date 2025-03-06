# Nelson Oseguera

# February 19th, 2023

# Project 1

# This program will take in basic student information such as student's name, degree name, the number of credits required for the degree, and the amount of credits taken. The program will then calculate the amount of credits left to graduate.

print('Enter student name: ')

studentName=input()

print('Enter degree program: ')

degreeName=input()

print('Enter Credits required for degree: ')

creditsDegree=int(input())

print('Enter Credits taken: ')

creditsTaken=int(input())

creditsLeft = (creditsDegree - creditsTaken)

print('The student\'s name is', studentName)

print('The degree program is', degreeName)

print('This means there are', creditsLeft , 'credits left until graduation')



