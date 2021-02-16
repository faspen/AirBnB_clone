# AirBnB_clone

This project is about creating a full web application based off of AirBnB. It is divided into separate projects.

## Description

The AirBnB project is a mega-project divided into seven seperate ones:

**The Console:**

* create your data model

* manage (create, update, destroy, etc) objects via a console / command interpreter

* store and persist objects to a file (JSON file)

**Web Static:**

* learn HTML/CSS

* create the HTML of your application

* create template of each object

**MySQL storage:**

* replace the file storage by a Database storage

* map your models to a table in database by using an O.R.M.

**Web framework - templating:**

* create your first web server in Python

* make your static HTML file dynamic by using objects stored in a file or database

**RESTful API:**

* expose all your objects stored via a JSON web interface

* manipulate your objects via a RESTful API

**Web dynamic:**

* learn JQuery

* load objects from the client side by using your own RESTful API

## How to Use

**Startup**

First, clone this repository with the following command:

```shell
git clone https://github.com/faspen/AirBnB_clone
```

Once the repository is cloned, change directories and execute the file:

```shell
./console
```

When you run this command you should see the prompt:

```shell
(hbnb)
```

Once you see this, you are now ready to use the console.

**Commands**

The purpose of the AirBnB console is to create, manipulate, and destroy different objects. The table below contains the different objects you can interact with.

| Class | Attributes |
| ------ | ------ |
| BaseModel | id, created_at, updated_at |
| User | email, password, first_name, last_name |
| State | name |
| City | state_id, name |
| Amenity | name |
| Place | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| Review | place_id, user_id, text |

The table below shows all available commands and their uses.

| Command | Action |
| ------ | ------ |
| create | create a class instance |
| show | displays information of a given instance |
| destroy | Delete an instance |
| all | display all instances of a class or all instances of all classes |
| update | update attributes of a class |

Here is how you use each of the different commands:

* create - to create an instance, type "create" followed by a class name. This will create an instance of that class and display its id.

```shell
(hbnb) create User
16cd9638-b240-4f0e-9b4a-e035b5dcfb57
```

* show - in order to show an instance, you must type "show" followed by the class name of the instance, followed by the instance's id.

```shell
(hbnb) show User 16cd9638-b240-4f0e-9b4a-e035b5dcfb57
[User] (16cd9638-b240-4f0e-9b4a-e035b5dcfb57) {'id': '16cd9638-b240-4f0e-9b4a-e035b5dcfb57', 'created_at': datetime.datetime(2021, 2, 16, 17, 38, 32, 955297), 'updated_at': datetime.datetime(2021, 2, 16, 17, 38, 32, 955474)}
```

* destroy - to delete an instance, type "delete" followed by the class name of the instance, followed by the instance's id.

```shell
(hbnb) destroy User 16cd9638-b240-4f0e-9b4a-e035b5dcfb57
(hbnb)
(hbnb) show User 16cd9638-b240-4f0e-9b4a-e035b5dcfb57
** no instance found **
```

* all - to display all instances, simply type "all". To display all instances of a specific class, type "all" followed by the class name.

```shell
(hbnb) all
["[User] (6c6976e4-97d4-4f60-99ae-c948fc2cfd15) {'updated_at': datetime.datetime(2021, 2, 16, 17, 48, 13, 24922), 'id': '6c6976e4-97d4-4f60-99ae-c948fc2cfd15', 'created_at': datetime.datetime(2021, 2, 16, 17, 48, 13, 24663)}", "[User] (16cd9638-b240-4f0e-9b4a-e035b5dcfb57) {'updated_at': datetime.datetime(2021, 2, 16, 17, 38, 32, 955474), 'id': '16cd9638-b240-4f0e-9b4a-e035b5dcfb57', 'created_at': datetime.datetime(2021, 2, 16, 17, 38, 32, 955297)}", "[BaseModel] (7e43e47e-e771-4b48-a8a1-83142d7f6788) {'updated_at': datetime.datetime(2021, 2, 12, 2, 17, 0, 296464), 'id': '7e43e47e-e771-4b48-a8a1-83142d7f6788', 'created_at': datetime.datetime(2021, 2, 12, 2, 17, 0, 296419)}"]
(hbnb) all User
["[User] (6c6976e4-97d4-4f60-99ae-c948fc2cfd15) {'updated_at': datetime.datetime(2021, 2, 16, 17, 48, 13, 24922), 'id': '6c6976e4-97d4-4f60-99ae-c948fc2cfd15', 'created_at': datetime.datetime(2021, 2, 16, 17, 48, 13, 24663)}", "[User] (16cd9638-b240-4f0e-9b4a-e035b5dcfb57) {'updated_at': datetime.datetime(2021, 2, 16, 17, 38, 32, 955474), 'id': '16cd9638-b240-4f0e-9b4a-e035b5dcfb57', 'created_at': datetime.datetime(2021, 2, 16, 17, 38, 32, 955297)}"]
```

* update - updating an instance requires you to type "update", followed by the class name and instance id, followed by the attribute you would like to update, followed by the value.

```shell
(hbnb) show User 16cd9638-b240-4f0e-9b4a-e035b5dcfb57
[User] (16cd9638-b240-4f0e-9b4a-e035b5dcfb57) {'created_at': datetime.datetime(2021, 2, 16, 17, 38, 32, 955297), 'id': '16cd9638-b240-4f0e-9b4a-e035b5dcfb57', 'updated_at': datetime.datetime(2021, 2, 16, 17, 38, 32, 955474), 'first_name': 'Finn'}
(hbnb) update User 16cd9638-b240-4f0e-9b4a-e035b5dcfb57 first_name "Betty"
[User] (16cd9638-b240-4f0e-9b4a-e035b5dcfb57) {'created_at': datetime.datetime(2021, 2, 16, 17, 38, 32, 955297), 'id': '16cd9638-b240-4f0e-9b4a-e035b5dcfb57', 'first_name': 'Betty', 'updated_at': datetime.datetime(2021, 2, 16, 17, 38, 32, 955474)}
(hbnb) show User 16cd9638-b240-4f0e-9b4a-e035b5dcfb57
```
