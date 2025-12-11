import mysql.connector


def create_database():
    """
    Create the alx_book_store database in MySQL.
    Handles connection errors and ensures proper resource cleanup.
    """
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='9251246Precious'
        )
        
        # Create a cursor to execute queries
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        # Close cursor
        cursor.close()
        
        # Print success message
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as err:
        # Handle connection errors
        if err.errno == 2003:
            print("Error: Failed to connect to MySQL server. Please ensure MySQL is running.")
        elif err.errno == 1045:
            print("Error: Invalid username or password.")
        else:
            print(f"Error: {err}")
    
    finally:
        # Close the connection
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
