select album_name, release_date from album
where release_date between '2018-01-01' and '2018-12-31';
select track_name, duration from track
order by duration desc 
limit 1;
select  track_name, duration from track
where duration >='00:03:30';
select collection_name from collection 
where release_date between '2018-01-01' and '2020-12-31';
select track_name from track
where track_name like '%мой%' or track_name like '%my%';
select executor_name from executor
where executor_name not like '% %';