This is a personal job baord scraping project.
Currently it is scraping Builtin Indeed and Ycomb, more may be added later. 
I understand that job boards don't generally like to be scraped as their value is the job listing themselves, 
however this is meant to be more of an academic project than anything and will only ever be running locally.

This project operates by using the react page to call scraping scripts defined in python. And then use the
react page to view the returned opportunities. While this could just be settup to run on a timer, its intended
use is to be booted up ran and then shuttered. I didn't think it necissary to scrape these sites multiple times 
a day, also that would require duplicate handling. Arguably there should already be duplicate handling, however each
site stores its opportunities differently and even when using a key with the company name and job title there are opportunities
that share those fields but are completely different offerings. Also for the intended use duplicate handling was too much scope.
The design decsion to call the scripts from react does lead to the interesting conundrum that a node server is not techincally 
necissary here and the scrape could get all the data using flask. I had however already set up the node server and a more fully 
flushed out tool would probably make proper use of that server. For now it servers to seperate resposibilities well enough.
Last, the search is very rudimentary. It is not at all optimized and runs incredibly slowly. It also only runs against the job titles
but for now its enough. Providing proper filters when the information acquired from each search is so varried would be a real pain 
requiring individual mapping from each site to a shared object which I also didnt want to do, and wasn't requried for the inteded purpose.

To build project clone repo and run docker-compose up from inside the directory.
Create an .env file with layout:
Y_COMB_PASSWORD=
Y_COMB_EMAIL=

Y_COMB_LOGIN_LINK=
Y_COMB_LINKS=
BUILTIN_LINK=
INDEED_LINK=

CONNECTION_STRING =

DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=

FLASK_HOST=
FLASK_PORT=

Navigate to the react page at http://localhost:3000.
Use the "Scrape" button to initialize the web scraping.
Eventually opportunities will be returned and the page updated.
