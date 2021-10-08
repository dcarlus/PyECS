# PyECS

Implementation of an ECS [Entity+Component-System] architecture in Python, with jobs (threads). This is more to be considered as a prototype to experiment this kind of architecture.

## Project structure

* `ecs`: core package of the ECS architecture

* `engine`: implementation of Systems for a 2D game with `pygame` and graphics elements

* `game`: main program with initializations of stuff and resources

## Implementation

### Entities

As the ECS architecture describes it, an `Entity` is only made of a unique ID (ie. an integer value). Entities are managed so that deleted IDs are stored to be reused later for new entities. An `EntityFactory` is used to handle the creation, storing and deletion of entities. 
:warning: Yet, do not use the `EntityFactory` directly!

### Components

`Component`s are only data/properties aggregates, with no logic into them. They can be seen as the data model from a certain point of view. As for the entities, a `ComponentFactory` is used to more easily create, store, access and destroy components. 
:warning: However, as for the entities, you do not have to directly use the `ComponentFactory`.

### Systems

`System`s contain the logic of the Components. Systems are splitted into two classes in this prototype:

* `System` is a generic class for all Systems in your applicaton. It creates a `Component`for a given `Entity` (and links them), deletes the `Component`s attached to an `Entity`, give an access to the `Component` attached to a specific `Entity`, etc. It can be seen as a kind of top-layer factory but provides, in addition, an access to another class, the `SystemProcessing`.

* `SystemProcessing` is an abstract class instancied once in each `System`. It is dedicated to the logic of the `Component`s. Thus, for each `Component` type, a `SystemProcessing` has to be implemented as well.

Here, you have to use the `System`s to create your `Component`s. :wink:

### Jobs

`Job`s are used to group `System`s that can run concurrently (ie. at the same time in different threads). It is possible to set one or more `System`s per `Job` but it is highly recommanded to put together `System`s that are working on different data. It is possible to order the execution of different `Job`s in time, so that you can run a `Job` whose `System`s depends on `System`s processed by a previous `Job`. For example, you will want to update all the sprite positions before doing the render of the frame in a 2D video game. Hence, `Job`s can not only be ordered, but you can define separately the amount of threads to use for each `Job` . Moreover, `Job`s execute `System`s in the order you give them in the list. So that, you have a quite full control on their execution.

### World

`World` is the top class of the whole ECS architecture implementation provided here. It is the one you have to use to create or delete entities, systems and jobs. It handles the life of entities if they are marked as to be removed and all their associated components. `World` also provides a `run` method to execute one loop of the `System`s processing and much more for managing inner data.

## Limitations

CPython does not use the power of multithreading here because of the GIL [Global Interpreter Lock] that safely locks every data. Thus, even if a lot of threads are created, the application performances are the same as if it was monothreaded. :unamused:

It is possible to use another Python interpreter than CPython to get rid of this limitation. However, this repository includes `pygame` as a third-party to display cool things on screen and measure performances of ECS in a game-like application. So, the interpreter should preferably support pygame to plenly test this project. At the moment, no working solution other than CPython has been found.

It would be possible to use multiprocessing instead of multithreading but as it is made to be easily ported to another programming language, it would be better to keep generic things. Moreover, multiprocessing implies a manual managing of shared memories and this point is quite long and/or complicated to handle here. :grimacing:


