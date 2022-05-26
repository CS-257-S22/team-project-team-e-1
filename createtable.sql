DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
  showtype char(10),
  title text,
  director varchar(500),
  actors text,
  country varchar(500),
  dateadded date,
  releaseyear smallint,
  rating char(10),
  duration char(20),
  genre text,
  synopsis text,
  platform char(30)
);