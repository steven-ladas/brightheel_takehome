/*********************************************
DB
*********************************************/
create database brightwheel_test;

/*********************************************
complete history of sourced lead csvs
*********************************************/

CREATE TABLE lead_sources (
    source_name VARCHAR(255),
    source_filename VARCHAR(255),
    source_record_number INT,
    source_extract_time INT,
    accepts_financial_aid VARCHAR(255),
    ages_served VARCHAR(255),
    capacity INT,
    certificate_expiration_date DATETIME,
    city VARCHAR(255),
    address1 VARCHAR(255),
    address2 VARCHAR(255),
    company VARCHAR(255),
    phone VARCHAR(50),
    phone2 VARCHAR(50),
    county VARCHAR(255),
    curriculum_type VARCHAR(255),
    email VARCHAR(255),
    first_name VARCHAR(255),
    language VARCHAR(255),
    last_name VARCHAR(255),
    license_status VARCHAR(255),
    license_issued DATETIME,
    license_number VARCHAR(255),
    license_renewed DATETIME,
    license_type VARCHAR(255),
    licensee_name VARCHAR(255),
    max_age INT,
    min_age INT,
    operator VARCHAR(255),
    provider_id VARCHAR(255),
    schedule TEXT,
    state VARCHAR(50),
    title VARCHAR(255),
    website_address VARCHAR(255),
    zip VARCHAR(10),
    facility_type VARCHAR(255),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


/*********************************************
latest leads by source

if duplicate rows exist based on phone/addy...
	just pull in one row
	totally arbitrary, room for improvement
*********************************************/
create view vw_lead_sources as

	with latest_sources as (
		select 	source_name,
				max(source_extract_time) source_extract_time
		from 	lead_sources
		group by
			source_name
	),

	unfiltered as (
		select	leads.*,
				row_number() over (partition by leads.phone, leads.phone2, leads.address1, leads.address2) rn
		from 	lead_sources leads
				inner join
				latest_sources ls
		on 		leads.source_name = ls.source_name
		and 	leads.source_extract_time = ls.source_extract_time
	)
    
	select 	accepts_financial_aid,
			ages_served,
			capacity,
			certificate_expiration_date,
			city ,
			address1,
			address2,
			company,
			phone,
			phone2,
			county,
			curriculum_type,
			email,
			first_name,
			language,
			last_name,
			license_status,
			license_issued,
			license_number,
			license_renewed,
			license_type,
			licensee_name,
			max_age,
			min_age,
			operator,
			provider_id,
			schedule,
			state,
			title,
			website_address,
			zip,
			facility_type
    from 	unfiltered
    where 	rn = 1;