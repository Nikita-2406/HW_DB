select executor_name, count(*) 
from executor e 
join genre_executor ge on e.executor_id = ge.executor_id 
group by e.executor_name;

select count(*)
from track t 
join album a on t.item_id = a.album_id 
where a.release_date  between '2019-01-01' and '2020-12-31';

select a.album_name, avg(t.duration)
from album a 
join track t on a.album_id = t.item_id 
group by a.album_name;

select e.executor_name 
from executor e 
join executors_alboms ea on e.executor_id = ea.executor_id 
join album a on ea.album_id = a.album_id 
where a.release_date not between '2020-01-01' and '2020-12-31';

select c.collection_name 
from collection c 
join track_colection tc on tc.collection_id = c.collection_id 
join track t on tc.track_id = t.track_id 
join album a on t.item_id = a.album_id 
join executors_alboms ea on a.album_id = ea.album_id 
join executor e on ea.executor_id = e.executor_id 
where e.executor_name = 'Михаил Круг'
group by c.collection_name;

select a.album_name 
from album a 
join executors_alboms ea on a.album_id = ea.album_id 
join executor e on ea.executor_id = e.executor_id 
join genre_executor ge on e.executor_id = ge.executor_id 
group by album_name, ge.executor_id 
having count(genre_id) > 1;

select t.track_name 
from track t 
left join track_colection tc on t.track_id = tc.track_id 
where tc.collection_id is null;

select e.executor_name 
from track t 
join album a on t.item_id = a.album_id 
join executors_alboms ea on a.album_id = ea.album_id 
join executor e on ea.executor_id = e.executor_id 
where t.duration = (select min(duration) from track);

select a.album_name
from track t
	join album a on t.item_id = a.album_id 
group by a.album_name
having count(*) = (
	select 
		count(*)	
	from 
		track
	group by item_id
	order by count(*) asc
	limit 1)	
	






select a.album_name
	from track t
	join album a on t.item_id = a.album_id 
	group by 
