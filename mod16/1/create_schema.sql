CREATE TABLE actors
(
    act_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    act_first_name VARCHAR(50),
    act_last_name  VARCHAR(50),
    act_gender     VARCHAR(1)
);

CREATE TABLE movie
(
    mov_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_title VARCHAR(50)
);

CREATE TABLE director
(
    dir_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    dir_first_name VARCHAR(50),
    dir_last_name  VARCHAR(50)
);

CREATE TABLE movie_cast
(
    act_id INTEGER,
    mov_id INTEGER,
    role   VARCHAR(50),
    FOREIGN KEY (act_id) REFERENCES actors (act_id) ON DELETE CASCADE,
    FOREIGN KEY (mov_id) REFERENCES movie (mov_id) ON DELETE CASCADE
);

CREATE TABLE oscar_awarded
(
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_id   INTEGER,
    FOREIGN KEY (mov_id) REFERENCES movie (mov_id) ON DELETE CASCADE
);

CREATE TABLE movie_direction
(
    dir_id INTEGER,
    mov_id INTEGER,
    FOREIGN KEY (mov_id) REFERENCES movie (mov_id) ON DELETE CASCADE,
    FOREIGN KEY (dir_id) REFERENCES director (dir_id) ON DELETE CASCADE
);