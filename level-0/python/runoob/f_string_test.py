#!/usr/bin/env python3
# Copyright 2025 Wayson
# SPDX-License-Identifier: MIT
# License text: https://opensource.org/licenses/MIT

# f_string
name = "wayson"  # string
print(f"hello {name}")  # hello wayson
print(f"{1 + 2}")  # 3
student = ["wayson", "jack", "lee", "lily"]
#print(f"students' names are : {student}")  # students name are : {'lily', 'lee', 'wayson', 'jack'}
print(f"students' names are : {', '.join(student)}")  # students' names are : lily, lee, jack, wayson
print(f"the student {student[0]} is female.")  # the student wayson is female.
github_repo = {"wayson1994" : "to-embodied-ai"}
print(f"the repo belonging to wayson1994 is {github_repo['wayson1994']}.")  # the repo belonging to wayson1994 is to-embodied-ai.
print(f"{1 + 1 = }")  # 1 + 1 =2 but not 1 + 1 = 2, no space is added after the = — that’s just how the debug format works. 

# This is all I’ve covered on runoob.com; I’ll dive deeper into f-strings elsewhere later.