import os
image_files=[]
os.chdir(os.path.join("data","obj","obj"))
print("start")
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        print(filename)
        image_files.append("data/obj/obj/"+filename)
os.chdir("..")
os.chdir("..")

with open("train.txt","w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
print("end")
