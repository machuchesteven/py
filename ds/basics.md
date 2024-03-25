# Basics

Data structure is a systematic way to organize data in order to use it efficiently. Two terms are foundation of any data structures:-

- `Interface` - represents a set of operations that a data structure supports, only provides a list of operations that are supported, type of parameters supported, and return type of the operations
- `Implementation` - they provide the definition of the algorithms used in the operations of data structures

## Characteristics of DS

- `Corrrectness` - DS implementation should implement its interface correctly
- `Time Complexity` - Running time or execution time must be as small as possible
- `Space Complexity` - Memory usage of a data structure operations must be as little as possible

## Needs for DS

As applications gets more complex and data rich, there are mainly 3 problems applications face nowadays:-

- `Data Search` - Consider an inventory of 1M items, each time an application search for data, it scans 1M items, as data grows, apps get slower
- `Processor Speed` - Processor Speed falls limited as data grows to billions
- `Multiple Requests` - As thousands of users need to access data in the same server concurrently, even a very fast server might fail while searching

## Execution Time Cases

There are three cases in comparison of various data structures execution time in relative manner

- Worst Case - Maximum time the DS operation can take, eg _f(n)_ is the worst case, then the function wont take more than _f(n)_ time
- Average Case - Average time the DS operation can take, eg if an operation takes _f(n)_ time, then m operations will take _mf(n)_ time
- Best Case - This depict the least possible execution time of an operation of a data structure

## Basic Terminologies

- Data - values or set of values
- Data Item - refers to single unit of value
- Group Item - Data Items that are divided into sub-items are called are called Group items
- Elementary Items - Data items that can't be divided
- Attribute and Entity - An entity is an object that contains certain attributes or properties which may be assigned values
- Entity set - Entities of similar attributes form an entity set
- Field - a single elementary unit of information representing an attribute of an entity
- Record - collection of field values of a given entity
- File - a collection of records of the entities in a given entity set

## Basic DS Concepts

Consider the following on data definition:-

- Atomic - definition should define a single concept
- Traceable - definition should be able to mapped to some data elements
- Accurate - definition should be unambiguous
- Clear and Concise - definition should understandable

## Data Object

Represents an object having data

## Data Types

Is a way to classify various type of data example as integer, string, boolean, date etc which determines the values that can be used with various types of data, the type of operations that can be performed on the corresponding type of data
