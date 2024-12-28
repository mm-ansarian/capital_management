"""This module provides all the required methods such as creating a message box and 
calling the database.
"""


import mysql.connector as db_module
import ctypes


# TODO: The program should be able to connect to the database of localhost at all situations.
class Options:
    """A class including all the required methods.
    This class has a module to create a message box.
    There also another module in this class which is used to connect to the database.
    """

    # Default host, username, password and name of the database.
    default_host = 'localhost'
    default_username = 'root'
    default_password = ''
    default_name = 'capital_management'

    # A module to create a message box.
    @classmethod
    def message_box(cls, title: str, text: str, number: int) -> None:
        ctypes.windll.user32.MessageBoxW(0, text, title, number)

    # A module to work with database.
    @classmethod
    def call_database(cls, host_arg: str=default_host, username_arg: str=default_username,
        password_arg: str=default_password, name_arg: str=default_name, command_arg: str=None,
        create_notification: bool=True) -> list | None:
        try:
            temp_database = db_module.connect(
                host=host_arg,
                username=username_arg,
                password=password_arg)
            temp_cursor = temp_database.cursor()

            temp_cursor.execute(f'CREATE DATABASE IF NOT EXISTS {name_arg}')
            temp_database.close()

            main_database = db_module.connect(
                host=host_arg,
                username=username_arg,
                password=password_arg,
                database=name_arg)
            cursor = main_database.cursor()

            if command_arg:
                cursor.execute(command_arg)

            if "SELECT" in command_arg.upper():
                return cursor.fetchall()
            
            elif "INSERT" in command_arg.upper() or "UPDATE" in command_arg.upper() or (
                "DELETE" in command_arg.upper() or "DROP" in command_arg.upper() or (
                "CREATE" in command_arg.upper())):
                main_database.commit()

        except db_module.ProgrammingError:
            if create_notification:
                Options.message_box(
                    "Incorrect Password",
                    "The password of the database was incorrect.",
                    16)
                
        except db_module.DatabaseError:
            if create_notification:
                cls.message_box(
                    "Connection Failed",
                    "The program couldn't connect to the database due to some reasons :(",
                    16)
                
        finally:
                try:
                    cursor.close()
                    main_database.close()

                except:
                    pass
