# Production Test: @prompd.io/simple-code-gen@1.0.0/prompts/generate-class.prmd

**Date:** 2025-09-12 21:28:57
**Status:** PASS
**Parameters:** {'class_name': 'User', 'description': 'User management class', 'language': 'python'}

## LLM Response

```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| Here's a well-structured Python class for User management:                                                           |
|                                                                                                                      |
| ```python                                                                                                            |
| class User:                                                                                                          |
|     """                                                                                                              |
|     A class representing a user in a user management system.                                                         |
|                                                                                                                      |
|     Attributes:                                                                                                      |
|         _user_id (int): The unique identifier for the user.                                                          |
|         _username (str): The username of the user.                                                                   |
|         _email (str): The email address of the user.                                                                 |
|         _password (str): The password of the user.                                                                   |
|         _active (bool): Indicates whether the user is active or not.                                                 |
|     """                                                                                                              |
|                                                                                                                      |
|     def __init__(self, user_id, username, email, password):                                                          |
|         """                                                                                                          |
|         Initializes a new instance of the User class.                                                                |
|                                                                                                                      |
|         Args:                                                                                                        |
|             user_id (int): The unique identifier for the user.                                                       |
|             username (str): The username of the user.                                                                |
|             email (str): The email address of the user.                                                              |
|             password (str): The password of the user.                                                                |
|                                                                                                                      |
|         Raises:                                                                                                      |
|             ValueError: If any of the input parameters are invalid.                                                  |
|         """                                                                                                          |
|         if not isinstance(user_id, int) or user_id <= 0:                                                             |
|             raise ValueError("Invalid user ID.")                                                                     |
|         if not isinstance(username, str) or not username.strip():                                                    |
|             raise ValueError("Invalid username.")                                                                    |
|         if not isinstance(email, str) or not self._is_valid_email(email):                                            |
|             raise ValueError("Invalid email address.")                                                               |
|         if not isinstance(password, str) or not password.strip():                                                    |
|             raise ValueError("Invalid password.")                                                                    |
|                                                                                                                      |
|         self._user_id = user_id                                                                                      |
|         self._username = username                                                                                    |
|         self._email = email                                                                                          |
|         self._password = password                                                                                    |
|         self._active = True                                                                                          |
|                                                                                                                      |
|     @property                                                                                                        |
|     def user_id(self):                                                                                               |
|         """                                                                                                          |
|         Gets the unique identifier for the user.                                                                     |
|                                                                                                                      |
|         Returns:                                                                                                     |
|             int: The user's ID.                                                                                      |
|         """                                                                                                          |
|         return self._user_id                                                                                         |
|                                                                                                                      |
|     @property                                                                                                        |
|     def username(self):                                                                                              |
|         """                                                                                                          |
|         Gets the username of the user.                                                                               |
|                                                                                                                      |
|         Returns:                                                                                                     |
|             str: The user's username.                                                                                |
|         """                                                                                                          |
|         return self._username                                                                                        |
|                                                                                                                      |
|     @property                                                                                                        |
|     def email(self):                                                                                                 |
|         """                                                                                                          |
|         Gets the email address of the user.                                                                          |
|                                                                                                                      |
|         Returns:                                                                                                     |
|             str: The user's email address.                                                                           |
|         """                                                                                                          |
|         return self._email                                                                                           |
|                                                                                                                      |
|     @property                                                                                                        |
|     def active(self):                                                                                                |
|         """                                                                                                          |
|         Gets a value indicating whether the user is active or not.                                                   |
|                                                                                                                      |
|         Returns:                                                                                                     |
|             bool: True if the user is active, False otherwise.                                                       |
|         """                                                                                                          |
|         return self._active                                                                                          |
|                                                                                                                      |
|     def activate(self):                                                                                              |
|         """                                                                                                          |
|         Activates the user.                                                                                          |
|         """                                                                                                          |
|         self._active = True                                                                                          |
|                                                                                                                      |
|     def deactivate(self):                                                                                            |
|         """                                                                                                          |
|         Deactivates the user.                                                                                        |
|         """                                                                                                          |
|         self._active = False                                                                                         |
|                                                                                                                      |
|     def change_password(self, new_password):                                                                         |
|         """                                                                                                          |
|         Changes the user's password.                                                                                 |
|                                                                                                                      |
|         Args:                                                                                                        |
|             new_password (str): The new password for the user.                                                       |
|                                                                                                                      |
|         Raises:                                                                                                      |
|             ValueError: If the new password is invalid.                                                              |
|         """                                                                                                          |
|         if not isinstance(new_password, str) or not new_password.strip():                                            |
|             raise ValueError("Invalid password.")                                                                    |
|         self._password = new_password                                                                                |
|                                                                                                                      |
|     def _is_valid_email(self, email):                                                                                |
|         """                                                                                                          |
|         Checks if the given email address is valid.                                                                  |
|                                                                                                                      |
|         Args:                                                                                                        |
|             email (str): The email address to validate.                                                              |
|                                                                                                                      |
|         Returns:                                                                                                     |
|             bool: True if the email address is valid, False otherwise.                                               |
|         """                                                                                                          |
|         # Implement email validation logic here                                                                      |
|         return "@" in email and "." in email                                                                         |
| ```                                                                                                                  |
|                                                                                                                      |
| This class includes the following features:                                                                          |
|                                                                                                                      |
| 1. **Constructor**: The `__init__` method validates the input parameters and initializes the user's properties.      |
| 2. **Encapsulation**: The user's properties are marked as private (`_user_id`, `_username`, `_email`, `_password`,   |
| `_active`) and can only be accessed through the provided getter and setter methods.                                  |
| 3. **Documentation**: The class and method documentation provide comprehensive information about the purpose,        |
| parameters, and behavior of the class and its methods.                                                               |
| 4. **Error Handling**: The constructor and `change_password` method include input validation and raise `ValueError`  |
| exceptions for invalid input.                                                                                        |
| 5. **Best Practices**: The class follows Python's object-oriented design principles, such as using properties for    |
| accessing private attributes and providing methods for performing specific actions on the user object.               |
|                                                                                                                      |
| You can use this class to manage users in your application, such as creating new users, activating an                |
+----------------------------------------------------------------------------------------------------------------------+

```
