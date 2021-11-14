CREATE DATABASE leaderboard;
USE DATABASE leaderboard;

CREATE TABLE scoreboard(
	id INTEGER;
	name VARCHAR(20);
	score INT not NULL;
	PRIMARY KEY(id);
);