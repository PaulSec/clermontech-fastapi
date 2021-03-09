PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE speakers (
	id INTEGER NOT NULL, 
	first_name VARCHAR(255), 
	last_name VARCHAR(255), 
	created_at DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO speakers VALUES(2,'Paul','Pinault','2021-03-05 10:52:37.198516');
INSERT INTO speakers VALUES(3,'Pascal','Lafourcade','2021-03-05 10:52:50.816609');
INSERT INTO speakers VALUES(4,'Sylvain','Desgrais','2021-03-05 10:54:52.317639');
INSERT INTO speakers VALUES(5,'Paul','Amar','2021-03-05 10:54:58.781147');
CREATE TABLE events (
	id INTEGER NOT NULL, 
	name VARCHAR(255), 
	created_at DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO events VALUES(1,'API Hour 47','2021-03-04 21:38:38.393339');
CREATE TABLE talks (
	id INTEGER NOT NULL, 
	event_id INTEGER, 
	speaker_id INTEGER, 
	name VARCHAR(255), 
	duration INTEGER, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(event_id) REFERENCES events (id), 
	FOREIGN KEY(speaker_id) REFERENCES speakers (id)
);
INSERT INTO talks VALUES(5,1,3,'Mission Cryptographie',1337,'2021-03-05 10:56:18.932462');
INSERT INTO talks VALUES(6,1,2,'Helium',1337,'2021-03-05 10:56:44.718519');
INSERT INTO talks VALUES(7,1,4,'Alpine c''est cool !',1337,'2021-03-05 10:57:02.714595');
INSERT INTO talks VALUES(8,1,5,'Livecoding avec FastAPI',1337,'2021-03-05 10:57:19.858323');
CREATE INDEX ix_speakers_last_name ON speakers (last_name);
CREATE INDEX ix_speakers_first_name ON speakers (first_name);
CREATE INDEX ix_events_name ON events (name);
CREATE INDEX ix_talks_name ON talks (name);
CREATE INDEX ix_talks_duration ON talks (duration);
COMMIT;
