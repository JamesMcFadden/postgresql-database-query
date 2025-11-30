INSERT INTO agencies (name, country, founded_year) VALUES
 ('NASA', 'USA', 1958),
 ('SpaceX', 'USA', 2002),
 ('ESA', 'Europe', 1975);

INSERT INTO rockets (name, manufacturer, first_flight_year) VALUES
 ('Falcon 9', 'SpaceX', 2010),
 ('Falcon Heavy', 'SpaceX', 2018),
 ('SLS', 'NASA', 2022);

INSERT INTO launch_sites (name, country) VALUES
 ('Kennedy Space Center LC-39A', 'USA'),
 ('Vandenberg SFB', 'USA');

INSERT INTO launches (
    mission_name, launch_date, agency_id, rocket_id, site_id,
    destination, outcome, payload_mass_kg
) VALUES
 ('CRS-21',     '2020-12-06', 2, 1, 1, 'ISS',  'success', 2972),
 ('Starlink-15','2020-10-24', 2, 1, 2, 'LEO',  'success', 15400),
 ('Artemis I',  '2022-11-16', 1, 3, 1, 'Moon', 'success', 27000),
 ('Test Flight 1','2021-03-01', 3, 1, 2, 'LEO','failure', 5000);
