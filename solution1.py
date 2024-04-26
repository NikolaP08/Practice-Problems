def analyze_text(in1):
    print("String Length: " + str(len(in1)))

    print("Contains Only Alphabetical Characters? - " + str(in1.isalpha()))

    occur = input("Occurrence Of The Character: ")
    while len(occur) >= 2 or len(occur) <= 0:
        print("Invalid Response")
        occur = input("Occurrence Of The Character: ")
    print("This Character Occurs " + str(in1.count(occur)) + " Times.")

    print("Lowercase Version Of Your String: " + in1.lower())

    startindex = input("Provide A Start Index: ")
    while startindex.isalpha() or len(startindex) == 0 or int(startindex) >= len(in1) or int(startindex) < 0:
        print("Invalid Response")
        startindex = input("Provide A Start Index: ")

    stopindex = input("Provide A Stop Index: ")
    while stopindex.isalpha() or len(stopindex) == 0 or int(stopindex) > len(in1) or int(stopindex) < 0 or int(stopindex) <= int(startindex):
        print("Invalid Response")
        stopindex = input("Provide A Stop Index: ")

    print("Result: " + in1[int(startindex):int(stopindex)])

    index = input("Provide A Index For Your String: ")
    while index.isalpha() or int(index) > len(in1) or int(index) < 0:
        print("Invalid Response")
        index = input("Provide A Index For Your String: ")

    print("Result: " + in1[int(index)])

analyze_text(input("Test Input: "))