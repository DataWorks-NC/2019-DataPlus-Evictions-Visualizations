etm_2012_2019 = """select 
	src.docket_num,
	src.fips,(mod(cast(src.fips as bigint), 10000) * 1.0) / 100 as tract, 
	src.data_year as year,
    src.status_date as month,
    src.date as status_date,
    src.process,
    case when src.data_year = 2012 and src.status_date = 1 then 1 else 0 end as Jan_2012,
    case when src.data_year = 2012 and src.status_date = 2 then 1 else 0 end as Feb_2012,
    case when src.data_year = 2012 and src.status_date = 3 then 1 else 0 end as Mar_2012,
    case when src.data_year = 2012 and src.status_date = 4 then 1 else 0 end as Apr_2012,
    case when src.data_year = 2012 and src.status_date = 5 then 1 else 0 end as May_2012,
    case when src.data_year = 2012 and src.status_date = 6 then 1 else 0 end as Jun_2012,
    case when src.data_year = 2012 and src.status_date = 7 then 1 else 0 end as Jul_2012,
    case when src.data_year = 2012 and src.status_date = 8 then 1 else 0 end as Aug_2012,
    case when src.data_year = 2012 and src.status_date = 9 then 1 else 0 end as Sep_2012,
    case when src.data_year = 2012 and src.status_date = 10 then 1 else 0 end as Oct_2012,
    case when src.data_year = 2012 and src.status_date = 11 then 1 else 0 end as Nov_2012,
    case when src.data_year = 2012 and src.status_date = 12 then 1 else 0 end as Dec_2012,
    case when src.data_year = 2013 and src.status_date = 1 then 1 else 0 end as Jan_2013,
    case when src.data_year = 2013 and src.status_date = 2 then 1 else 0 end as Feb_2013,
    case when src.data_year = 2013 and src.status_date = 3 then 1 else 0 end as Mar_2013,
    case when src.data_year = 2013 and src.status_date = 4 then 1 else 0 end as Apr_2013,
    case when src.data_year = 2013 and src.status_date = 5 then 1 else 0 end as May_2013,
    case when src.data_year = 2013 and src.status_date = 6 then 1 else 0 end as Jun_2013,
    case when src.data_year = 2013 and src.status_date = 7 then 1 else 0 end as Jul_2013,
    case when src.data_year = 2013 and src.status_date = 8 then 1 else 0 end as Aug_2013,
    case when src.data_year = 2013 and src.status_date = 9 then 1 else 0 end as Sep_2013,
    case when src.data_year = 2013 and src.status_date = 10 then 1 else 0 end as Oct_2013,
    case when src.data_year = 2013 and src.status_date = 11 then 1 else 0 end as Nov_2013,
    case when src.data_year = 2013 and src.status_date = 12 then 1 else 0 end as Dec_2013,
    case when src.data_year = 2014 and src.status_date = 1 then 1 else 0 end as Jan_2014,
    case when src.data_year = 2014 and src.status_date = 2 then 1 else 0 end as Feb_2014,
    case when src.data_year = 2014 and src.status_date = 3 then 1 else 0 end as Mar_2014,
    case when src.data_year = 2014 and src.status_date = 4 then 1 else 0 end as Apr_2014,
    case when src.data_year = 2014 and src.status_date = 5 then 1 else 0 end as May_2014,
    case when src.data_year = 2014 and src.status_date = 6 then 1 else 0 end as Jun_2014,
    case when src.data_year = 2014 and src.status_date = 7 then 1 else 0 end as Jul_2014,
    case when src.data_year = 2014 and src.status_date = 8 then 1 else 0 end as Aug_2014,
    case when src.data_year = 2014 and src.status_date = 9 then 1 else 0 end as Sep_2014,
    case when src.data_year = 2014 and src.status_date = 10 then 1 else 0 end as Oct_2014,
    case when src.data_year = 2014 and src.status_date = 11 then 1 else 0 end as Nov_2014,
    case when src.data_year = 2014 and src.status_date = 12 then 1 else 0 end as Dec_2014,
    case when src.data_year = 2015 and src.status_date = 1 then 1 else 0 end as Jan_2015,
    case when src.data_year = 2015 and src.status_date = 2 then 1 else 0 end as Feb_2015,
    case when src.data_year = 2015 and src.status_date = 3 then 1 else 0 end as Mar_2015,
    case when src.data_year = 2015 and src.status_date = 4 then 1 else 0 end as Apr_2015,
    case when src.data_year = 2015 and src.status_date = 5 then 1 else 0 end as May_2015,
    case when src.data_year = 2015 and src.status_date = 6 then 1 else 0 end as Jun_2015,
    case when src.data_year = 2015 and src.status_date = 7 then 1 else 0 end as Jul_2015,
    case when src.data_year = 2015 and src.status_date = 8 then 1 else 0 end as Aug_2015,
    case when src.data_year = 2015 and src.status_date = 9 then 1 else 0 end as Sep_2015,
    case when src.data_year = 2015 and src.status_date = 10 then 1 else 0 end as Oct_2015,
    case when src.data_year = 2015 and src.status_date = 11 then 1 else 0 end as Nov_2015,
    case when src.data_year = 2015 and src.status_date = 12 then 1 else 0 end as Dec_2015,
    case when src.data_year = 2016 and src.status_date = 1 then 1 else 0 end as Jan_2016,
    case when src.data_year = 2016 and src.status_date = 2 then 1 else 0 end as Feb_2016,
    case when src.data_year = 2016 and src.status_date = 3 then 1 else 0 end as Mar_2016,
    case when src.data_year = 2016 and src.status_date = 4 then 1 else 0 end as Apr_2016,
    case when src.data_year = 2016 and src.status_date = 5 then 1 else 0 end as May_2016,
    case when src.data_year = 2016 and src.status_date = 6 then 1 else 0 end as Jun_2016,
    case when src.data_year = 2016 and src.status_date = 7 then 1 else 0 end as Jul_2016,
    case when src.data_year = 2016 and src.status_date = 8 then 1 else 0 end as Aug_2016,
    case when src.data_year = 2016 and src.status_date = 9 then 1 else 0 end as Sep_2016,
    case when src.data_year = 2016 and src.status_date = 10 then 1 else 0 end as Oct_2016,
    case when src.data_year = 2016 and src.status_date = 11 then 1 else 0 end as Nov_2016,
    case when src.data_year = 2016 and src.status_date = 12 then 1 else 0 end as Dec_2016,
    case when src.data_year = 2017 and src.status_date = 1 then 1 else 0 end as Jan_2017,
    case when src.data_year = 2017 and src.status_date = 2 then 1 else 0 end as Feb_2017,
    case when src.data_year = 2017 and src.status_date = 3 then 1 else 0 end as Mar_2017,
    case when src.data_year = 2017 and src.status_date = 4 then 1 else 0 end as Apr_2017,
    case when src.data_year = 2017 and src.status_date = 5 then 1 else 0 end as May_2017,
    case when src.data_year = 2017 and src.status_date = 6 then 1 else 0 end as Jun_2017,
    case when src.data_year = 2017 and src.status_date = 7 then 1 else 0 end as Jul_2017,
    case when src.data_year = 2017 and src.status_date = 8 then 1 else 0 end as Aug_2017,
    case when src.data_year = 2017 and src.status_date = 9 then 1 else 0 end as Sep_2017,
    case when src.data_year = 2017 and src.status_date = 10 then 1 else 0 end as Oct_2017,
    case when src.data_year = 2017 and src.status_date = 11 then 1 else 0 end as Nov_2017,
    case when src.data_year = 2017 and src.status_date = 12 then 1 else 0 end as Dec_2017,
    case when src.data_year = 2018 and src.status_date = 1 then 1 else 0 end as Jan_2018,
    case when src.data_year = 2018 and src.status_date = 2 then 1 else 0 end as Feb_2018,
    case when src.data_year = 2018 and src.status_date = 3 then 1 else 0 end as Mar_2018,
    case when src.data_year = 2018 and src.status_date = 4 then 1 else 0 end as Apr_2018,
    case when src.data_year = 2018 and src.status_date = 5 then 1 else 0 end as May_2018,
    case when src.data_year = 2018 and src.status_date = 6 then 1 else 0 end as Jun_2018,
    case when src.data_year = 2018 and src.status_date = 7 then 1 else 0 end as Jul_2018,
    case when src.data_year = 2018 and src.status_date = 8 then 1 else 0 end as Aug_2018,
    case when src.data_year = 2018 and src.status_date = 9 then 1 else 0 end as Sep_2018,
    case when src.data_year = 2018 and src.status_date = 10 then 1 else 0 end as Oct_2018,
    case when src.data_year = 2018 and src.status_date = 11 then 1 else 0 end as Nov_2018,
    case when src.data_year = 2018 and src.status_date = 12 then 1 else 0 end as Dec_2018,
    case when src.data_year = 2019 and src.status_date = 1 then 1 else 0 end as Jan_2019,
    case when src.data_year = 2019 and src.status_date = 2 then 1 else 0 end as Feb_2019,
    case when src.data_year = 2019 and src.status_date = 3 then 1 else 0 end as Mar_2019,
    case when src.data_year = 2019 and src.status_date = 4 then 1 else 0 end as Apr_2019,
    case when src.data_year = 2019 and src.status_date = 5 then 1 else 0 end as May_2019,
    case when src.data_year = 2019 and src.status_date = 6 then 1 else 0 end as Jun_2019,
    case when src.data_year = 2019 and src.status_date = 7 then 1 else 0 end as Jul_2019,
    case when src.data_year = 2019 and src.status_date = 8 then 1 else 0 end as Aug_2019,
    case when src.data_year = 2019 and src.status_date = 9 then 1 else 0 end as Sep_2019,
    case when src.data_year = 2019 and src.status_date = 10 then 1 else 0 end as Oct_2019,
    case when src.data_year = 2019 and src.status_date = 11 then 1 else 0 end as Nov_2019,
    case when src.data_year = 2019 and src.status_date = 12 then 1 else 0 end as Dec_2019
FROM (
SELECT
       h.docket_num,
       h.fips,
       h.data_year,
       cast(substring(cast(h.status_date as varchar(10)), 6, 2) as int) as status_date,
       h.status_date as date,
       h.process
    FROM housing.evictions__tract h) as src"""
etm_2000_2011 = """select
    src.docket_num,
    src.fips,
    (mod(cast(src.fips as bigint), 10000) * 1.0) / 100 as tract,
    src.data_year as year,
    src.month,
    src.date as status_date,
    src.process,
    case when src.data_year = 2000 and src.month = 1 then 1 else 0 end as Jan_2000,
    case when src.data_year = 2000 and src.month = 2 then 1 else 0 end as Feb_2000,
    case when src.data_year = 2000 and src.month = 3 then 1 else 0 end as Mar_2000,
    case when src.data_year = 2000 and src.month = 4 then 1 else 0 end as Apr_2000,
    case when src.data_year = 2000 and src.month = 5 then 1 else 0 end as May_2000,
    case when src.data_year = 2000 and src.month = 6 then 1 else 0 end as Jun_2000,
    case when src.data_year = 2000 and src.month = 7 then 1 else 0 end as Jul_2000,
    case when src.data_year = 2000 and src.month = 8 then 1 else 0 end as Aug_2000,
    case when src.data_year = 2000 and src.month = 9 then 1 else 0 end as Sep_2000,
    case when src.data_year = 2000 and src.month = 10 then 1 else 0 end as Oct_2000,
    case when src.data_year = 2000 and src.month = 11 then 1 else 0 end as Nov_2000,
    case when src.data_year = 2000 and src.month = 12 then 1 else 0 end as Dec_2000,
    case when src.data_year = 2001 and src.month = 1 then 1 else 0 end as Jan_2001,
    case when src.data_year = 2001 and src.month = 2 then 1 else 0 end as Feb_2001,
    case when src.data_year = 2001 and src.month = 3 then 1 else 0 end as Mar_2001,
    case when src.data_year = 2001 and src.month = 4 then 1 else 0 end as Apr_2001,
    case when src.data_year = 2001 and src.month = 5 then 1 else 0 end as May_2001,
    case when src.data_year = 2001 and src.month = 6 then 1 else 0 end as Jun_2001,
    case when src.data_year = 2001 and src.month = 7 then 1 else 0 end as Jul_2001,
    case when src.data_year = 2001 and src.month = 8 then 1 else 0 end as Aug_2001,
    case when src.data_year = 2001 and src.month = 9 then 1 else 0 end as Sep_2001,
    case when src.data_year = 2001 and src.month = 10 then 1 else 0 end as Oct_2001,
    case when src.data_year = 2001 and src.month = 11 then 1 else 0 end as Nov_2001,
    case when src.data_year = 2001 and src.month = 12 then 1 else 0 end as Dec_2001,
    case when src.data_year = 2002 and src.month = 1 then 1 else 0 end as Jan_2002,
    case when src.data_year = 2002 and src.month = 2 then 1 else 0 end as Feb_2002,
    case when src.data_year = 2002 and src.month = 3 then 1 else 0 end as Mar_2002,
    case when src.data_year = 2002 and src.month = 4 then 1 else 0 end as Apr_2002,
    case when src.data_year = 2002 and src.month = 5 then 1 else 0 end as May_2002,
    case when src.data_year = 2002 and src.month = 6 then 1 else 0 end as Jun_2002,
    case when src.data_year = 2002 and src.month = 7 then 1 else 0 end as Jul_2002,
    case when src.data_year = 2002 and src.month = 8 then 1 else 0 end as Aug_2002,
    case when src.data_year = 2002 and src.month = 9 then 1 else 0 end as Sep_2002,
    case when src.data_year = 2002 and src.month = 10 then 1 else 0 end as Oct_2002,
    case when src.data_year = 2002 and src.month = 11 then 1 else 0 end as Nov_2002,
    case when src.data_year = 2002 and src.month = 12 then 1 else 0 end as Dec_2002,
    case when src.data_year = 2003 and src.month = 1 then 1 else 0 end as Jan_2003,
    case when src.data_year = 2003 and src.month = 2 then 1 else 0 end as Feb_2003,
    case when src.data_year = 2003 and src.month = 3 then 1 else 0 end as Mar_2003,
    case when src.data_year = 2003 and src.month = 4 then 1 else 0 end as Apr_2003,
    case when src.data_year = 2003 and src.month = 5 then 1 else 0 end as May_2003,
    case when src.data_year = 2003 and src.month = 6 then 1 else 0 end as Jun_2003,
    case when src.data_year = 2003 and src.month = 7 then 1 else 0 end as Jul_2003,
    case when src.data_year = 2003 and src.month = 8 then 1 else 0 end as Aug_2003,
    case when src.data_year = 2003 and src.month = 9 then 1 else 0 end as Sep_2003,
    case when src.data_year = 2003 and src.month = 10 then 1 else 0 end as Oct_2003,
    case when src.data_year = 2003 and src.month = 11 then 1 else 0 end as Nov_2003,
    case when src.data_year = 2003 and src.month = 12 then 1 else 0 end as Dec_2003,
    case when src.data_year = 2004 and src.month = 1 then 1 else 0 end as Jan_2004,
    case when src.data_year = 2004 and src.month = 2 then 1 else 0 end as Feb_2004,
    case when src.data_year = 2004 and src.month = 3 then 1 else 0 end as Mar_2004,
    case when src.data_year = 2004 and src.month = 4 then 1 else 0 end as Apr_2004,
    case when src.data_year = 2004 and src.month = 5 then 1 else 0 end as May_2004,
    case when src.data_year = 2004 and src.month = 6 then 1 else 0 end as Jun_2004,
    case when src.data_year = 2004 and src.month = 7 then 1 else 0 end as Jul_2004,
    case when src.data_year = 2004 and src.month = 8 then 1 else 0 end as Aug_2004,
    case when src.data_year = 2004 and src.month = 9 then 1 else 0 end as Sep_2004,
    case when src.data_year = 2004 and src.month = 10 then 1 else 0 end as Oct_2004,
    case when src.data_year = 2004 and src.month = 11 then 1 else 0 end as Nov_2004,
    case when src.data_year = 2004 and src.month = 12 then 1 else 0 end as Dec_2004,
    case when src.data_year = 2005 and src.month = 1 then 1 else 0 end as Jan_2005,
    case when src.data_year = 2005 and src.month = 2 then 1 else 0 end as Feb_2005,
    case when src.data_year = 2005 and src.month = 3 then 1 else 0 end as Mar_2005,
    case when src.data_year = 2005 and src.month = 4 then 1 else 0 end as Apr_2005,
    case when src.data_year = 2005 and src.month = 5 then 1 else 0 end as May_2005,
    case when src.data_year = 2005 and src.month = 6 then 1 else 0 end as Jun_2005,
    case when src.data_year = 2005 and src.month = 7 then 1 else 0 end as Jul_2005,
    case when src.data_year = 2005 and src.month = 8 then 1 else 0 end as Aug_2005,
    case when src.data_year = 2005 and src.month = 9 then 1 else 0 end as Sep_2005,
    case when src.data_year = 2005 and src.month = 10 then 1 else 0 end as Oct_2005,
    case when src.data_year = 2005 and src.month = 11 then 1 else 0 end as Nov_2005,
    case when src.data_year = 2005 and src.month = 12 then 1 else 0 end as Dec_2005,
    case when src.data_year = 2006 and src.month = 1 then 1 else 0 end as Jan_2006,
    case when src.data_year = 2006 and src.month = 2 then 1 else 0 end as Feb_2006,
    case when src.data_year = 2006 and src.month = 3 then 1 else 0 end as Mar_2006,
    case when src.data_year = 2006 and src.month = 4 then 1 else 0 end as Apr_2006,
    case when src.data_year = 2006 and src.month = 5 then 1 else 0 end as May_2006,
    case when src.data_year = 2006 and src.month = 6 then 1 else 0 end as Jun_2006,
    case when src.data_year = 2006 and src.month = 7 then 1 else 0 end as Jul_2006,
    case when src.data_year = 2006 and src.month = 8 then 1 else 0 end as Aug_2006,
    case when src.data_year = 2006 and src.month = 9 then 1 else 0 end as Sep_2006,
    case when src.data_year = 2006 and src.month = 10 then 1 else 0 end as Oct_2006,
    case when src.data_year = 2006 and src.month = 11 then 1 else 0 end as Nov_2006,
    case when src.data_year = 2006 and src.month = 12 then 1 else 0 end as Dec_2006,
    case when src.data_year = 2007 and src.month = 1 then 1 else 0 end as Jan_2007,
    case when src.data_year = 2007 and src.month = 2 then 1 else 0 end as Feb_2007,
    case when src.data_year = 2007 and src.month = 3 then 1 else 0 end as Mar_2007,
    case when src.data_year = 2007 and src.month = 4 then 1 else 0 end as Apr_2007,
    case when src.data_year = 2007 and src.month = 5 then 1 else 0 end as May_2007,
    case when src.data_year = 2007 and src.month = 6 then 1 else 0 end as Jun_2007,
    case when src.data_year = 2007 and src.month = 7 then 1 else 0 end as Jul_2007,
    case when src.data_year = 2007 and src.month = 8 then 1 else 0 end as Aug_2007,
    case when src.data_year = 2007 and src.month = 9 then 1 else 0 end as Sep_2007,
    case when src.data_year = 2007 and src.month = 10 then 1 else 0 end as Oct_2007,
    case when src.data_year = 2007 and src.month = 11 then 1 else 0 end as Nov_2007,
    case when src.data_year = 2007 and src.month = 12 then 1 else 0 end as Dec_2007,
    case when src.data_year = 2008 and src.month = 1 then 1 else 0 end as Jan_2008,
    case when src.data_year = 2008 and src.month = 2 then 1 else 0 end as Feb_2008,
    case when src.data_year = 2008 and src.month = 3 then 1 else 0 end as Mar_2008,
    case when src.data_year = 2008 and src.month = 4 then 1 else 0 end as Apr_2008,
    case when src.data_year = 2008 and src.month = 5 then 1 else 0 end as May_2008,
    case when src.data_year = 2008 and src.month = 6 then 1 else 0 end as Jun_2008,
    case when src.data_year = 2008 and src.month = 7 then 1 else 0 end as Jul_2008,
    case when src.data_year = 2008 and src.month = 8 then 1 else 0 end as Aug_2008,
    case when src.data_year = 2008 and src.month = 9 then 1 else 0 end as Sep_2008,
    case when src.data_year = 2008 and src.month = 10 then 1 else 0 end as Oct_2008,
    case when src.data_year = 2008 and src.month = 11 then 1 else 0 end as Nov_2008,
    case when src.data_year = 2008 and src.month = 12 then 1 else 0 end as Dec_2008,
    case when src.data_year = 2009 and src.month = 1 then 1 else 0 end as Jan_2009,
    case when src.data_year = 2009 and src.month = 2 then 1 else 0 end as Feb_2009,
    case when src.data_year = 2009 and src.month = 3 then 1 else 0 end as Mar_2009,
    case when src.data_year = 2009 and src.month = 4 then 1 else 0 end as Apr_2009,
    case when src.data_year = 2009 and src.month = 5 then 1 else 0 end as May_2009,
    case when src.data_year = 2009 and src.month = 6 then 1 else 0 end as Jun_2009,
    case when src.data_year = 2009 and src.month = 7 then 1 else 0 end as Jul_2009,
    case when src.data_year = 2009 and src.month = 8 then 1 else 0 end as Aug_2009,
    case when src.data_year = 2009 and src.month = 9 then 1 else 0 end as Sep_2009,
    case when src.data_year = 2009 and src.month = 10 then 1 else 0 end as Oct_2009,
    case when src.data_year = 2009 and src.month = 11 then 1 else 0 end as Nov_2009,
    case when src.data_year = 2009 and src.month = 12 then 1 else 0 end as Dec_2009,
    case when src.data_year = 2010 and src.month = 1 then 1 else 0 end as Jan_2010,
    case when src.data_year = 2010 and src.month = 2 then 1 else 0 end as Feb_2010,
    case when src.data_year = 2010 and src.month = 3 then 1 else 0 end as Mar_2010,
    case when src.data_year = 2010 and src.month = 4 then 1 else 0 end as Apr_2010,
    case when src.data_year = 2010 and src.month = 5 then 1 else 0 end as May_2010,
    case when src.data_year = 2010 and src.month = 6 then 1 else 0 end as Jun_2010,
    case when src.data_year = 2010 and src.month = 7 then 1 else 0 end as Jul_2010,
    case when src.data_year = 2010 and src.month = 8 then 1 else 0 end as Aug_2010,
    case when src.data_year = 2010 and src.month = 9 then 1 else 0 end as Sep_2010,
    case when src.data_year = 2010 and src.month = 10 then 1 else 0 end as Oct_2010,
    case when src.data_year = 2010 and src.month = 11 then 1 else 0 end as Nov_2010,
    case when src.data_year = 2010 and src.month = 12 then 1 else 0 end as Dec_2010,
    case when src.data_year = 2011 and src.month = 1 then 1 else 0 end as Jan_2011,
    case when src.data_year = 2011 and src.month = 2 then 1 else 0 end as Feb_2011,
    case when src.data_year = 2011 and src.month = 3 then 1 else 0 end as Mar_2011,
    case when src.data_year = 2011 and src.month = 4 then 1 else 0 end as Apr_2011,
    case when src.data_year = 2011 and src.month = 5 then 1 else 0 end as May_2011,
    case when src.data_year = 2011 and src.month = 6 then 1 else 0 end as Jun_2011,
    case when src.data_year = 2011 and src.month = 7 then 1 else 0 end as Jul_2011,
    case when src.data_year = 2011 and src.month = 8 then 1 else 0 end as Aug_2011,
    case when src.data_year = 2011 and src.month = 9 then 1 else 0 end as Sep_2011,
    case when src.data_year = 2011 and src.month = 10 then 1 else 0 end as Oct_2011,
    case when src.data_year = 2011 and src.month = 11 then 1 else 0 end as Nov_2011,
    case when src.data_year = 2011 and src.month = 12 then 1 else 0 end as Dec_2011
FROM (
SELECT
       t.docket_num,
       t.fips,
       cast(t.data_year as int),
       cast(substring(cast(t.status_date as varchar(10)), 1, 2) as int) as month,
       t.status_date as date,
       t.process
    FROM (
    SELECT
       h.data_year,
       h.docket_num,
       h.process,
       h.status_dat as status_date,
       g.fips
        FROM (staging.eviction_processes_2000_2011_bgclip h
         JOIN geom.tract g ON (st_contains(st_transform(g.geom, 102719), st_transform(h.geom, 102719))))
             ) t) as src"""

ebm_2012_2019 = """select
    src.docket_num,
    src.fips,
    mod(cast(src.fips as bigint),10) as blockgroup,
    (mod(cast(floor(cast(src.fips as bigint) / 10) as bigint), 10000) * 1.0) / 100 as tract,
    src.data_year as year,
    src.status_date as month,
    src.date as status_date,
    src.process,
    case when src.data_year = 2012 and src.status_date = 1 then 1 else 0 end as Jan_2012,
    case when src.data_year = 2012 and src.status_date = 2 then 1 else 0 end as Feb_2012,
    case when src.data_year = 2012 and src.status_date = 3 then 1 else 0 end as Mar_2012,
    case when src.data_year = 2012 and src.status_date = 4 then 1 else 0 end as Apr_2012,
    case when src.data_year = 2012 and src.status_date = 5 then 1 else 0 end as May_2012,
    case when src.data_year = 2012 and src.status_date = 6 then 1 else 0 end as Jun_2012,
    case when src.data_year = 2012 and src.status_date = 7 then 1 else 0 end as Jul_2012,
    case when src.data_year = 2012 and src.status_date = 8 then 1 else 0 end as Aug_2012,
    case when src.data_year = 2012 and src.status_date = 9 then 1 else 0 end as Sep_2012,
    case when src.data_year = 2012 and src.status_date = 10 then 1 else 0 end as Oct_2012,
    case when src.data_year = 2012 and src.status_date = 11 then 1 else 0 end as Nov_2012,
    case when src.data_year = 2012 and src.status_date = 12 then 1 else 0 end as Dec_2012,
    case when src.data_year = 2013 and src.status_date = 1 then 1 else 0 end as Jan_2013,
    case when src.data_year = 2013 and src.status_date = 2 then 1 else 0 end as Feb_2013,
    case when src.data_year = 2013 and src.status_date = 3 then 1 else 0 end as Mar_2013,
    case when src.data_year = 2013 and src.status_date = 4 then 1 else 0 end as Apr_2013,
    case when src.data_year = 2013 and src.status_date = 5 then 1 else 0 end as May_2013,
    case when src.data_year = 2013 and src.status_date = 6 then 1 else 0 end as Jun_2013,
    case when src.data_year = 2013 and src.status_date = 7 then 1 else 0 end as Jul_2013,
    case when src.data_year = 2013 and src.status_date = 8 then 1 else 0 end as Aug_2013,
    case when src.data_year = 2013 and src.status_date = 9 then 1 else 0 end as Sep_2013,
    case when src.data_year = 2013 and src.status_date = 10 then 1 else 0 end as Oct_2013,
    case when src.data_year = 2013 and src.status_date = 11 then 1 else 0 end as Nov_2013,
    case when src.data_year = 2013 and src.status_date = 12 then 1 else 0 end as Dec_2013,
    case when src.data_year = 2014 and src.status_date = 1 then 1 else 0 end as Jan_2014,
    case when src.data_year = 2014 and src.status_date = 2 then 1 else 0 end as Feb_2014,
    case when src.data_year = 2014 and src.status_date = 3 then 1 else 0 end as Mar_2014,
    case when src.data_year = 2014 and src.status_date = 4 then 1 else 0 end as Apr_2014,
    case when src.data_year = 2014 and src.status_date = 5 then 1 else 0 end as May_2014,
    case when src.data_year = 2014 and src.status_date = 6 then 1 else 0 end as Jun_2014,
    case when src.data_year = 2014 and src.status_date = 7 then 1 else 0 end as Jul_2014,
    case when src.data_year = 2014 and src.status_date = 8 then 1 else 0 end as Aug_2014,
    case when src.data_year = 2014 and src.status_date = 9 then 1 else 0 end as Sep_2014,
    case when src.data_year = 2014 and src.status_date = 10 then 1 else 0 end as Oct_2014,
    case when src.data_year = 2014 and src.status_date = 11 then 1 else 0 end as Nov_2014,
    case when src.data_year = 2014 and src.status_date = 12 then 1 else 0 end as Dec_2014,
    case when src.data_year = 2015 and src.status_date = 1 then 1 else 0 end as Jan_2015,
    case when src.data_year = 2015 and src.status_date = 2 then 1 else 0 end as Feb_2015,
    case when src.data_year = 2015 and src.status_date = 3 then 1 else 0 end as Mar_2015,
    case when src.data_year = 2015 and src.status_date = 4 then 1 else 0 end as Apr_2015,
    case when src.data_year = 2015 and src.status_date = 5 then 1 else 0 end as May_2015,
    case when src.data_year = 2015 and src.status_date = 6 then 1 else 0 end as Jun_2015,
    case when src.data_year = 2015 and src.status_date = 7 then 1 else 0 end as Jul_2015,
    case when src.data_year = 2015 and src.status_date = 8 then 1 else 0 end as Aug_2015,
    case when src.data_year = 2015 and src.status_date = 9 then 1 else 0 end as Sep_2015,
    case when src.data_year = 2015 and src.status_date = 10 then 1 else 0 end as Oct_2015,
    case when src.data_year = 2015 and src.status_date = 11 then 1 else 0 end as Nov_2015,
    case when src.data_year = 2015 and src.status_date = 12 then 1 else 0 end as Dec_2015,
    case when src.data_year = 2016 and src.status_date = 1 then 1 else 0 end as Jan_2016,
    case when src.data_year = 2016 and src.status_date = 2 then 1 else 0 end as Feb_2016,
    case when src.data_year = 2016 and src.status_date = 3 then 1 else 0 end as Mar_2016,
    case when src.data_year = 2016 and src.status_date = 4 then 1 else 0 end as Apr_2016,
    case when src.data_year = 2016 and src.status_date = 5 then 1 else 0 end as May_2016,
    case when src.data_year = 2016 and src.status_date = 6 then 1 else 0 end as Jun_2016,
    case when src.data_year = 2016 and src.status_date = 7 then 1 else 0 end as Jul_2016,
    case when src.data_year = 2016 and src.status_date = 8 then 1 else 0 end as Aug_2016,
    case when src.data_year = 2016 and src.status_date = 9 then 1 else 0 end as Sep_2016,
    case when src.data_year = 2016 and src.status_date = 10 then 1 else 0 end as Oct_2016,
    case when src.data_year = 2016 and src.status_date = 11 then 1 else 0 end as Nov_2016,
    case when src.data_year = 2016 and src.status_date = 12 then 1 else 0 end as Dec_2016,
    case when src.data_year = 2017 and src.status_date = 1 then 1 else 0 end as Jan_2017,
    case when src.data_year = 2017 and src.status_date = 2 then 1 else 0 end as Feb_2017,
    case when src.data_year = 2017 and src.status_date = 3 then 1 else 0 end as Mar_2017,
    case when src.data_year = 2017 and src.status_date = 4 then 1 else 0 end as Apr_2017,
    case when src.data_year = 2017 and src.status_date = 5 then 1 else 0 end as May_2017,
    case when src.data_year = 2017 and src.status_date = 6 then 1 else 0 end as Jun_2017,
    case when src.data_year = 2017 and src.status_date = 7 then 1 else 0 end as Jul_2017,
    case when src.data_year = 2017 and src.status_date = 8 then 1 else 0 end as Aug_2017,
    case when src.data_year = 2017 and src.status_date = 9 then 1 else 0 end as Sep_2017,
    case when src.data_year = 2017 and src.status_date = 10 then 1 else 0 end as Oct_2017,
    case when src.data_year = 2017 and src.status_date = 11 then 1 else 0 end as Nov_2017,
    case when src.data_year = 2017 and src.status_date = 12 then 1 else 0 end as Dec_2017,
    case when src.data_year = 2018 and src.status_date = 1 then 1 else 0 end as Jan_2018,
    case when src.data_year = 2018 and src.status_date = 2 then 1 else 0 end as Feb_2018,
    case when src.data_year = 2018 and src.status_date = 3 then 1 else 0 end as Mar_2018,
    case when src.data_year = 2018 and src.status_date = 4 then 1 else 0 end as Apr_2018,
    case when src.data_year = 2018 and src.status_date = 5 then 1 else 0 end as May_2018,
    case when src.data_year = 2018 and src.status_date = 6 then 1 else 0 end as Jun_2018,
    case when src.data_year = 2018 and src.status_date = 7 then 1 else 0 end as Jul_2018,
    case when src.data_year = 2018 and src.status_date = 8 then 1 else 0 end as Aug_2018,
    case when src.data_year = 2018 and src.status_date = 9 then 1 else 0 end as Sep_2018,
    case when src.data_year = 2018 and src.status_date = 10 then 1 else 0 end as Oct_2018,
    case when src.data_year = 2018 and src.status_date = 11 then 1 else 0 end as Nov_2018,
    case when src.data_year = 2018 and src.status_date = 12 then 1 else 0 end as Dec_2018,
    case when src.data_year = 2019 and src.status_date = 1 then 1 else 0 end as Jan_2019,
    case when src.data_year = 2019 and src.status_date = 2 then 1 else 0 end as Feb_2019,
    case when src.data_year = 2019 and src.status_date = 3 then 1 else 0 end as Mar_2019,
    case when src.data_year = 2019 and src.status_date = 4 then 1 else 0 end as Apr_2019,
    case when src.data_year = 2019 and src.status_date = 5 then 1 else 0 end as May_2019,
    case when src.data_year = 2019 and src.status_date = 6 then 1 else 0 end as Jun_2019,
    case when src.data_year = 2019 and src.status_date = 7 then 1 else 0 end as Jul_2019,
    case when src.data_year = 2019 and src.status_date = 8 then 1 else 0 end as Aug_2019,
    case when src.data_year = 2019 and src.status_date = 9 then 1 else 0 end as Sep_2019,
    case when src.data_year = 2019 and src.status_date = 10 then 1 else 0 end as Oct_2019,
    case when src.data_year = 2019 and src.status_date = 11 then 1 else 0 end as Nov_2019,
    case when src.data_year = 2019 and src.status_date = 12 then 1 else 0 end as Dec_2019
FROM (
SELECT
       h.docket_num,
       h.fips,
       h.data_year,
       cast(substring(cast(h.status_date as varchar(10)), 6, 2) as int) as status_date,
       h.status_date as date,
       h.process
    FROM housing.evictions__blockgroup h) as src"""

ebm_2018oct_2019oct = """select
    g.fips,
    g.tract,
    g.blockgroup, 
    SUM(g.Oct_2018) as Oct_2018, 
    SUM(g.Nov_2018) as Nov_2018,
    SUM(g.Dec_2018) as Dec_2018,
    SUM(g.Jan_2019) as Jan_2019,
    SUM(g.Feb_2019) as Feb_2019,
    SUM(g.Mar_2019) as Mar_2019,
    SUM(g.Apr_2019) as Apr_2019,
    SUM(g.May_2019) as May_2019,
    SUM(g.Jun_2019) as Jun_2019,
    SUM(g.Jul_2019) as Jul_2019,
    SUM(g.Aug_2019) as Aug_2019,
    SUM(g.Sep_2019) as Sep_2019,
    SUM(g.Oct_2019) as Oct_2019 
FROM(
    SELECT
        src.fips,
        mod(cast(src.fips as bigint),10) as blockgroup,
        (mod(cast(floor(cast(src.fips as bigint) / 10) as bigint), 10000) * 1.0) / 100 as tract,
        case when src.data_year = 2018 and src.status_date = 10 then 1 else 0 end as Oct_2018,
        case when src.data_year = 2018 and src.status_date = 11 then 1 else 0 end as Nov_2018,
        case when src.data_year = 2018 and src.status_date = 12 then 1 else 0 end as Dec_2018,
        case when src.data_year = 2019 and src.status_date = 1 then 1 else 0 end as Jan_2019,
        case when src.data_year = 2019 and src.status_date = 2 then 1 else 0 end as Feb_2019,
        case when src.data_year = 2019 and src.status_date = 3 then 1 else 0 end as Mar_2019,
        case when src.data_year = 2019 and src.status_date = 4 then 1 else 0 end as Apr_2019,
        case when src.data_year = 2019 and src.status_date = 5 then 1 else 0 end as May_2019,
        case when src.data_year = 2019 and src.status_date = 6 then 1 else 0 end as Jun_2019,
        case when src.data_year = 2019 and src.status_date = 7 then 1 else 0 end as Jul_2019,
        case when src.data_year = 2019 and src.status_date = 8 then 1 else 0 end as Aug_2019,
        case when src.data_year = 2019 and src.status_date = 9 then 1 else 0 end as Sep_2019,
        case when src.data_year = 2019 and src.status_date = 10 then 1 else 0 end as Oct_2019
    FROM(
        SELECT
           CAST(fips as NUMERIC) as fips,
           data_year,
           cast(substring(cast(status_date as varchar(10)), 6, 2) as int) as status_date,
           status_date as date
        FROM housing.evictions__blockgroup
        WHERE (process = 'Summary Ejectment')
        ) as src 
    ) as g
GROUP BY (g.fips, g.tract, g.blockgroup)
ORDER BY g.fips"""

evictions_by_month_by_blockgroup_2018_to_present = """SELECT 
    year, 
    month, 
    fips, 
    count(*) as evictions
from (select date_part('year', status_date) as year, date_part('month', status_date) as month, fips
      from housing.evictions__blockgroup
      where status_date > date '2018-01-01') as e
group by year, month, fips order by fips"""

ebm_2000_2011 = """select
    src.docket_num,
    src.fips,
    mod(cast(src.fips as bigint),10) as blockgroup,
    (mod(cast(floor(cast(src.fips as bigint) / 10) as bigint), 10000) * 1.0) / 100 as tract,
    src.data_year as year,
    src.month,
    src.date as status_date,
    src.process,
    case when src.data_year = 2000 and src.month = 1 then 1 else 0 end as Jan_2000,
    case when src.data_year = 2000 and src.month = 2 then 1 else 0 end as Feb_2000,
    case when src.data_year = 2000 and src.month = 3 then 1 else 0 end as Mar_2000,
    case when src.data_year = 2000 and src.month = 4 then 1 else 0 end as Apr_2000,
    case when src.data_year = 2000 and src.month = 5 then 1 else 0 end as May_2000,
    case when src.data_year = 2000 and src.month = 6 then 1 else 0 end as Jun_2000,
    case when src.data_year = 2000 and src.month = 7 then 1 else 0 end as Jul_2000,
    case when src.data_year = 2000 and src.month = 8 then 1 else 0 end as Aug_2000,
    case when src.data_year = 2000 and src.month = 9 then 1 else 0 end as Sep_2000,
    case when src.data_year = 2000 and src.month = 10 then 1 else 0 end as Oct_2000,
    case when src.data_year = 2000 and src.month = 11 then 1 else 0 end as Nov_2000,
    case when src.data_year = 2000 and src.month = 12 then 1 else 0 end as Dec_2000,
    case when src.data_year = 2001 and src.month = 1 then 1 else 0 end as Jan_2001,
    case when src.data_year = 2001 and src.month = 2 then 1 else 0 end as Feb_2001,
    case when src.data_year = 2001 and src.month = 3 then 1 else 0 end as Mar_2001,
    case when src.data_year = 2001 and src.month = 4 then 1 else 0 end as Apr_2001,
    case when src.data_year = 2001 and src.month = 5 then 1 else 0 end as May_2001,
    case when src.data_year = 2001 and src.month = 6 then 1 else 0 end as Jun_2001,
    case when src.data_year = 2001 and src.month = 7 then 1 else 0 end as Jul_2001,
    case when src.data_year = 2001 and src.month = 8 then 1 else 0 end as Aug_2001,
    case when src.data_year = 2001 and src.month = 9 then 1 else 0 end as Sep_2001,
    case when src.data_year = 2001 and src.month = 10 then 1 else 0 end as Oct_2001,
    case when src.data_year = 2001 and src.month = 11 then 1 else 0 end as Nov_2001,
    case when src.data_year = 2001 and src.month = 12 then 1 else 0 end as Dec_2001,
    case when src.data_year = 2002 and src.month = 1 then 1 else 0 end as Jan_2002,
    case when src.data_year = 2002 and src.month = 2 then 1 else 0 end as Feb_2002,
    case when src.data_year = 2002 and src.month = 3 then 1 else 0 end as Mar_2002,
    case when src.data_year = 2002 and src.month = 4 then 1 else 0 end as Apr_2002,
    case when src.data_year = 2002 and src.month = 5 then 1 else 0 end as May_2002,
    case when src.data_year = 2002 and src.month = 6 then 1 else 0 end as Jun_2002,
    case when src.data_year = 2002 and src.month = 7 then 1 else 0 end as Jul_2002,
    case when src.data_year = 2002 and src.month = 8 then 1 else 0 end as Aug_2002,
    case when src.data_year = 2002 and src.month = 9 then 1 else 0 end as Sep_2002,
    case when src.data_year = 2002 and src.month = 10 then 1 else 0 end as Oct_2002,
    case when src.data_year = 2002 and src.month = 11 then 1 else 0 end as Nov_2002,
    case when src.data_year = 2002 and src.month = 12 then 1 else 0 end as Dec_2002,
    case when src.data_year = 2003 and src.month = 1 then 1 else 0 end as Jan_2003,
    case when src.data_year = 2003 and src.month = 2 then 1 else 0 end as Feb_2003,
    case when src.data_year = 2003 and src.month = 3 then 1 else 0 end as Mar_2003,
    case when src.data_year = 2003 and src.month = 4 then 1 else 0 end as Apr_2003,
    case when src.data_year = 2003 and src.month = 5 then 1 else 0 end as May_2003,
    case when src.data_year = 2003 and src.month = 6 then 1 else 0 end as Jun_2003,
    case when src.data_year = 2003 and src.month = 7 then 1 else 0 end as Jul_2003,
    case when src.data_year = 2003 and src.month = 8 then 1 else 0 end as Aug_2003,
    case when src.data_year = 2003 and src.month = 9 then 1 else 0 end as Sep_2003,
    case when src.data_year = 2003 and src.month = 10 then 1 else 0 end as Oct_2003,
    case when src.data_year = 2003 and src.month = 11 then 1 else 0 end as Nov_2003,
    case when src.data_year = 2003 and src.month = 12 then 1 else 0 end as Dec_2003,
    case when src.data_year = 2004 and src.month = 1 then 1 else 0 end as Jan_2004,
    case when src.data_year = 2004 and src.month = 2 then 1 else 0 end as Feb_2004,
    case when src.data_year = 2004 and src.month = 3 then 1 else 0 end as Mar_2004,
    case when src.data_year = 2004 and src.month = 4 then 1 else 0 end as Apr_2004,
    case when src.data_year = 2004 and src.month = 5 then 1 else 0 end as May_2004,
    case when src.data_year = 2004 and src.month = 6 then 1 else 0 end as Jun_2004,
    case when src.data_year = 2004 and src.month = 7 then 1 else 0 end as Jul_2004,
    case when src.data_year = 2004 and src.month = 8 then 1 else 0 end as Aug_2004,
    case when src.data_year = 2004 and src.month = 9 then 1 else 0 end as Sep_2004,
    case when src.data_year = 2004 and src.month = 10 then 1 else 0 end as Oct_2004,
    case when src.data_year = 2004 and src.month = 11 then 1 else 0 end as Nov_2004,
    case when src.data_year = 2004 and src.month = 12 then 1 else 0 end as Dec_2004,
    case when src.data_year = 2005 and src.month = 1 then 1 else 0 end as Jan_2005,
    case when src.data_year = 2005 and src.month = 2 then 1 else 0 end as Feb_2005,
    case when src.data_year = 2005 and src.month = 3 then 1 else 0 end as Mar_2005,
    case when src.data_year = 2005 and src.month = 4 then 1 else 0 end as Apr_2005,
    case when src.data_year = 2005 and src.month = 5 then 1 else 0 end as May_2005,
    case when src.data_year = 2005 and src.month = 6 then 1 else 0 end as Jun_2005,
    case when src.data_year = 2005 and src.month = 7 then 1 else 0 end as Jul_2005,
    case when src.data_year = 2005 and src.month = 8 then 1 else 0 end as Aug_2005,
    case when src.data_year = 2005 and src.month = 9 then 1 else 0 end as Sep_2005,
    case when src.data_year = 2005 and src.month = 10 then 1 else 0 end as Oct_2005,
    case when src.data_year = 2005 and src.month = 11 then 1 else 0 end as Nov_2005,
    case when src.data_year = 2005 and src.month = 12 then 1 else 0 end as Dec_2005,
    case when src.data_year = 2006 and src.month = 1 then 1 else 0 end as Jan_2006,
    case when src.data_year = 2006 and src.month = 2 then 1 else 0 end as Feb_2006,
    case when src.data_year = 2006 and src.month = 3 then 1 else 0 end as Mar_2006,
    case when src.data_year = 2006 and src.month = 4 then 1 else 0 end as Apr_2006,
    case when src.data_year = 2006 and src.month = 5 then 1 else 0 end as May_2006,
    case when src.data_year = 2006 and src.month = 6 then 1 else 0 end as Jun_2006,
    case when src.data_year = 2006 and src.month = 7 then 1 else 0 end as Jul_2006,
    case when src.data_year = 2006 and src.month = 8 then 1 else 0 end as Aug_2006,
    case when src.data_year = 2006 and src.month = 9 then 1 else 0 end as Sep_2006,
    case when src.data_year = 2006 and src.month = 10 then 1 else 0 end as Oct_2006,
    case when src.data_year = 2006 and src.month = 11 then 1 else 0 end as Nov_2006,
    case when src.data_year = 2006 and src.month = 12 then 1 else 0 end as Dec_2006,
    case when src.data_year = 2007 and src.month = 1 then 1 else 0 end as Jan_2007,
    case when src.data_year = 2007 and src.month = 2 then 1 else 0 end as Feb_2007,
    case when src.data_year = 2007 and src.month = 3 then 1 else 0 end as Mar_2007,
    case when src.data_year = 2007 and src.month = 4 then 1 else 0 end as Apr_2007,
    case when src.data_year = 2007 and src.month = 5 then 1 else 0 end as May_2007,
    case when src.data_year = 2007 and src.month = 6 then 1 else 0 end as Jun_2007,
    case when src.data_year = 2007 and src.month = 7 then 1 else 0 end as Jul_2007,
    case when src.data_year = 2007 and src.month = 8 then 1 else 0 end as Aug_2007,
    case when src.data_year = 2007 and src.month = 9 then 1 else 0 end as Sep_2007,
    case when src.data_year = 2007 and src.month = 10 then 1 else 0 end as Oct_2007,
    case when src.data_year = 2007 and src.month = 11 then 1 else 0 end as Nov_2007,
    case when src.data_year = 2007 and src.month = 12 then 1 else 0 end as Dec_2007,
    case when src.data_year = 2008 and src.month = 1 then 1 else 0 end as Jan_2008,
    case when src.data_year = 2008 and src.month = 2 then 1 else 0 end as Feb_2008,
    case when src.data_year = 2008 and src.month = 3 then 1 else 0 end as Mar_2008,
    case when src.data_year = 2008 and src.month = 4 then 1 else 0 end as Apr_2008,
    case when src.data_year = 2008 and src.month = 5 then 1 else 0 end as May_2008,
    case when src.data_year = 2008 and src.month = 6 then 1 else 0 end as Jun_2008,
    case when src.data_year = 2008 and src.month = 7 then 1 else 0 end as Jul_2008,
    case when src.data_year = 2008 and src.month = 8 then 1 else 0 end as Aug_2008,
    case when src.data_year = 2008 and src.month = 9 then 1 else 0 end as Sep_2008,
    case when src.data_year = 2008 and src.month = 10 then 1 else 0 end as Oct_2008,
    case when src.data_year = 2008 and src.month = 11 then 1 else 0 end as Nov_2008,
    case when src.data_year = 2008 and src.month = 12 then 1 else 0 end as Dec_2008,
    case when src.data_year = 2009 and src.month = 1 then 1 else 0 end as Jan_2009,
    case when src.data_year = 2009 and src.month = 2 then 1 else 0 end as Feb_2009,
    case when src.data_year = 2009 and src.month = 3 then 1 else 0 end as Mar_2009,
    case when src.data_year = 2009 and src.month = 4 then 1 else 0 end as Apr_2009,
    case when src.data_year = 2009 and src.month = 5 then 1 else 0 end as May_2009,
    case when src.data_year = 2009 and src.month = 6 then 1 else 0 end as Jun_2009,
    case when src.data_year = 2009 and src.month = 7 then 1 else 0 end as Jul_2009,
    case when src.data_year = 2009 and src.month = 8 then 1 else 0 end as Aug_2009,
    case when src.data_year = 2009 and src.month = 9 then 1 else 0 end as Sep_2009,
    case when src.data_year = 2009 and src.month = 10 then 1 else 0 end as Oct_2009,
    case when src.data_year = 2009 and src.month = 11 then 1 else 0 end as Nov_2009,
    case when src.data_year = 2009 and src.month = 12 then 1 else 0 end as Dec_2009,
    case when src.data_year = 2010 and src.month = 1 then 1 else 0 end as Jan_2010,
    case when src.data_year = 2010 and src.month = 2 then 1 else 0 end as Feb_2010,
    case when src.data_year = 2010 and src.month = 3 then 1 else 0 end as Mar_2010,
    case when src.data_year = 2010 and src.month = 4 then 1 else 0 end as Apr_2010,
    case when src.data_year = 2010 and src.month = 5 then 1 else 0 end as May_2010,
    case when src.data_year = 2010 and src.month = 6 then 1 else 0 end as Jun_2010,
    case when src.data_year = 2010 and src.month = 7 then 1 else 0 end as Jul_2010,
    case when src.data_year = 2010 and src.month = 8 then 1 else 0 end as Aug_2010,
    case when src.data_year = 2010 and src.month = 9 then 1 else 0 end as Sep_2010,
    case when src.data_year = 2010 and src.month = 10 then 1 else 0 end as Oct_2010,
    case when src.data_year = 2010 and src.month = 11 then 1 else 0 end as Nov_2010,
    case when src.data_year = 2010 and src.month = 12 then 1 else 0 end as Dec_2010,
    case when src.data_year = 2011 and src.month = 1 then 1 else 0 end as Jan_2011,
    case when src.data_year = 2011 and src.month = 2 then 1 else 0 end as Feb_2011,
    case when src.data_year = 2011 and src.month = 3 then 1 else 0 end as Mar_2011,
    case when src.data_year = 2011 and src.month = 4 then 1 else 0 end as Apr_2011,
    case when src.data_year = 2011 and src.month = 5 then 1 else 0 end as May_2011,
    case when src.data_year = 2011 and src.month = 6 then 1 else 0 end as Jun_2011,
    case when src.data_year = 2011 and src.month = 7 then 1 else 0 end as Jul_2011,
    case when src.data_year = 2011 and src.month = 8 then 1 else 0 end as Aug_2011,
    case when src.data_year = 2011 and src.month = 9 then 1 else 0 end as Sep_2011,
    case when src.data_year = 2011 and src.month = 10 then 1 else 0 end as Oct_2011,
    case when src.data_year = 2011 and src.month = 11 then 1 else 0 end as Nov_2011,
    case when src.data_year = 2011 and src.month = 12 then 1 else 0 end as Dec_2011
FROM (
SELECT
       t.docket_num,
       t.fips,
       cast(t.data_year as int),
       cast(substring(cast(t.status_date as varchar(10)), 1, 2) as int) as month,
       t.status_date as date,
       t.process
    FROM (
    SELECT
       h.data_year,
       h.docket_num,
       h.process,
       h.status_dat as status_date,
       g.fips
        FROM (staging.eviction_processes_2000_2011_bgclip h
         JOIN geom.blockgroup g ON (st_contains(st_transform(g.geom, 102719), st_transform(h.geom, 102719))))
             ) t) as src"""
set_2012_2019 = """select * FROM housing.summary_ejectments__tract__year;"""
set_2000_2011 = """select 
       h.fips        AS fips,
       sum(h.y_2000) AS y_2000,
       sum(h.y_2001) AS y_2001,
       sum(h.y_2002) AS y_2002,
       sum(h.y_2003) AS y_2003,
       sum(h.y_2004) AS y_2004,
       sum(h.y_2005) AS y_2005,
       sum(h.y_2006) AS y_2006,
       sum(h.y_2007) AS y_2007,
       sum(h.y_2008) AS y_2008,
       sum(h.y_2009) AS y_2009,
       sum(h.y_2010) AS y_2010,
       sum(h.y_2011) AS y_2011
FROM (SELECT k.fips,
             CASE
                 WHEN (k.data_year = 2000) THEN 1
                 ELSE 0
                 END AS y_2000,
             CASE
                 WHEN (k.data_year = 2001) THEN 1
                 ELSE 0
                 END AS y_2001,
             CASE
                 WHEN (k.data_year = 2002) THEN 1
                 ELSE 0
                 END AS y_2002,
             CASE
                 WHEN (k.data_year = 2003) THEN 1
                 ELSE 0
                 END AS y_2003,
             CASE
                 WHEN (k.data_year = 2004) THEN 1
                 ELSE 0
                 END AS y_2004,
             CASE
                 WHEN (k.data_year = 2005) THEN 1
                 ELSE 0
                 END AS y_2005,
             CASE
                 WHEN (k.data_year = 2006) THEN 1
                 ELSE 0
                 END AS y_2006,
             CASE
                 WHEN (k.data_year = 2007) THEN 1
                 ELSE 0
                 END AS y_2007,
             CASE
                 WHEN (k.data_year = 2008) THEN 1
                 ELSE 0
                 END AS y_2008,
             CASE
                 WHEN (k.data_year = 2009) THEN 1
                 ELSE 0
                 END AS y_2009,
             CASE
                 WHEN (k.data_year = 2010) THEN 1
                 ELSE 0
                 END AS y_2010,
             CASE
                 WHEN (k.data_year = 2011) THEN 1
                 ELSE 0
                 END AS y_2011
      FROM (
            SELECT CAST(f.data_year as int),
                   f.process,
                   g.fips
            FROM (staging.eviction_processes_2000_2011_bgclip f
                     JOIN geom.tract g ON (st_contains(st_transform(g.geom, 102719), st_transform(f.geom, 102719))))
          ) k
      WHERE ((k.process)::text = 'Summary Ejectment'::text)) h
GROUP BY h.fips
ORDER BY h.fips"""
seb_2012_2019 = """select * FROM housing.summary_ejectments__blockgroup__year;"""
seb_2000_2011 = """select
       h.fips        AS fips,
       sum(h.y_2000) AS y_2000,
       sum(h.y_2001) AS y_2001,
       sum(h.y_2002) AS y_2002,
       sum(h.y_2003) AS y_2003,
       sum(h.y_2004) AS y_2004,
       sum(h.y_2005) AS y_2005,
       sum(h.y_2006) AS y_2006,
       sum(h.y_2007) AS y_2007,
       sum(h.y_2008) AS y_2008,
       sum(h.y_2009) AS y_2009,
       sum(h.y_2010) AS y_2010,
       sum(h.y_2011) AS y_2011
FROM (SELECT k.fips,
             CASE
                 WHEN (k.data_year = 2000) THEN 1
                 ELSE 0
                 END AS y_2000,
             CASE
                 WHEN (k.data_year = 2001) THEN 1
                 ELSE 0
                 END AS y_2001,
             CASE
                 WHEN (k.data_year = 2002) THEN 1
                 ELSE 0
                 END AS y_2002,
             CASE
                 WHEN (k.data_year = 2003) THEN 1
                 ELSE 0
                 END AS y_2003,
             CASE
                 WHEN (k.data_year = 2004) THEN 1
                 ELSE 0
                 END AS y_2004,
             CASE
                 WHEN (k.data_year = 2005) THEN 1
                 ELSE 0
                 END AS y_2005,
             CASE
                 WHEN (k.data_year = 2006) THEN 1
                 ELSE 0
                 END AS y_2006,
             CASE
                 WHEN (k.data_year = 2007) THEN 1
                 ELSE 0
                 END AS y_2007,
             CASE
                 WHEN (k.data_year = 2008) THEN 1
                 ELSE 0
                 END AS y_2008,
             CASE
                 WHEN (k.data_year = 2009) THEN 1
                 ELSE 0
                 END AS y_2009,
             CASE
                 WHEN (k.data_year = 2010) THEN 1
                 ELSE 0
                 END AS y_2010,
             CASE
                 WHEN (k.data_year = 2011) THEN 1
                 ELSE 0
                 END AS y_2011
      FROM (
            SELECT CAST(f.data_year as int),
                   f.process,
                   g.fips
            FROM (staging.eviction_processes_2000_2011_bgclip f
                     JOIN geom.blockgroup g ON (st_contains(st_transform(g.geom, 102719), st_transform(f.geom, 102719))))
          ) k
      WHERE ((k.process)::text = 'Summary Ejectment'::text)) h
GROUP BY h.fips
ORDER BY h.fips"""
ell_2012_2019 = """select
       h.gid,
       st_x(st_transform(ST_Centroid(h.geom),4326)) as x,
       st_y(st_transform(ST_Centroid(h.geom),4326)) as y,
       h.data_year,
       h.name,
       h.docket_num,
       h.street_address,
       h.status,
       h.involvement,
       h.process,
       h.status_date,
       h.issued_date
From housing.evictions h"""
ell_2000_2011 = """select
       h.id as gid,
       st_x(st_transform(ST_Centroid(h.geom),4326)) as x,
       st_y(st_transform(ST_Centroid(h.geom),4326)) as y,
       h.data_year,
       h.name,
       h.docket_num,
       h.street_add as street_address,
       h.status,
       h.involvemen as involvement,
       h.process,
       h.status_dat as status_date,
       h.issued_dat as issued_date
From staging.eviction_processes_2000_2011_bgclip h"""
