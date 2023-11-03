<img  height="50px" align="right" src="https://apply.holbertonschool.com/holberton-logo.png">

# Holberton - AirBnB Clone

<p align="center">
    <img src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" alt="Holberton AirBnb Clone logo">
</p>

## 📝 <span id="description">Description</span>

This repository serves as the foundational component for a comprehensive project aimed at creating an **Airbnb clone**.
<br>
It marks the initial phase of this student undertaking, introducing a powerful backend interface, often referred to as a console.
<br>
The console empowers users with the ability to effortlessly manage various program data, including object creation, updates, deletions, and efficient file storage management.
<br>
By leveraging **JSON** serialization and deserialization, data persistence is seamlessly maintained across multiple sessions, setting the stage for subsequent projects like HTML/CSS templating, database integration, API development, and front-end integration.

## 🔨 <span id="tech-stack">Tech stack</span>

<p align="left">
    <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white&style=for-the-badge" alt="VIM badge">
    <img src="https://img.shields.io/badge/JSON-000000?logo=json&logoColor=white&style=for-the-badge" alt="VIM badge">
    <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" alt="Shell badge">
    <img src="https://img.shields.io/badge/UBUNTU-e95420?logo=ubuntu&logoColor=white&style=for-the-badge" alt="Ubuntu badge">
    <img src="https://img.shields.io/badge/VISUAL STUDIO CODE-007ACC?logo=visualstudiocode&logoColor=white&style=for-the-badge" alt="VIM badge">
<p>

## 📋 <span id="requirements">Requirements</span>
 
- All the files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (version 3.8.5).
- The first line of all the files should be exactly `#!/usr/bin/python3`.
- The code should use the `pycodestyle` (version 2.7.*).
- All the files must be executable.
- All the functions, classes and modules should have a documentation .
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose...
- You have to use the `unittest` module.
- All your `unittest` files should be inside a folder tests.
- All your test files should be python files (extension: `.py`).
- All your test files and folders should start by `test_`.
- Your file organization in the tests folder should be the same as your project.
- All your tests should be executed by using this command: `python3 -m unittest discover tests`

## 🎓 <span id="instructions">Instructions</span>

<details>
	<summary>
		<b>Task 0. README, AUTHORS</b>
	</summary>
	<br>

- Write a `README.md`:
    - Description of the project.
    - description of the command interpreter:
        - How to start it.
        - How to use it.
        - Examples.
- You should have an `AUTHORS` file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference <a href="https://github.com/moby/moby/blob/master/AUTHORS">Docker’s AUTHORS page</a>.
- You should use branches and pull requests on GitHub - it will help you as team to organize your work.
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `README.md`, `AUTHORS`.
<hr>
</details>

<details>
	<summary>
		<b>Task 1. Be pycodestyle compliant!</b>
	</summary>
	<br>

Write beautiful code that passes the pycodestyle checks.
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `console.py`, `models/base_model.py`, `models/user.py`, `models/place.py`, `models/state.py`, `models/city.py`, `models/amenity.py`, `models/review.py`, `models/engine/file_storage.py`.
<hr>
</details>

<details>
	<summary>
		<b>Task 2. Unittests</b>
	</summary>
	<br>
All your files, classes, functions must be tested with unit tests

```
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```

*Note that this is just an example, the number of tests you create can be different from the above example.*

**Warning**:

Unit tests must also pass in non-interactive mode:

```
guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `tests/`.
<hr>
</details>

<details>
	<summary>
		<b>Task 3. BaseModel</b>
	</summary>
	<br>

Write a class `BaseModel` that defines all common attributes/methods for other classes:

- `models/base_model.py`.
- Public instance attributes:
    - `id`: string - assign with an `uuid` when an instance is created:
        - You can use `uuid.uuid4()` to generate unique `id` but don’t forget to convert to a string.
        - The goal is to have unique `id` for each `BaseModel`.
    - `created_at`: datetime - assign with the current datetime when an instance is created.
    - `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object.
- `__str__`: should print: `[<class name>] (<self.id>) <self.__dict__>`.
- Public instance methods:
    - `save(self)`: updates the public instance attribute `updated_at` with the current datetime.
    - `to_dict(self)`: returns a dictionary containing all keys/values of `__dict__` of the instance:
        - By using `self.__dict__`, only instance attributes set will be returned.
        - a key `__class__` must be added to this dictionary with the class name of the object.
        - `created_at` and `updated_at` must be converted to string object in ISO format:
            - format: `%Y-%m-%dT%H:%M:%S.%f` (ex: `2017-06-14T22:31:03.285259`).
            - you can use `isoformat()` of `datetime` object.
        - This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our `BaseModel`.

```
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - My First Model
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$ 
```
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `models/base_model.py`, `models/__init__.py`, `tests/`.
<hr>
</details>

<details>
	<summary>
		<b>Task 4. Create BaseModel from dictionary</b>
	</summary>
	<br>

Previously we created a method to generate a dictionary representation of an instance (method `to_dict()`).

Now it’s time to re-create an instance with this dictionary representation.

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```

Update `models/base_model.py`:

- `__init__(self, *args, **kwargs)`:
    - You will use `*args`, `**kwargs` arguments for the constructor of a `BaseModel`. (more information inside the **AirBnB clone** concept page).
    - `*args` won’t be used.
    - If kwargs is not empty:
        - Each key of this dictionary is an attribute name (**Note** `__class__` from `kwargs` is the only one that should not be added as an attribute. See the example output, below).
        - Each value of this dictionary is the value of this attribute name.
    - **Warning**: `created_at` and `updated_at` are strings in this dictionary, but inside your `BaseModel` instance is working with `datetime` object. You have to convert these strings into `datetime` object. Tip: you know the string format of these datetime.
    - Otherwise:
        - Create `id` and `created_at` as you did previously (new instance).

```
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
False
guillaume@ubuntu:~/AirBnB$ 
```
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `models/base_model.py`, `tests/`.
<hr>
</details>

<details>
	<summary>
		<b>Task 5. Store first object</b>
	</summary>
	<br>

Now we can recreate a `BaseModel` from another one by using a dictionary representation:

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```

It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

- Python doesn’t know how to convert a string to a dictionary (easily).
- It’s not human readable.
- Using this file with another program in Python or other language will be hard.

So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```

Magic right?

Terms:

- **Simple Python data structure**: Dictionaries, arrays, number and string. ex: `{ '12': { 'numbers': [1, 2, 3], 'name': "John" } }`.
- **JSON string representation**: String representing a simple data structure in JSON format. ex: `'{ "12": { "numbers": [1, 2, 3], "name": "John" } }'`.

Write a class `FileStorage` that serializes instances to a JSON file and deserializes JSON file to instances:

- `models/engine/file_storage.py`.
- Private class attributes:
    - `__file_path`: string - path to the JSON file (ex: `file.json`)
    - `__objects`: dictionary - empty but will store all objects by `<class name>.id` (ex: to store a `BaseModel` object with `id=12121212`, the key will be `BaseModel.12121212`).
- Public instance methods:
    - `all(self)`: returns the dictionary `__objects`.
    - `new(self, obj)`: sets in `__objects` the obj with key `<obj class name>.id`.
    - `save(self)`: serializes `__objects` to the JSON file (path: `__file_path`).
    - `reload(self)`: deserializes the JSON file to `__objects` (only if the JSON file (`__file_path`) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised).

Update `models/__init__.py`: to create a unique `FileStorage` instance for your application.

- Import `file_storage.py`.
- Create the variable `storage`, an instance of `FileStorage`.
- Call `reload()` method on this variable.

Update `models/base_model.py`: to link your `BaseModel` to `FileStorage` by using the variable `storage`.

- Import the variable `storage`.
- In the method `save(self)`:
    - Call `save(self)` method of `storage`.
- `__init__(self, *args, **kwargs)`:
    - If it’s a new instance (not from a dictionary representation), add a call to the method `new(self)` on `storage`.

```
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$ 
```
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `models/engine/file_storage.py`, `models/engine/__init__.py`, `models/__init__.py`, `models/base_model.py`, `tests/`
<hr>
</details>

<details>
	<summary>
		<b>Task 6. Console 0.0.1</b>
	</summary>
	<br>

Write a program called `console.py` that contains the entry point of the command interpreter:

- You must use the module `cmd`.
- Your class definition must be: `class HBNBCommand(cmd.Cmd):`
- Your command interpreter should implement:
    - `quit` and `EOF` to exit the program.
    - `help` (this action is provided by default by `cmd` but you should keep it updated and documented as you work through tasks).
    - a custom prompt: `(hbnb)`.
    - an empty line + `ENTER` shouldn’t execute anything.
- Your code should not be executed when imported.

**Warning**:

You should end your file with:

```
if __name__ == '__main__':
    HBNBCommand().cmdloop()
```

To make your program executable except when imported. Please don’t add anything around - the Checker won’t like it otherwise.

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
```
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `console.py`.
<hr>
</details>

<details>
	<summary>
		<b>Task 7. Console 0.1</b>
	</summary>
	<br>

Update your command interpreter (`console.py`) to have these commands:

- `create`: creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`.
    - If the class name is missing, print `** class name missing **` (ex: `$ create`)
    - If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ create MyModel`).
- `show`: Prints the string representation of an instance based on the class name and `id`. ex: `$ show BaseModel 1234-1234-1234`.
    - If the class name is missing, print `** class name missing **` (ex: `$ show`).
    - If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ show MyModel`).
    - If the `id` is missing, print `** instance id missing **` (ex: `$ show BaseModel`).
    - If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ show BaseModel 121212`).
- `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file). ex: `$ destroy BaseModel 1234-1234-1234`.
    - If the class name is missing, print `** class name missing **` (ex: `$ destroy`).
    - If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ destroy MyModel`).
    - If the `id` is missing, print `** instance id missing **` (ex: `$ destroy BaseModel`).
    - If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ destroy BaseModel 121212`).
- `all`: prints all string representation of all instances based or not on the class name. ex: `$ all BaseModel` or `$ all`.
    - The printed result must be a list of strings (like the example below).
    - If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ all MyModel`).
- `update`: updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
    - Usage: `update <class name> <id> <attribute name> "<attribute value>"`.
    - Only one attribute can be updated at the time.
    - You can assume the attribute name is valid (exists for this model).
    - The attribute value must be casted to the attribute type.
    - If the class name is missing, print `** class name missing **` (ex: `$ update`).
    - If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ update MyModel`).
    - If the `id` is missing, print `** instance id missing **` (ex: `$ update BaseModel`).
    - If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ update BaseModel 121212`).
    - If the attribute name is missing, print `** attribute name missing **` (ex: `$ update BaseModel existing-id`).
    - If the value for the attribute name doesn’t exist, print `** value missing **` (ex: `$ update BaseModel existing-id first_name`).
    - All other arguments should not be used (ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"` = `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`).
    - `id`, `created_at` and `updated_at` cant’ be updated. You can assume they won’t be passed in the `update` command.
    - Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime.

Let’s add some rules:

- You can assume arguments are always in the right order.
- Each arguments are separated by a space.
- A string argument with a space must be between double quote.
- The error management starts from the first argument to the last one.

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
```
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `console.py`.
<hr>
</details>

<details>
	<summary>
		<b>Task 8. First User</b>
	</summary>
	<br>

Write a class User that inherits from `BaseModel`:

- `models/user.py`.
- Public class attributes:
    - `email`: string - empty string
    - `password`: string - empty string
    - `first_name`: string - empty string
    - `last_name`: string - empty string

Update `FileStorage` to manage correctly serialization and deserialization of `User`.

Update your command interpreter (`console.py`) to allow `show`, `create`, `destroy`, `update` and `all` used with `User`.

```
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_user.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
-- Create a new User --
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@mail.com', 'first_name': 'Betty', 'last_name': 'Bar', 'password': 'root'}
-- Create a new User 2 --
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'email': 'airbnb2@mail.com', 'first_name': 'John', 'password': 'root'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at": "2017-09-28T21:11:42.848279", "updated_at": "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", "first_name": "Betty", "__class__": "User", "last_name": "Bar", "password": "root"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"id": "d0ef8146-4664-4de5-8e89-096d667b728e", "created_at": "2017-09-28T21:11:42.848280", "updated_at": "2017-09-28T21:11:42.848294", "email": "airbnb_2@mail.com", "first_name": "John", "__class__": "User", "password": "root"}}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), 'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), 'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), 'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), 'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287)}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), 'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337)}
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'last_name': 'Bar', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name': 'Betty'}
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'first_name': 'John'}
-- Create a new User --
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'last_name': 'Bar', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'first_name': 'Betty'}
-- Create a new User 2 --
[User] (fce12f8a-fdb6-439a-afe8-2881754de71c) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611354), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611368), 'id': 'fce12f8a-fdb6-439a-afe8-2881754de71c', 'first_name': 'John'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848279", "email": "airbnb@mail.com", "id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "last_name": "Bar", "updated_at": "2017-09-28T21:11:42.848291", "first_name": "Betty", "__class__": "User"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848280", "email": "airbnb_2@mail.com", "id": "d0ef8146-4664-4de5-8e89-096d667b728e", "updated_at": "2017-09-28T21:11:42.848294", "first_name": "John", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852"}, "User.246c227a-d5c1-403d-9bc7-6a47bb9f0f68": {"password": "root", "created_at": "2017-09-28T21:12:19.611352", "email": "airbnb@mail.com", "id": "246c227a-d5c1-403d-9bc7-6a47bb9f0f68", "last_name": "Bar", "updated_at": "2017-09-28T21:12:19.611363", "first_name": "Betty", "__class__": "User"}, "User.fce12f8a-fdb6-439a-afe8-2881754de71c": {"password": "root", "created_at": "2017-09-28T21:12:19.611354", "email": "airbnb_2@mail.com", "id": "fce12f8a-fdb6-439a-afe8-2881754de71c", "updated_at": "2017-09-28T21:12:19.611368", "first_name": "John", "__class__": "User"}}
guillaume@ubuntu:~/AirBnB$ 
```
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `models/user.py`, `models/engine/file_storage.py`, `console.py`, `tests/`.
<hr>
</details>

<details>
	<summary>
		<b>Task 9. More classes!</b>
	</summary>
	<br>

Write all those classes that inherit from `BaseModel`:

- `State` (`models/state.py`):
        - Public class attributes:
            - `name`: string - empty string.
- `City` (`models/city.py`):
    - Public class attributes:
        - `state_id`: string - empty string: it will be the `State.id`
        - `name`: string - empty string.
- `Amenity` (`models/amenity.py`):
    - Public class attributes:
        - `name`: string - empty string.
- `Place` (`models/place.py`):
    - Public class attributes:
        - `city_id`: string - empty string: it will be the `City.id`.
        - `user_id`: string - empty string: it will be the `User.id`.
        - `name`: string - empty string.
        - `description`: string - empty string.
        - `number_rooms`: integer - 0.
        - `number_bathrooms`: integer - 0.
        - `max_guest`: integer - 0.
        - `price_by_night`: integer - 0.
        - `latitude`: float - 0.0.
        - `longitude`: float - 0.0.
        - `amenity_ids`: list of string - empty list: it will be the list of `Amenity.id` later.
- `Review` (`models/review.py`):
    - Public class attributes:
        - `place_id`: string - empty string: it will be the `Place.id`.
        - `user_id`: string - empty string: it will be the `User.id`.
        - `text`: string - empty string.
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `models/state.py`, `models/city.py`, `models/amenity.py`, `models/place.py`, `models/review.py`, `tests/`.
<hr>
</details>

<details>
	<summary>
		<b>Task 10. Console 1.0</b>
	</summary>
	<br>

Update `FileStorage` to manage correctly serialization and deserialization of all our new classes: `Place`, `State`, `City`, `Amenity` and `Review`.

Update your command interpreter (`console.py`) to allow those actions: `show`, `create`, `destroy`, `update` and `all` with all classes created previously.

Enjoy your first console!

**No unittests needed for the console.**
#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone`.
- File: `console.py`, `models/engine/file_storage.py`, `tests/`.
<hr>
</details>


## 📂 <span id="files-description">Files description</span>

### Files

| FILE | DESCRIPTION |
| :-: | - |
| tests | Unittests files folder. |
| AUTHORS | A list of all individuals having contributed content to the repository. |
| README.md | The readme file you are currently reading 😉. |
| console.py | The console module. |

### Models folder

| FILE | DESCRIPTION |
| :-: | - |
| engine -> file_storage.py | Module that defines the FileStorage class, which handles the storage and retrieval of model objects in files. |
| __init__.py | An initialization file for the "models" package. |
| amenity.py | Module that defines the Amenity class, which represents an amenity or feature in our system. |
| base_model.py | Module that defines the BaseModel class, which serves as a base class for other model classes and manages ID, creation, and update dates. |
| city.py | Module that defines the City class, which represents a city in our system. |
| place.py | Module that defines the Place class, which represents a place or accommodation in our system. |
| review.py | Module that defines the Review class, which represents a review or feedback on a place or experience. |
| state.py | Module that defines the State class, which represents a geographic state or region in our system. |
| user.py | Module that defines the User class, which represents a user in our system. |

### Tests folder

| FILE | DESCRIPTION |
| :-: | - |
| __init__.py | An initialization file for the "tests" package. |
| test_amenity.py | Unit tests for Amenity class.|
| test_base_model.py | Unit tests for BaseModel class. |
| test_city.py | Unit tests for City class. |
| test_place.py | Unit tests for Place class. |
| test_review.py | Unit tests for Review class. |
| test_state.py | Unit tests for State class. |
| test_user.pi | Unit tests for User class. |

## Installation

- Clone this repository:
```
git clone https://github.com/fchavonet/holbertonschool-AirBnB_clone.git
```
- To ensure that `console.py` file is executable, run:
```
chmod +x console.py
```
- Run hbnb (interactively):
```
./console.py
```
- Run hbnb (non-interactively):
```
echo "<command>" | ./console.py
```

## 💾 Available Commands

| **COMMAND** | **DESCRIPTION** |
| :-: | - |
| `help` | Prints information about specific command. |
| `create` | Creates a new instance of given class. |
| `show` | Prints the string representation of an instance based on the class name and `id`. |
| `destroy` | Deletes an instance based on the class name and `id` (save the change into the JSON file). |
| `all`	| Prints all string representation of all instances based or not on the class name. |
| `update` | Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). |
| `quit/ EOF` |	Exit the program. |

## 💻 Example

### Launch the console

```
$ ./console.py
(hbnb) 
```

### Help command usage

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create

        Creates a new instance from the given class string (arg),
        saves it (to the JSON file) and prints its id.

        Ex: $ create BaseModel

(hbnb)
```

### Error messages example

```
(hbnb) ls
*** Unknown syntax: ls

(hbnb) create
** class name missing **

(hbnb) all MyModel
** class doesn't exist **
```

### Usage

```
(hbnb) create BaseModel
a7137f85-15d9-46b3-aaae-dfabb8c39797
(hbnb) all BaseModel
["[BaseModel] (a7137f85-15d9-46b3-aaae-dfabb8c39797) {'id': 'a7137f85-15d9-46b3-aaae-dfabb8c39797', 'created_at': datetime.datetime(2023, 11, 3, 16, 59, 17, 455473), 'updated_at': datetime.datetime(2023, 11, 3, 16, 59, 17, 455490)}"]

(hbnb) update BaseModel a7137f85-15d9-46b3-aaae-dfabb8c39797 first_name "Batman"
(hbnb) show BaseModel a7137f85-15d9-46b3-aaae-dfabb8c39797
[BaseModel] (a7137f85-15d9-46b3-aaae-dfabb8c39797) {'id': 'a7137f85-15d9-46b3-aaae-dfabb8c39797', 'created_at': datetime.datetime(2023, 11, 3, 16, 59, 17, 455473), 'updated_at': datetime.datetime(2023, 11, 3, 16, 59, 17, 455490), 'first_name': 'Batman'}

(hbnb) create BaseModel
f408def6-3ffa-4a7e-83a0-31b18a35e906
(hbnb) all BaseModel
["[BaseModel] (a7137f85-15d9-46b3-aaae-dfabb8c39797) {'id': 'a7137f85-15d9-46b3-aaae-dfabb8c39797', 'created_at': datetime.datetime(2023, 11, 3, 16, 59, 17, 455473), 'updated_at': datetime.datetime(2023, 11, 3, 16, 59, 17, 455490), 'first_name': 'Batman'}", "[BaseModel] (f408def6-3ffa-4a7e-83a0-31b18a35e906) {'id': 'f408def6-3ffa-4a7e-83a0-31b18a35e906', 'created_at': datetime.datetime(2023, 11, 3, 17, 0, 34, 57632), 'updated_at': datetime.datetime(2023, 11, 3, 17, 0, 34, 57638)}"]

(hbnb) destroy BaseModel a7137f85-15d9-46b3-aaae-dfabb8c39797
(hbnb) destroy BaseModel f408def6-3ffa-4a7e-83a0-31b18a35e906
(hbnb) all BaseModel
[]

(hbnb) 
```

## ♥️ <span id="thanks">Thanks</span>

A big thank you to all our Holberton School peers for their help and support throughout this project.
<br>

## 👷 <span id="authors">Authors</span>
**Fabien CHAVONET**
- Github: [@fchavonet](https://github.com/fchavonet)

**Pierre-Émmanuel SAINT-MÉZARD**
- Github: [@Eonvorax](https://github.com/Eonvorax)
