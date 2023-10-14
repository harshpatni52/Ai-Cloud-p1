class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harshApplication = RailwayForm()
harshApplication.name = "Harshit"
harshApplication.train = "Satapdi Express"
harshApplication.printData()         