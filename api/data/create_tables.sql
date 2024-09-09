
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
    user_id INT REFERENCES users(id) NOT NULL 
);

CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    data VARCHAR(300)
);


INSERT INTO users (userName) VALUES 
('johndoe'), ('janedoe'), ('juan'), ('bob'), ('charlie'),
('david'), ('edward'), ('frank'), ('george'), ('harry'),
('irene'), ('james'), ('karen'), ('laura'), ('michael'),
('nancy'), ('oliver'), ('paul'), ('quincy'), ('rachel');


INSERT INTO events (action_type, created_at, user_id, information) VALUES
('login', '2024-08-01', 1, 'User logged in from IP 192.168.0.1'),
('logout', '2024-08-01', 2, 'User logged out from IP 192.168.0.2'),
('update', '2024-08-02', 3, 'Updated profile information'),
('login', '2024-08-03', 4, 'User logged in from IP 192.168.0.4'),
('create', '2024-08-04', 5, 'Created a new support case'),
('delete', '2024-08-05', 6, 'Deleted a support case'),
('login', '2024-08-06', 7, 'User logged in from IP 192.168.0.7'),
('logout', '2024-08-07', 8, 'User logged out from IP 192.168.0.8'),
('create', '2024-08-08', 9, 'Created a new event'),
('update', '2024-08-09', 10, 'Updated case description'),
('login', '2024-08-10', 11, 'User logged in from IP 192.168.0.11'),
('logout', '2024-08-11', 12, 'User logged out from IP 192.168.0.12'),
('create', '2024-08-12', 13, 'Created a new support case'),
('delete', '2024-08-13', 14, 'Deleted event data'),
('login', '2024-08-14', 15, 'User logged in from IP 192.168.0.15'),
('logout', '2024-08-15', 16, 'User logged out from IP 192.168.0.16'),
('update', '2024-08-16', 17, 'Updated support case details'),
('create', '2024-08-17', 18, 'Created a new event'),
('delete', '2024-08-18', 19, 'Deleted a support case'),
('login', '2024-08-19', 20, 'User logged in from IP 192.168.0.20');

INSERT INTO support_cases (case_name, description, created_at, user_id) VALUES
('Case 1', 'Issue with logging in to the platform', '2024-07-01', 1),
('Case 2', 'System crash during file upload', '2024-07-02', 2),
('Case 3', 'Unable to reset password', '2024-07-03', 3),
('Case 4', 'Bug in event creation workflow', '2024-07-04', 4),
('Case 5', 'Data not syncing with server', '2024-07-05', 5),
('Case 6', 'Performance issue with dashboard', '2024-07-06', 6),
('Case 7', 'Error while deleting events', '2024-07-07', 7),
('Case 8', 'Missing logs in the system', '2024-07-08', 8),
('Case 9', 'Support case assignment not working', '2024-07-09', 9),
('Case 10', 'Security vulnerability in login', '2024-07-10', 10),
('Case 11', 'Issue with file download', '2024-07-11', 11),
('Case 12', 'Inconsistent UI in mobile view', '2024-07-12', 12),
('Case 13', 'Search functionality not returning results', '2024-07-13', 13),
('Case 14', 'Problem with case history retrieval', '2024-07-14', 14),
('Case 15', 'Unexpected logout after 10 minutes', '2024-07-15', 15),
('Case 16', 'API timeout errors', '2024-07-16', 16),
('Case 17', 'Slow response when opening support cases', '2024-07-17', 17),
('Case 18', 'Missing user data in reports', '2024-07-18', 18),
('Case 19', 'Notifications not working as expected', '2024-07-19', 19),
('Case 20', 'Error while saving case information', '2024-07-20', 20);

INSERT INTO logs (data) VALUES 
('Log entry 1: User johndoe logged in successfully'),
('Log entry 2: System generated an error at 2:30 PM'),
('Log entry 3: Support case 5 was created successfully'),
('Log entry 4: Case description updated by janedoe'),
('Log entry 5: User alice reported an issue with the dashboard'),
('Log entry 6: Event ID 3 created by user 4'),
('Log entry 7: Case 10 deleted by admin'),
('Log entry 8: System outage reported at 10:00 AM'),
('Log entry 9: User john logged out due to inactivity'),
('Log entry 10: New user registered in the system'),
('Log entry 11: Scheduled maintenance completed successfully'),
('Log entry 12: Data synchronization completed for all users'),
('Log entry 13: Error in case 14 details update'),
('Log entry 14: User bob added a new support ticket'),
('Log entry 15: System updated logs for the day'),
('Log entry 16: Log entry review at 5:00 PM'),
('Log entry 17: Admin manually updated the event log'),
('Log entry 18: Data purge scheduled for 2024-09-01'),
('Log entry 19: User frank reset their password'),
('Log entry 20: Error log for server downtime recorded');