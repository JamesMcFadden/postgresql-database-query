CREATE TABLE IF NOT EXISTS agencies (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    country TEXT,
    founded_year INTEGER
);

CREATE TABLE IF NOT EXISTS rockets (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    manufacturer TEXT,
    first_flight_year INTEGER
);

CREATE TABLE IF NOT EXISTS launch_sites (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    country TEXT
);

CREATE TABLE IF NOT EXISTS launches (
    id SERIAL PRIMARY KEY,
    mission_name TEXT NOT NULL,
    launch_date DATE NOT NULL,     -- use DATE instead of TEXT
    agency_id INTEGER NOT NULL REFERENCES agencies(id),
    rocket_id INTEGER NOT NULL REFERENCES rockets(id),
    site_id INTEGER NOT NULL REFERENCES launch_sites(id),
    destination TEXT,
    outcome TEXT NOT NULL,
    payload_mass_kg REAL
);
