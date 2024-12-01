#### Databases

Querying (SELECT)
- filtering condition (WHERE)
- SQL is declarative (HAVING used after made aggregations with GROUP BY)

Pull postgres from docker: run `docker pull postgres`

SQLite browser application - download it (with zip file) and run it
- open database file
- run basic queries: 

`SELECT * 
FROM Artist
;`

`SELECT Name. GenreId, Miliseconds, Miliseconds/1000 AS Seconds
FROM Track
--WHERE Miliseconds > 300000 (comment)
WHERE Miliseconds > 300000
;`

`SELECT Name. GenreId, Miliseconds, Miliseconds/1000 AS Seconds
FROM Track
WHERE Name LIKE 'The%' -- case insensitive
;`

`SELECT Name. GenreId, Miliseconds, Miliseconds/1000 AS Seconds
FROM Track
WHERE LOWER(Name) LIKE '%around%' 
;`

JOINS:

`SELECT *
FROM Album
JOIN Artist ON Album.ArtistId = Artist.ArtistId
;`

`SELECT *
FROM Artist
INNER JOIN Album ON Album.ArtistId = Artist.ArtistId
;`

`SELECT *
FROM Artist
LEFT OUTER JOIN Album ON Album.ArtistId = Artist.ArtistId
;`

LEFT JOIN would set NULL values for the right table if there is no match

`PRAGMA table_info(Album);` - to see the schema of the table

`PRAGMA foreign_keys = ON;` - to enable foreign keys in SQLite

`SELECT ar.Name, al.Title
FROM Artist ar
INNER JOIN Album al ON ar.ArtistId = al.ArtistId
;`

`SELECT ar.Name, al.Title
FROM Artist ar
LEFT OUTER JOIN Album al ON ar.ArtistId = al.ArtistId
;`

`SELECT ar.Name, 
            COUNT(al.AlbumId) AS AlbumCount
FROM Artist ar
LEFT OUTER JOIN Album al ON ar.ArtistId = al.ArtistId
GROUP BY ar.ArtistId
ORDER BY AlbumCount DESC
;`

`SELECT ar.Name, al.Title
FROM Artist ar
JOIN Album al ON ar.ArtistId = al.ArtistId
;`

`SELECT ar.Name, 
            COUNT(al.AlbumId) AS AlbumCount
FROM Artist ar
JOIN Album al ON ar.ArtistId = al.ArtistId
GROUP BY ar.Name
ORDER BY AlbumCount DESC
LIMIT 5 -- top 5
;`

Order of execution: (not the same as the order of writing)
1. FROM
2. JOIN
3. WHERE
4. GROUP BY
5. HAVING
6. SELECT
7. ORDER BY
8. LIMIT

`SELECT Name, Miliseconds/1000 AS Seconds
FROM Track
-- WHERE Miliseconds > 300000 
WHERE Seconds > 300 -- SELECT executes after WHERE so it might not work with alias
;`

`SELECT ar.Name, 
            COUNT(al.AlbumId) AS AlbumCount
FROM Artist ar
JOIN Album al ON ar.ArtistId = al.ArtistId
GROUP BY ar.Name
-- HAVING AlbumCount > 5 might not work for some SQL engines, in SQLite it works
HAVING COUNT(al.AlbumId) > 5
ORDER BY AlbumCount DESC
;`

Double quotes for aliases in SQLite: 
`SELECT ar.Name AS "Artist Name", COUNT(al.AlbumId) AS "Album Count"
FROM Artist ar
JOIN Album al ON ar.ArtistId = al.ArtistId
GROUP BY ar.Name
HAVING COUNT(al.AlbumId) > 5
ORDER BY "Album Count" DESC
;`

Subqueries:

Retrieve the names of all tracks that belong to genres that have more than 50 tracks in the database.

`SELECT Track.Name AS TrackTitle, Genre.Name AS GenreName
FROM Track
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE Track.GenreId IN ( -- IN range of values
    SELECT GenreId
    FROM Track
    GROUP BY GenreId
    HAVING COUNT(TrackId) > 50
);`

CTE (Common Table Expression) - temporary table created at the beginning that can be used in the query

`WITH GenreTrackCounts AS ( -- creates new table GenreTrackCounts
    SELECT Genre.Name AS GenreName
        ,Genre.GenreId
        , COUNT(Track.TrackId) AS TrackCount
    FROM Genre
    JOIN Track ON Genre.GenreId = Track.GenreId
    GROUP BY Genre.GenreId
    HAVING TrackCount > 50
)
SELECT Track.Name, GenreTrackCounts.TrackCount
FROM Track
JOIN GenreTrackCounts ON Track.GenreId = GenreTrackCounts.GenreId
WHERE TrackCount > 100
;`

###### Access with Python 

- open notebook
- import sqlite3
- spin up a local postgres instance
- follow the instructions in the readme for connecting to the postgres database
- then connect with python
- see the tables in the database (terminal):

    `docker exec -it chinook-postgres psql -U postgres -d chinook`

    `\dt` - to see the tables

- compare connection settings from the end of the notebook with the ones in the readme (at the end)
- if the data is huge, faster to first manipulate in the database system and then pull it into python

