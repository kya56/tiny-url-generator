# tiny url generator with FastAPI

This web application is an educational project which shortens url with FastAPI.  
* rest api which shortens url
* rest api which get long url by short url
* persistent with postgresql
* (TODO) unit testing & load testing
* (TODO) caching for read


### Getting Started
* Make sure you have python3 installed
* go to project root and run `bash run.sh`
* Check swagger api specification in `http://127.0.0.1:8000/docs#/`
![Screenshot 2024-06-12 at 10.47.59.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fz8%2Fmnqyq15j5ds95819y8hl6r1m0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_EYFbEf%2FScreenshot%202024-06-12%20at%2010.47.59.png)

### How it works
* use Base 62 conversion (62 characters, 0-9,a-z,A-Z)
* take longUrl as an input and first checks in DB if it already exists
* if it exists, it returns shortUrl
* if not, generate unique ID based on showflake ID
* convert ID to shortUrl and persist in DB