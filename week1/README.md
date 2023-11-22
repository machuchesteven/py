# This week, NOv 17 - 24, 2023

This weeks first challenges is creating a python django project for the pokemonAPI using django and django rest framework

## The Schema used will be given with djangopokes project in this directory

The project will be the alternative to the C# project created with the .NET framework

## Challenge 1 - djandopokes project structure and configuration

Models:-

1. Pokemon
   *. id
   *. name
   *. description
   *. category
   *. birth_date
2. Category
   *. id
   *. name
   *. description : nullable
3. Country
   *. id
   *. name
   *. description : nullable
4. Owner
   *. id
   *. first_name
   *. last_name
   *. country : nullable
5. Review
   *. id
   *. title
   *. content
   *. rating : nullable
6. Reviewer
   *. id
   *. first_name
   *. last_name
   *. email : nullable
   *. user_id : nullable
7. PokemonOwner
   *. pokemon
   *. owner
8. PokemonCategory
   *. pokemon
   *. category

## Challenge 2 - Chatbot with a json Database

The aim of the project is building a conversational chatbot that will be used to gather user inputs and store them into the database that is a json file, and wherever the customer asks the liking of the same question, the chatbot will respond with response to the given answers before.
The json object have to be with the following structure

1. question
2. answer

The user will have to type cancel to cancel or a question to continue, and the first thing the user will be asked is the name,
The structure is as follows
User joins the chat
The chatbot gives greeting to the user
The chatbot starts a loop for waiting input
if input is cancel, then cancel the conversation with remarks
else the conversation will continue, taking the questions from the user, comparing them with the answers we have in the db file, and returning the answer if there is, or asking the user to help us answer the question
