# string analysis 

#KEY TAKEAWAY = NOTHING 

class captionAnalyse:
    def __init__(self, string):
        self.string = string

    def analyseString(self):
        counter = 0
        counterSmall = 0
        reversed = []
        for i in self.string:
            reversed.append(i)
            for j in i:
                counterSmall += 1
            counter += 1
        print("Words:", counter)
        print("Characters:", counterSmall)
        print("Reversed:", "".join(reversed))
        print("Title Case:", self.string.capitalize())

string1 = captionAnalyse("the dark knight rises again")
string1.analyseString()