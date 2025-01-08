CREATE TABLE IF NOT EXISTS usr.user (
	id		serial				not null
	,username	varchar(256)			not null
	,password	varchar(256)			not null

	,created_at	timestamp with time zone	not null	default current_timestamp
	,updated_at	timestamp with time zone	not null	default current_timestamp
	,delete_flag	boolean				not null	default false
)
;

ALTER TABLE usr.user ADD CONSTRAINT user_pk PRIMARY KEY (
	id
	,username
	,password
)
;

/*
select *
from usr.user
limit 100
;
*/
