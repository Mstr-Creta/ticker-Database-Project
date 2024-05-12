import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="sticker_database"
)

cursor = db.cursor()

# Example: Inserting a new user
def insert_user(username, email, password, profile_picture=None):
    sql = "INSERT INTO Users (Username, Email, Password, ProfilePicture) VALUES (%s, %s, %s, %s)"
    val = (username, email, password, profile_picture)
    cursor.execute(sql, val)
    db.commit()
    print("User inserted successfully.")

# Example: Getting all stickers
def get_all_stickers():
    cursor.execute("SELECT * FROM Stickers")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Example: Adding a sticker to a user's collection
def add_sticker_to_user(user_id, sticker_id, status='Pending'):
    sql = "INSERT INTO User_Sticker (UserID, StickerID, Status) VALUES (%s, %s, %s)"
    val = (user_id, sticker_id, status)
    cursor.execute(sql, val)
    db.commit()
    print("Sticker added to user's collection.")

# Example: Getting a user's stickers
def get_user_stickers(user_id):
    sql = "SELECT * FROM User_Sticker WHERE UserID = %s"
    val = (user_id,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Example usage
if __name__ == "__main__":
    # Inserting a new user
    insert_user("john_doe", "john@example.com", "password123")

    # Getting all stickers
    get_all_stickers()

    # Adding a sticker to a user's collection
    add_sticker_to_user(1, 1)

    # Getting a user's stickers
    get_user_stickers(1)

# Close the database connection
db.close()
