

select * from properties_2017; -- 2,985,217

select parcelid, count(*). -- no duplicates 
from properties_2017
group by parcelid
order by parcelid desc;

select * 
from properties_2017
left join airconditioningtype using(airconditioningtypeid)
left join architecturalstyletype using(architecturalstyletypeid)
left join buildingclasstype using(buildingclasstypeid)
left join heatingorsystemtype using(heatingorsystemtypeid)
left join propertylandusetype using(propertylandusetypeid)
left join storytype using(storytypeid)
left join typeconstructiontype using(typeconstructiontypeid);

create temporary table bayes_828.t1 as (select * 
from predictions_2017
where (parcelid, transactiondate) in (select parcelid, max(transactiondate)
									  from predictions_2017
									  group by parcelid));


select * from t1;





left join properties_2017 using(parcelid)
left join airconditioningtype using(airconditioningtypeid)
left join architecturalstyletype using(architecturalstyletypeid)
left join buildingclasstype using(buildingclasstypeid)
left join heatingorsystemtype using(heatingorsystemtypeid)
left join propertylandusetype using(propertylandusetypeid)
left join storytype using(storytypeid)
left join typeconstructiontype using(typeconstructiontypeid)

where (parcelid, transactiondate) in (select parcelid, max(transactiondate)
									  from predictions_2017
									  group by parcelid)
									  
and latitude is not null
and longitude is not null;