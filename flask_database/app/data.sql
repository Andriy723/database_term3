INSERT INTO iot_db.creator (creator_id, first_name, last_name, birth_date) VALUES
(1, 'qw', 'qqq', '12-10-2023'),
(2, 'w', 'www', '11-01-2028'),
(3, 'f', 'fff', '07-11-2021'),
(4, 's', 'sss', '07-11-2021'),
(5, 'h', 'hhh', '07-11-2021'),
(6, 'k', 'kkk', '07-11-2021'),
(7, 'p', 'ppp', '07-11-2021'),
(8, 'c', 'ccc', '07-11-2021'),
(9, 'b', 'bbb', '07-11-2021'),
(10, 'r', 'rrr', '12-10-2023');

INSERT INTO iot_db.music_labels (id_music_labels, label_name, creator_creator_id) VALUES
(1, 'qw', 1),
(2, 'w', 2),
(3, 'f', 3),
(4, 's', 4),
(5, 'h', 5),
(6, 'k', 6),
(7, 'p', 7),
(8, 'c', 8),
(9, 'b', 9),
(10, 'r', 10);

INSERT INTO iot_db.albom (id_albom, songs_num, name, creator_creator_id, music_labels_id_music_labels, music_labels_creator_creator_id) VALUES
(1, '444', 'r', 1, 1, 1),
(2, '1', 't', 2, 2, 2),
(3, '66546', 'y', 3, 3, 3),
(4, '98765', 'u', 4, 4, 4),
(5, '5678994', 'b', 5, 5, 5),
(6, '98766', 'g', 6, 6, 6),
(7, '7316', 'f', 7, 7, 7),
(8, '8679', 'd', 8, 8, 8),
(9, '22442', 'n', 9, 9, 9),
(10, '4216', 'v', 10, 10, 10);

INSERT INTO iot_db.music (id, duration, name, albom_id_albom, creator_creator_id) VALUES
(1, '56', 'rq', 1, 1),
(2, '22', 'tq', 2, 2),
(3, '7', 'yq', 3, 3),
(4, '5', 'uq', 4, 4),
(5, '3', 'bq', 5, 5),
(6, '4', 'gq', 6, 6),
(7, '2', 'fq', 7, 7),
(8, '8', 'dq', 8, 8),
(9, '1', 'nq', 9, 9),
(10, '2', 'vq', 10, 10);

INSERT INTO iot_db.janre (janre_id, name) VALUES
(1, 'rq'),
(2, 'tq'),
(3, 'yq'),
(4, 'uq'),
(5, 'bq'),
(6, 'gq'),
(7, 'fq'),
(8, 'dq'),
(9, 'nq'),
(10, 'vq');

INSERT INTO iot_db.country (country_id, city, current_place) VALUES
(1, 'rqq', 'w'),
(2, 'tqq', 'ww'),
(3, 'yqq', 'www'),
(4, 'uqq', 'wwww'),
(5, 'bqq', 'wwwww'),
(6, 'gqq', 'wwwwww'),
(7, 'fqq', 'wwwwwww'),
(8, 'dqq', 'wwwwwwww'),
(9, 'nqq', 'wwwwwwwww'),
(10, 'vqq', 'wwwwwwwwww');

INSERT INTO iot_db.downloading_song (id_downloading_song, downloading_num, music_id, music_albom_id_albom) VALUES
(1, '111', 1, 1),
(2, '222', 2, 2),
(3, '333', 3, 3),
(4, '444', 4, 4),
(5, '555', 5, 5),
(6, '666', 6, 6),
(7, '777', 7, 7),
(8, '888', 8, 8),
(9, '999', 9, 9),
(10, '101010', 10, 10);

INSERT INTO iot_db.follower (id_follower, followers_num, creator_creator_id) VALUES
(1, '111', 1),
(2, '222', 2),
(3, '333', 3),
(4, '444', 4),
(5, '555', 5),
(6, '666', 6),
(7, '777', 7),
(8, '888', 8),
(9, '999', 9),
(10, '101010', 10);

INSERT INTO iot_db.person_profile (id_person_profile, first_name, last_name, birth_date, follower_id_follower, follower_creator_creator_id) VALUES
(1, 'q', 'qq', '12-12-2012', 1, 1),
(2, 'w', 'ww', '11-11-2011', 2, 2),
(3, 'e', 'ee', '10-10-2010', 3, 3),
(4, 't', 'tt', '09-09-2009', 4, 4),
(5, 'y', 'yy', '08-08-2008', 5, 5),
(6, 'u', 'uu', '07-07-2007', 6, 6),
(7, 'i', 'ii', '06-06-2006', 7, 7),
(8, 'a', 'aa', '05-05-2005', 8, 8),
(9, 's', 'ss', '04-04-2004', 9, 9),
(10, 'd', 'dd', '03-03-2003', 10, 10);

INSERT INTO iot_db.country_has_music (country_country_id, music_id, music_albom_id_albom, price, price_curency) VALUES
(1, 1, 1, '343', 'dr'),
(2, 2, 2, '5677', 'drdr'),
(3, 3, 3, '1489679', 'tr'),
(4, 4, 4, '12345', 'trtr'),
(5, 5, 5, '5638', 'rt'),
(6, 6, 6, '97446', 'rtrt'),
(7, 7, 7, '85553', 'uy'),
(8, 8, 8, '847635', 'uy'),
(9, 9, 9, '745578', 'io'),
(10, 10, 10, '245653', 'io');

INSERT INTO iot_db.janre_has_music (janre_janre_id, music_id, music_albom_id_albom, music_creator_creator_id) VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 4),
(5, 5, 5, 5),
(6, 6, 6, 6),
(7, 7, 7, 7),
(8, 8, 8, 8),
(9, 9, 9, 9),
(10, 10, 10, 10);

INSERT INTO iot_db.downloading_song_has_person_profile (downloading_song_id_downloading_song, downloading_song_music_id,
downloading_song_music_albom_id_albom, person_profile_id_person_profile, person_profile_follower_id_follower,
person_profile_follower_creator_creator_id) VALUES
(1, 1, 1, 1, 1, 1),
(2, 2, 2, 2, 2, 2),
(3, 3, 3, 3, 3, 3),
(4, 4, 4, 4, 4, 4),
(5, 5, 5, 5, 5, 5),
(6, 6, 6, 6, 6, 6),
(7, 7, 7, 7, 7, 7),
(8, 8, 8, 8, 8, 8),
(9, 9, 9, 9, 9, 9),
(10, 10, 10, 10, 10, 10);

INSERT INTO iot_db.follower_has_creator (follower_id_follower, follower_creator_creator_id, creator_creator_id) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);

INSERT INTO iot_db.creator_has_music_labels (creator_creator_id, music_labels_id_music_labels, music_labels_creator_creator_id) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);
