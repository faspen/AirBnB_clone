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
create BaseModel
16cd9638-b240-4f0e-9b4a-e035b5dcfb57
