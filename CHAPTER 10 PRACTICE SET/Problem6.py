from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is booked in Train No. : {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train No. : {slf.trainNo} is running on time") 

    def getFare(slf, fro, to):
        print(f"Ticket fare in Train No. : {slf.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(123454)
t.book("Jaipur","Jodhpur")
t.getStatus()
t.getFare("Jaipur","Jodhpur")





from random import randint

class Train:

    def __init__(daksh, trainNo):
        daksh.trainNo = trainNo

    def book(daksh, fro, to):
        print(f"Ticket is booked in Train No. : {daksh.trainNo} from {fro} to {to}")

    def getStatus(daksh):
        print(f"Train No. : {daksh.trainNo} is running on time") 

    def getFare(daksh, fro, to):
        print(f"Ticket fare in Train No. : {daksh.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(123454)
t.book("Jaipur","Jodhpur")
t.getStatus()
t.getFare("Jaipur","Jodhpur")