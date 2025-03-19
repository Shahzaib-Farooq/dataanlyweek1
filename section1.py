print("Welcome to movie recommendation")
genra=input("What genra do you prefer?(Action,Comedy,Horror,Sci-Fi)")
if genra=="Action":
    prefer=input("Do you prefer a serious or fun movie")
    if prefer=="serious":
        language=input("Do you prefer English or another language movie")
    elif prefer=="fun":
        lang=input("Do you prefer English or another language movie")
        if lang=="English":
            Time="120 min"
            
        else:
            print("hindi movie")
            Time="60 min"
            
    else:
        print("Chinese serious movie")

elif genra=="Comedy":
    prefer=input("Do you prefer a serious or fun movie")
elif genra=="Horror":
    prefer=input("Do you prefer a serious or fun movie")
else:
    print("Sci-Fi")
print ("Duration",Time)
    