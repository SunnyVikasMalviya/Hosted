#! python3
# userCRUD.py
# 1. Creates a new user and writes user credentials to a database.
# 2. Authenticates users while login by reading credentials from the data base.

import sqlite3
import hashlib

class userCRUD:
    def __init__(self):
        print("Creating cursor and connection objects...")
        self.conn, self.cursor = self.connectDB()

    def connectDB(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        if cursor.execute("SELECT name from sqlite_master WHERE name='users'").fetchone() == None:
            cursor.execute("CREATE TABLE users(username TEXT, email TEXT, password BLOB)")
            #TODO: This could be improved by using IF NOT EXISTS in CREATE TABLE query
        return conn, cursor

    def createHash(self, text):
        return hashlib.sha256(text.encode('ASCII'), usedforsecurity=True).hexdigest()

    def createUser(self, username, email, password):
        hashword = self.createHash(password)
        self.cursor.execute("INSERT INTO users(username, email, password) VALUES (?, ?, ?);", (username, email, hashword))
        self.conn.commit()
        print("User {} created.".format(username))
        return True

    def loginUser(self, username, password):
        user = self.getUser(username)
        if user:
            if user[0] == username and user[2] == self.createHash(password):
                return True
            else:
                print("Incorrect password for the given user {}".format(username))
        else:
            print("User {} doesn't exist.".format(username))
        return False
    
    def getUser(self, username):
        user = self.cursor.execute("SELECT * FROM users WHERE username = ?", username).fetchone()
        return user
    
    def deleteUser(self, username):
        self.cursor.execute("DELETE FROM users WHERE username = ?", username)
        self.conn.commit()
        print("User {} deleted.".format(username))
        return True

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("Deleting cursor and connection objects...")
        del self.cursor
        del self.conn

if __name__ == "__main__":
    userObj = userCRUD()
    print(userObj.createUser('A', 'Ag.com', 'A'))
    print(userObj.createUser('B', 'Bg.com', 'B'))
    print(userObj.createUser('C', 'Cg.com', 'C'))
    print(userObj.getUser('A'))
    print(userObj.getUser('B'))
    print(userObj.getUser('D'))
    print(userObj.loginUser('A', 'A'))
    print(userObj.loginUser('B', 'B'))
    print(userObj.loginUser('A', 'B'))
    print(userObj.loginUser('D', 'A'))
    print(userObj.deleteUser('C'))
    print(userObj.deleteUser('D'))
    print(userObj.getUser('C'))

    
    
