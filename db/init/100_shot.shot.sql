CREATE TABLE IF NOT EXISTS shot.shot(
	date			timestamp with time zone	not null

	,club			varchar(32)			null
	,club_speed		numeric(18, 9)			null
	,attack_angle		numeric(18, 9)			null
	,club_path		numeric(18, 9)			null
	,low_point		numeric(18, 9)			null
	,swing_plane		numeric(18, 9)			null
	,swing_direction	numeric(18, 9)			null
	,dynamic_loft		numeric(18, 9)			null
	,face_angle		numeric(18, 9)			null
	,face_to_path		numeric(18, 9)			null
	,ball_speed		numeric(18, 9)			null
	,smash_factor		numeric(18, 9)			null
	,launch_angle		numeric(18, 9)			null
	,launch_direction	numeric(18, 9)			null
	,spin_rate		numeric(18, 9)			null
	,spin_axis		numeric(18, 9)			null
	,max_height_dist	numeric(18, 9)			null
	,max_height_height	numeric(18, 9)			null
	,max_height_side	numeric(18, 9)			null
	,carry_flat_length	numeric(18, 9)			null
	,carry_flat_side	numeric(18, 9)			null
	,carry_flat_land_angle	numeric(18, 9)			null
	,carry_flat_ball_speed	numeric(18, 9)			null
	,carry_flat_time	numeric(18, 9)			null
	,total_flat_length	numeric(18, 9)			null
	,total_flat_side	numeric(18, 9)			null
	,dynamic_lie		numeric(18, 9)			null
	,impact_offset		numeric(18, 9)			null
	,impact_height		numeric(18, 9)			null
	,curve			numeric(18, 9)			null
	,spin_axis_sim		numeric(18, 9)			null
	,curve_sim		numeric(18, 9)			null
	,carry_sim		numeric(18, 9)			null
	,total_sim		numeric(18, 9)			null
	,carry_side_sim		numeric(18, 9)			null
	,total_side_sim		numeric(18, 9)			null
	,landing_angle_sim	numeric(18, 9)			null
	,landing_side_sim	numeric(18, 9)			null

	,created_at		timestamp with time zone	not null	default current_timestamp
	,updated_at		timestamp with time zone	not null	default current_timestamp
	,delete_flag		boolean				not null	default false
);

ALTER TABLE shot.shot ADD CONSTRAINT pk_shot_shot PRIMARY KEY (
	date
);

/*
select *
from shot.shot
limit 100
;
*/
