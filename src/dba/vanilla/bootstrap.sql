.mode csv
.bail on
.echo on

-- drop/create new tables
.open ./data/processed/DATABASE_NAME.sqlite
.read ./src/dba/vanilla/schema.sql

-- import the data
.changes on
.import ./data/raw/DATAFILE_NAME.csv TABLE_NAME

-- index the data
.read ./src/dba/vanilla/indexes.sql


-- remove the repeated headers
DELETE FROM TABLE_NAME WHERE SOME_ID_COL = 'SOME_ID_COL';
