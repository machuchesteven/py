# Cinemaxy: The Movies API for use with the CinemChatbot for showcasing

This is the app that clones the booking mechanism of cinemas and renders that to a user using the whatsapp chatbot,
The aim of the project is assist in the process of movie booking to provide easy and interactive means of booking for cinema shows and watching them. It might include links for trailers and other general packages for those movies

## The Database of the Cinema Booking API

The models of the cinema Booking API will include the following :-

1. Movie
   - id
   - title
   - description
   - rating
   - cover
   - release_date
   - Genres
   - duration
2. Genre
   - id
   - name
   - description
3. MovieGenre
   - id
   - movie_id
   - genre_id
4. MovieType
   - id
   - name
   - desc
5. Cinema
   - id
   - name
   - location
   - info
6. ShowDay
   - id
   - movie_id
   - start_time
   - cinema_room

```
add pytest-dkjango for making tests easier
```
