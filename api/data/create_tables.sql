CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    userName VARCHAR(50)
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    action_type VARCHAR(20) NOT NULL,
    created_at DATE NOT NULL,
    user_id INTEGER REFERENCES users(id) NOT NULL,
    information VARCHAR(100) NOT NULL
);

CREATE TABLE support_cases (
    id SERIAL PRIMARY KEY,
    case_name VARCHAR(100) NOT NULL,
    description VARCHAR(300) NOT NULL,
    created_at DATE NOT NULL,
    event_id INT REFERENCES events(id) NOT NULL,
    user_id INT REFERENCES users(id) NOT NULL 
);

CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    data VARCHAR(300)
);
