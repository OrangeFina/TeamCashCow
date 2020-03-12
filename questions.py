import csv
import statistics


"""
for api

import requests
assume user input collected on jsx stored in variable "jsx" as string "a,b,a,c,a,b,a,c,a,a"
user_input = [requests.get('jsx')] #get response from front end and store it in a list
"""
raw_input = "c,b,b,c,b,b,b,c,b,a"
counter_input = 80 
# input will be provided by front end via api

counter_raw_data = [69,92,48,47,120,60,100,88,88,100,55,30,35,90,99,120,30,69,88,101,95,90,66,67,67,43,108,150,100,70]
user_input = raw_input.upper().split(",")

def risk_profiling():

    score = 0
    profile = ""

    for response in user_input:
        if response == "A":
            score += 1
        elif response == "B":
            score += 3
        elif response == "C":
            score += 5
    print(score)

    # assume dataset come in csv and convert it into a list
    sd = statistics.stdev(counter_raw_data)*2
    mean = statistics.mean(counter_raw_data)
    print(mean)
    print(sd)

    if counter_input <= mean - sd:
        score += 15
    elif counter_input > mean - sd and counter_input <= mean:
        deviate = int((abs(counter_input - mean)/sd *6))
        score += 9 + deviate
    elif counter_input > mean and counter_input <= mean + sd:
        deviate = int((abs(counter_input - mean) / sd * 6))
        score += 9 - deviate
    elif counter_input > mean + sd:
        score += 3
    print(score)

    if score <= 21:
        profile = "aggressive"

    elif score > 21 and score <= 34:
        profile = "Moderate Balance"

    elif score > 35 and score <= 47:
        profile = "Growth Balance"

    elif score > 48:
        profile = "Conservative"

    print(profile)

    return profile

def store_response():
    # store user input into user_response.csv

    with open("user_response.csv", "a") as data:
        writer = csv.writer(data)
        writer.writerows([user_input])
        
risk_profiling()
store_response()
