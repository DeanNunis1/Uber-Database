import mysql.connector
mydb = mysql.connector.connect(host="",
user="",
password="",
auth_plugin='',
database = "RideShare")
print(mydb)
# create cursor obj to interact with mySQL
mycursor = mydb.cursor()


# Rider or Driver
def User(id):
    if id % 2 == 0:
        sql = 'SELECT RiderName FROM Rider WHERE RiderID = %s'
        mycursor.execute(sql, (id, ))
        myresult = mycursor.fetchall()
        myresult = [i[0] for i in myresult]
        for i in myresult:
            print("Welcome", i, ", you are a rider")
    else:
        sql = 'SELECT DriverName FROM Driver WHERE DriverID = %s'
        mycursor.execute(sql, (id, ))
        myresult = mycursor.fetchall()
        myresult = [i[0] for i in myresult]
        for i in myresult:
            print("Welcome", i, ", you are a driver")


######## OPTIONS MENU FOR DRIVER OR RIDER #########
def DriverOptions(id, DriverChoice):
    if DriverChoice == 1:
        sql = "UPDATE Driver SET DriveMode = %s WHERE DriverID = %s"
        mycursor.execute(sql, (1, id, ))
        mydb.commit()
        ridechoice = input("A user has requested a ride, do you want to accept? Yes or No: ")
        if ridechoice == "No":
            print("\nDrive Mode has been turned off \n")
            sql = "UPDATE Driver SET DriveMode = %s WHERE DriverID = %s"
            mycursor.execute(sql, (1, id, ))
            mydb.commit()
            return DriverChoice == 1
        else:
            print("\nRide in progress, make sure to rate your rider after! \n")
            return DriverChoice == 1

    if DriverChoice == 2:
        rating = int(input("Enter a rating between 0 and 5 to give your last rider: "))
        sql = "UPDATE Ride SET RRating = %s WHERE DriverID = %s ORDER BY RideID DESC LIMIT 1"
        mycursor.execute(sql, (rating, id, ))
        mydb.commit()
        sql2 = ("SELECT RiderID FROM Ride WHERE DriverID = %s ORDER BY RideID DESC LIMIT 1")
        mycursor.execute(sql2, (id, ))
        myresult = mycursor.fetchone()
        for x in myresult:
            Riderid = x
        sql3 = ("SELECT RiderRating FROM Rider WHERE RiderID = %s")
        mycursor.execute(sql3, (Riderid, ))
        myresult = mycursor.fetchone()
        for y in myresult:
            RRating = y
        newRating = (rating + RRating)/2
        sql2 = ("UPDATE Rider SET RiderRating = %s Where RiderID = %s")
        mycursor.execute(sql2, (newRating, Riderid,  ))
        mydb.commit()
        print("\nThank you for rating your Rider, you will now be moved to the main menu \n")
    else:
        sql2 = "UPDATE Driver SET DriveMode = 0"
        mycursor.execute(sql2)
        exit()

def RiderOptions(id, RiderChoice):
    if RiderChoice == 1:
        sql = "UPDATE Rider SET RiderStatus = 1 WHERE RiderID = %s"
        mycursor.execute(sql, (id, ))
        mydb.commit()
        Pickup = input("Enter your pickup location: ")
        Dropoff = input("Enter a dropoff location: ")
        mycursor.execute("SELECT DriverID FROM Driver WHERE DriveMode = 1")
        myresult = mycursor.fetchone()
        for x in myresult:
            Driverid = x
        mycursor.execute("SELECT DriverName FROM Driver WHERE DriveMode = 1")
        myresult = mycursor.fetchone()
        for x in myresult:
            print("\nYour drivers name is,", x, ". He will be arriving shortly! \n")
        CreateRide(Driverid, id, Pickup, Dropoff)
        RiderChoice = 1
        return RiderChoice

    if RiderChoice == 2:
        rating = int(input("Enter a rating between 0 and 5 to give your last driver: "))
        sql = "UPDATE Ride SET DRating = %s WHERE RiderID = %s ORDER BY RideID DESC LIMIT 1"
        mycursor.execute(sql, (rating, id, ))
        mydb.commit()
        sql2 = ("SELECT DriverID FROM Ride WHERE RiderID = %s ORDER BY RideID DESC LIMIT 1")
        mycursor.execute(sql2, (id, ))
        myresult = mycursor.fetchone()
        for x in myresult:
            Driverid = x
        sql3 = ("SELECT DriverRating FROM Driver WHERE DriverID = %s")
        mycursor.execute(sql3, (Driverid, ))
        myresult = mycursor.fetchone()
        for y in myresult:
            DRating = y
        newRating = (rating + DRating)/2
        sql2 = ("UPDATE Driver SET DriverRating = %s Where DriverID = %s")
        mycursor.execute(sql2, (newRating, Driverid,  ))
        mydb.commit()
        print("\nThank you for rating your Rider, you will now be moved to the main menu\n")
    else:
        sql = "UPDATE Rider SET RiderStatus = 0"
        mycursor.execute(sql)
        exit()

def CreateRide(Driverid, Riderid, Pickup, Dropoff):
    mycursor.execute("INSERT INTO Ride (DriverID, RiderID, PickUp, DropOff, DRating, RRating) VALUES(%s, %s, %s, %s, %s, %s)",
    (Driverid, Riderid, Pickup, Dropoff, 5, 5))
    mydb.commit()


############# MAIN ##############
id = int(input("Enter your ID: "))
DriverChoice = 0
User(id)
if id % 2 == 0:
    RiderChoice = 1
    while RiderChoice != 3:
        print("Enter 1 to find a driver")
        print("Enter 2 to rate your last driver")
        print("Enter 3 to exit")
        RiderChoice = int(input())
        RiderOptions(id, RiderChoice)
else:
    DriverChoice = 1
    while DriverChoice != 3:
        print("Enter 1 to enable DriveMode")
        print("Enter 2 to rate your last Rider")
        print("Enter 3 to exit")
        DriverChoice = int(input())
        DriverOptions(id, DriverChoice)





# SHOW A TABLE
# mycursor.execute("SELECT * FROM Rider")
# result = mycursor.fetchall()
# for row in result:
#     print(row)
#     print("\n")


# ADD TABLES
#mycursor.execute("CREATE TABLE Driver(DriverID INT, DriverName VARCHAR(50), DriveMode INT, DriverRating DOUBLE, TotalRides INT, PRIMARY KEY(DriverID))")
#mycursor.execute("CREATE TABLE Rider (RiderID INT, RiderName VARCHAR(50), RiderStatus INT, RiderRating DOUBLE, PRIMARY KEY(RiderID))")
#mycursor.execute("CREATE TABLE Ride (RideID INT AUTO_INCREMENT, DriverID INT, RiderID INT, PickUp VARCHAR(100), DropOff VARCHAR(100), DRating DOUBLE, RRating DOUBLE, PRIMARY KEY(RideID))")


# DROP TABLE
#mycursor.execute("DROP TABLE Ride")


# ADDED DATA
#sql = "INSERT INTO Driver (DriverID, DriverName, DriveMode, DriverRating, TotalRides) VALUES (%s, %s, %s, %s, %s)"
#vals = [
  #(1, 'James Smith', 0, 4.3, 102),
  #(3, 'John Kenny', 0, 4.1, 106)
  #]
#sql = "INSERT INTO Rider (RiderID, RiderName, RiderStatus, RiderRating) VALUES (%s, %s, %s, %s)"
#vals = [
  #(2, 'Becca Smith', 0, 3.8),
  #(4, 'Amanda Robins', 0, 4.2)
  #]
# sql = "INSERT INTO Ride (RideID, DriverID, RiderID, PickUp, DropOff, DRating, RRating) VALUES (%s, %s, %s, %s, %s, %s, %s)"
# vals = [
#   (1, 1, 1, "22 west hollywood", "32 Broadway st", 4.2, 3.3),
#   (2, 2, 2, "22 east westwood st", "983 Cliff dr", 3.8, 4.8)
#   ]


# SEND DATA TO TABLES
# mycursor.executemany(sql, vals)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")


# SHOW DATBASES IN MYSQL
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
  #print(x)
mydb.close()
