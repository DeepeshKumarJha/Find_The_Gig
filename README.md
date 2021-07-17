# FindTheGig

## Sites From which we are fetching the data
 * upwork
 * freelancer
 * peopleperhour
 
### Freelancer
We can't access this site using scrapy because this site uses javascript to
load the content, So if the javascript is disabled page won't load.
So, For this we only have two options access data using the api or use 
selenium to for that.

### PeoplePerHour
I can't able to find any official api for this site, So I'm going to use
Scrapy to scrape the gigs from this site. Because, When I checked after 
disabling javascript this site still works fine but to search for particualar 
jobs, We should use url like :
        https://peopleperhour.com/freelance-<topic>-<name>-jobs