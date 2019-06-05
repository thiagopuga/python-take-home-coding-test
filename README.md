
Task 1 (documentation):

Write documentation for all tasks undertaken in a markdown file ( README.md ).

	• Discuss the planning of the task(s) that were completed and their final implementations.
	• What were some of the design considerations?
	• Why was this technology stack chosen and implemented?
	• What are the pros/cons of this technology stack?
	• What are some alternatives to the implemented technology stack?
	• What are their strength's and weaknesses?
	• Include a diagram of the overall pipeline that specifies the flow of the data and the architectural components of the stack.
	• Include installation instructions on how to install your code and dependencies.
	• All documentation and code should be checked into a Git compatible repository that is remotely accessible such as GitHub or BitBucket.
	• Documentation should be in Markdown ( .md ) format as a README.md at the root of the Git repository

Ferramentas utilizadas:
	- Python 3.7.3
	- MongoDB

Como executar:
    - Passo 1: instalar requerimentos do arquivo "requirements.txt"
    - Passo 2: executar script "get-store-show-recent-change.py"
    - Passo 3: abrir página HTML "Recent Change Stream.html"

Comandos adicionais (ajuda):
	- Acessar o MongoDB via linha de comando no Windows:
        cd C:\Program Files\MongoDB\Server\4.0\bin
        mongo
	- Criar database:
        use task3
	- Exibir database criado:
        db
	- Inserir registros da variável x no collection recent_change_stream_wikipedia:
        db.recent_change_stream_wikipedia.insert(x);
	- Exibir registro:
        db.recent_change_stream_wikipedia.find().pretty();
        db.recent_change_stream_wikipedia.find({_id: ObjectId("5cf80cf5bc967fb32d810e18")}).pretty();
	- Aggregate by timestamp
        db.recent_change_stream_wikipedia.aggregate([{$group: {_id: "$timestamp", count_changes: {$sum: 1}}}]);

---------------------------------------------------------------------------------------------------------

Task/Script 2 (extract):

Consume the Recent Change stream of the Wikipedia site and /filter the JSON to only show non-bot related edits. (https://stream.wikimedia.org/v2/stream/recentchange)

	• JSON should be formatted and indented to be readable. Script should run until	terminated.
	• (optional) Allow command-line parameter to alter the default filter (non-bot related edits) to an arbitrary filter via regex or DSL.
	• (optional) Allow command-parameter to write out data to a path/file of your choosing.
	• Include a requirements.txt file to make it easy to install your code dependencies.
	
Feito!

---------------------------------------------------------------------------------------------------------

Task/Script 3 (storage):

Store the filtered non-bot edit stream in a database.

	• Database creation should be scripted if it doesn’t exist.
	• Database table(s) should be truncated if DB already exists.
	• Script should run until terminated.
	
Feito!

---------------------------------------------------------------------------------------------------------

Task 4 (visualization):

Visualize the edits per minute on a web page.

	• Using any language or tool build a small web-page.
	• Page should display a graph of edits per second while the extract or storage scripts are running.
	• If possible the web page should refresh automatically every few seconds to show updated edit counts.
	• Feel free to use any framework, tool, or plain HTML you feel comfortable with.

Feito!