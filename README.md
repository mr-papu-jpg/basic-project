# basic-project

## DESCRIPTION:

*Fastapi basic project* in which all types of basic HTTP functions will be put into practice, and the creation of a common API will be put into practice, for now it does not have much, but as I am practicing and learning I am going to add things to this project.

*17/01/2026*: It has been updated and new basic CRUD functions have been added.

## Bookstores and Farmworks:

* FastAPI. 
* Uvicorn.
* HTTPie.

*(For the moment)*

## Commands and specifications for use:

To turn on and execute the API, the following comamdo of the Uvicorn library is used.

```bash
uvicorn main:app --reload
```
* Create:

```bash
http POST :8000/heroes/ id:=1 nombre="Thor" super_poder="Rayo" nivel_fuerza:=90
```

* Filter: 

```bash
http GET :8000/heroes/?poder=Rayo
```

* Delete:

```bash
http DELETE :8000/heroes/1
```

*(The use of Httpie will be specified later, I still haven't learned to use it.)*

## Screenshots showing your use and specifications:

*(there will be when the project is larger and more presentable and complex)*

## UPDATE: 16/01/1026 1:23 am venezuela.

### All made from Termux 
