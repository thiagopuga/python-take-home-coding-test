# Take Home Coding Test
The project consists of a data pipeline to monitor, store, and view the flow of recent events change from Wikipedia.
The approach chosen was a Python script, along with the MongoDB database and an HTML page.

## Documentation
Python programming language is present and well known in the market with a simple syntax and easy to understand.
Python is also widely used for Big Data. In addition to dealing with many data difficulties and supporting parallel computing.

MongoDB has an easy and very efficient query syntax, without the need to take many turns to handle documents in general.
MongoDB is also scalable. Thanks to sharding that can distribute data on multiple machines.

The visualization was developed in HTML with an image of a graphic because it was something very small and fast to be done.

It is also worth saying that this architectural decision had a strong appeal for the easy installation of the components and the reuse of the tools already installed.

Here is the API I've be using:

| API                                                                       | Description   |
| ------------------------------------------------------------------------- | ------------- |
| [EventStreams](https://stream.wikimedia.org/v2/stream/recentchange)                | Wikipedia Recent Events |

## How to Run
1. Install all components of the file `requirements.txt`
2. Run the script `get-store-show-recent-change.py`
3. Open the HTML page `Recent Change Stream.html`

## Completed Tasks
- [x] Task 1 (documentation)
- [x] Task/Script 2 (extract)
- [x] Task/Script 3 (storage)
- [x] Task 4 (visualization)
- [ ] Task 5 (query)
- [ ] Task 6 (devops)

## Tools Used
1. Python 3.7.3
2. pip 19.1.1
3. sseclient 0.0.24
4. MongoDB Compass Community 4.0.10
5. pymongo 3.8.0
6. matplotlib 3.1.0

Thank you!
