-- This script was generated by a beta version of the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS metacritic_games.games
(
    game_id integer,
    game_name character varying(100),
    PRIMARY KEY (game_id)
);

CREATE TABLE IF NOT EXISTS metacritic_games.companies
(
    company_id integer,
    company_name character varying(50),
    PRIMARY KEY (company_id)
);

CREATE TABLE IF NOT EXISTS metacritic_games.consoles
(
    console_id integer,
    company_id integer,
    console_name character varying(50),
    PRIMARY KEY (console_id)
);

CREATE TABLE IF NOT EXISTS metacritic_games.scores
(
    game_id integer,
    console_id integer,
    metascore integer,
    userscore numeric(2, 1),
    date date,
    PRIMARY KEY (game_id, console_id)
);

ALTER TABLE IF EXISTS metacritic_games.consoles
    ADD FOREIGN KEY (company_id)
    REFERENCES metacritic_games.companies (company_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS metacritic_games.scores
    ADD FOREIGN KEY (game_id)
    REFERENCES metacritic_games.games (game_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS metacritic_games.scores
    ADD FOREIGN KEY (console_id)
    REFERENCES metacritic_games.consoles (console_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;