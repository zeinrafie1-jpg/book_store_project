DROP TABLE IF EXISTS films;
DROP SEQUENCE IF EXISTS films_id_seq;

CREATE SEQUENCE IF NOT EXISTS films_id_seq;
CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title text,
    genre text,
    release_year int
);


INSERT INTO films (title, genre, release_year) VALUES ('Film1', 'Horror', 2000);
INSERT INTO films (title, genre, release_year) VALUES ('Grown Ups', 'Comedy', 2010);
INSERT INTO films (title, genre, release_year) VALUES ('The Devil Wears Prada 2', 'Comedy', 2026);

