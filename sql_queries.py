"""
Description: This file will be used as a module to import creation, insertion and selection queries in the following
scripts:
1. create_tables.py
2. etl.py
"""

# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
k = 0
songplay_table_create = ("""
                            CREATE TABLE IF NOT EXISTS songplays
                             (
                                  songplay_id SERIAL PRIMARY KEY, 
                                  start_time time NOT NULL REFERENCES TIME (START_TIME), 
                                  user_id INT REFERENCES USERS (USER_ID), 
                                  level varchar, 
                                  song_id varchar, 
                                  artist_id VARCHAR REFERENCES ARTISTS (ARTIST_ID), 
                                  session_id  int, 
                                  location varchar, 
                                  user_agent varchar
                              );
                             
                         """)


user_table_create = ("""
                        CREATE TABLE IF NOT EXISTS users
                        (
                            user_id INT PRIMARY KEY, 
                            first_name varchar, 
                            last_name varchar, 
                            gender varchar, 
                            level varchar
                        );
                    
                    """)


song_table_create = ("""
                        CREATE TABLE IF NOT EXISTS songs
                        (
                            song_id VARCHAR PRIMARY KEY, 
                            title varchar, 
                            artist_id VARCHAR REFERENCES ARTISTS (ARTIST_ID), 
                            year int, 
                            duration float
                        )
                    
                     """)


artist_table_create = ("""
                         CREATE TABLE IF NOT EXISTS artists
                         (
                             artist_id VARCHAR PRIMARY KEY, 
                             name varchar, 
                             location varchar, 
                             latitude float, 
                             longitude float
                         )
                       
                       """)


time_table_create = ("""
                        CREATE TABLE IF NOT EXISTS time
                        (
                            start_time time PRIMARY KEY, 
                            hour int, 
                            day int, 
                            week int, 
                            month int, 
                            year int, 
                            weekday int
                        )
                     
                     """)

# # INSERT RECORDS

songplay_table_insert = ("""
                            INSERT INTO songplays 
                            (
                                start_time, 
                                user_id, 
                                level, 
                                song_id, 
                                artist_id, 
                                session_id, 
                                location, 
                                user_agent
                            ) 
                            
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                         
                         """)

user_table_insert = ("""
                        INSERT INTO users 
                        (
                            user_id, 
                            first_name, 
                            last_name, 
                            gender, 
                            level
                        )
                        
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (user_id)
                        DO UPDATE
                                 SET level = EXCLUDED.level, user_id = EXCLUDED.user_id;
                     """)

song_table_insert = ("""
                        INSERT INTO songs 
                        (
                            song_id, 
                            title, 
                            artist_id, 
                            year, 
                            duration
                        )
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (song_id)
                        DO UPDATE
                                SET song_id = EXCLUDED.song_id;
                 """)


artist_table_insert = ("""
                            INSERT INTO artists 
                            (
                                artist_id, 
                                name, 
                                location, 
                                latitude, 
                                longitude
                            )
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (artist_id)
                            DO UPDATE
                                    SET artist_id = EXCLUDED.artist_id;
                       """)


time_table_insert = ("""
                        INSERT INTO time 
                        (
                            start_time, 
                            hour, 
                            day, 
                            week, 
                            month, 
                            year, 
                            weekday
                         )
                         VALUES (%s, %s, %s, %s, %s, %s, %s)
                         ON CONFLICT (start_time)
                         DO UPDATE
                                  SET start_time = EXCLUDED.start_time

                     """)

# FIND SONGS

song_select = ("""
                    SELECT 
                        songs.song_id, 
                        artists.artist_id 
                    FROM songs 
                    JOIN artists on songs.artist_id = artists.artist_id 
                    WHERE title=%s and name =%s and duration=%s  
               """)

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create, ]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]