class rev:
    def __init__(self,text):
        self.text=text
        self.count=len(text)
    def __iter__(self):
        return self
    def __next__(self):
        if self.count==0:
            raise StopIteration
        else:
            self.count-=1
            return(self.text[self.count])

x=rev("Akash")

for i in x:
    print(i)