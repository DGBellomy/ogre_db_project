-- CREATE DATABASE ogre;

--Accounts(id, username)
CREATE TABLE IF NOT EXISTS Accounts (
  id SERIAL PRIMARY KEY,
  username VARCHAR(20) UNIQUE NOT NULL
);
-- INSERT INTO Accounts(username) VALUES ('bob'), ('drew'), ('tommy');

--Characters(id, name, rank, level, xp, accountID)
CREATE TABLE IF NOT EXISTS Characters (
  id SERIAL PRIMARY KEY,
  name VARCHAR(20) UNIQUE NOT NULL,
  rank INT,
  level SMALLINT NOT NULL DEFAULT 1,
  xp INT NOT NULL DEFAULT 0,
  accountID INT NOT NULL REFERENCES Accounts(id)
);
-- INSERT INTO Characters(name, accountID) VALUES ('tiger', 1), ('leon', 2), ('fred2032', 1), ('sigmond1999', 3);

--Duels(timestamp, winnerID, loserID)
CREATE TABLE IF NOT EXISTS Duels (
  timestamp TIMESTAMPTZ DEFAULT NOW() PRIMARY KEY,
  winnerCharacterID INT NOT NULL REFERENCES Characters(id),
  loserCharacterID INT NOT NULL REFERENCES Characters(id),
  CHECK(winnerCharacterID <> loserCharacterID)
);
-- INSERT INTO Duels(winnerCharacterID, loserCharacterID) VALUES (2, 2); -- should fail

--Classes(name, description)
CREATE TABLE IF NOT EXISTS Classes (
  name VARCHAR(20) PRIMARY KEY NOT NULL,
  description VARCHAR(120) NOT NULL,
  CHECK(description <> '' AND name <> '')
);
-- INSERT INTO Classes(name, description) VALUES ('', ''); -- should fail

--Attributes(name, description)
CREATE TABLE IF NOT EXISTS Attributes (
  name VARCHAR(20) PRIMARY KEY NOT NULL,
  description VARCHAR(120) NOT NULL,
  CHECK(description <> '' AND name <> '')
);
-- INSERT INTO Attributes(name, description) VALUES ('', ''); -- should fail

--ClassAttributeWeights(className, attributeName, weight)
CREATE TABLE IF NOT EXISTS ClassAttributeWeights (
  className VARCHAR(20) NOT NULL REFERENCES Classes(name),
  attributeName VARCHAR(20) NOT NULL REFERENCES Attributes(name),
  weight SMALLINT NOT NULL CHECK(weight IN (4, 6, 8, 10)),
  PRIMARY KEY(className, attributeName)
);
-- INSERT INTO ClassAttributeWeights(className, attributeName, weight) VALUES ('Wizard', 'Intelligence', -13);

--CharacterAttributeValues(characterID, attributeName, value)
CREATE TABLE IF NOT EXISTS CharacterAttributeValues (
  characterID INT NOT NULL REFERENCES Characters(id),
  attributeName VARCHAR(20) NOT NULL REFERENCES Attributes(name),
  value SMALLINT NOT NULL CHECK(value > 0),
  PRIMARY KEY(characterID, attributeName)
);
-- INSERT INTO CharacterAttributeValues(characterID, attributeName, value) VALUES (1, 'Intelligence', -13);
