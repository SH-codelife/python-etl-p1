test_select = ('''
  SELECT *
  FROM petl1.AnnualTicketSales;
''')

insert_row = ('''
    INSERT INTO petl1.AnnualTicketSales
    VALUES(%s, %s, %s, %s, %s);
''')

test_insert = ('''
  INSERT INTO petl1.WideReleasesCount
  VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
''')

#create_schema = ('''
#    create schema IF NOT EXISTS petl1;
#''')

create_table = ('''  
    create table IF NOT EXISTS petl1.AnnualTicketSales (
        YEAR int primary key NOT NULL,
        TICKETS_SOLD text,
        TOTAL_BOX_OFFICE text,
        TOTAL_INFLATION_ADJUSTED_BOX_OFFICE text,
        AVERAGE_TICKET_PRICE text)
''')

create_table = ('''
    create table IF NOT EXISTS petl1.HighestGrossers (
        YEAR INT PRIMARY KEY NOT NULL,
        MOVIE text,
        GENRE text,
        MPAA_RATING text,
        DISTRIBUTOR text,
        TOTAL_FOR_YEAR text,
        TOTAL_IN_2019_DOLLARS text,
        TICKETS_SOLD text)
''')

create_table = ('''
    create table IF NOT EXISTS petl1.PopularCreativeTypes (
        RANK INT PRIMARY KEY NOT NULL,
        CREATIVE_TYPES text,
        MOVIES text,
        TOTAL_GROSS text,
        AVERAGE_GROSS text,
        MARKET_SHARE text)
''')

create_table = ('''
    create table IF NOT EXISTS petl1.TopDistributors (
        RANK INT PRIMARY KEY NOT NULL,
        DISTRIBUTORS text,
        MOVIES text,
        TOTAL_GROSS text,
        AVERAGE_GROSS text,
        MARKET_SHARE text)
''')

create_table = ('''
    create table IF NOT EXISTS petl1.TopGenres (
        RANK INT PRIMARY KEY NOT NULL,
        DISTRIBUTORS text,
        MOVIES text,
        TOTAL_GROSS text,
        AVERAGE_GROSS text,
        MARKET_SHARE text)
''')

create_table = ('''
    create table IF NOT EXISTS petl1.TopGrossingRatings (
        RANK INT PRIMARY KEY NOT NULL,
        MPAA_RATINGS text,
        MOVIES text,
        TOTAL_GROSS text,
        AVERAGE_GROSS text,
        MARKET_SHARE text)
''')

create_table = ('''
    create table IF NOT EXISTS petl1.TopGrossingSources (
        RANK INT PRIMARY KEY NOT NULL,
        SOURCES text,
        MOVIES text,
        TOTAL_GROSS text,
        AVERAGE_GROSS text,
        MARKET_SHARE text)
''')

create_table = ('''
    create table if NOT EXISTS petl1.TopProductionMethods (
        RANK INT PRIMARY KEY NOT NULL,
        PRODUCTION_METHODS text,
        MOVIES text,
        TOTAL_GROSS text,
        AVERAGE_GROSS text,
        MARKET_SHARE text)
''')
create_table = ('''
    create table IF NOT EXISTS petl1.WideReleasesCount (
        YEAR INT PRIMARY KEY NOT NULL,
        WARNER_BROS text,
        WALT_DISNEY text,
        _20TH_CENTURY_FOX text,
        PARAMOUNT_PICTURES text,
        SONY_PICTURES text,
        UNIVERSAL text,
        TOTAL_MAJOR_6 text,
        TOTAL_OTHER_STUDIOS text)
''')