Tools used:
	- Python 3.7.3
		- pip 19.1.1
		- sseclient 0.0.24
		- pymongo 3.8.0
		- matplotlib 3.1.0
	- MongoDB Compass Community 4.0.10

How to run:
     	- Step 1: Install requirements from the "requirements.txt"
     	- Step 2: Run script "get-store-show-recent-change.py"
     	- Step 3: Open HTML page "Recent Change Stream.html"

Additional commands (help):
- Access MongoDB via command line in Windows:
         cd C: \ Program Files \ MongoDB \ Server \ 4.0 \ bin
         Mongo
- Create database:
         use task3
- View created database:
         db
- Insert records of variable x in collection recent_change_stream_wikipedia:
         db.recent_change_stream_wikipedia.insert (x);
- View Record:
         db.recent_change_stream_wikipedia.find (). pretty ();
         db.recent_change_stream_wikipedia.find ({_ id: ObjectId ("5cf80cf5bc967fb32d810e18")}). pretty ();
- Aggregate by timestamp
         db.recent_change_stream_wikipedia.aggregate ([{$ group: {_id: "$ timestamp", count_changes: {$ sum: 1}}}]);
