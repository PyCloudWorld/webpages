#  Log Analytics Queries
Below is a reference for the queries for Log Analytics

0. This can be used for search for a keyword in the event table

Event
* ![image_1](images/7_log_analystic_queries/0.png)

1. This can be used for search for a keyword in the event table

Event | search "demovm"
* ![image_1](images/7_log_analystic_queries/1.png)
* 
1. This can be used for search for a keyword in the event table

Event | search "demovm"
* ![image_1](images/7_log_analystic_queries/1.png)


2. This can used to pick up 5 events taken in no specific order

Event | top 10 by TimeGenerated
* ![image_1](images/7_log_analystic_queries/2.png)


3. This is used to filter based on a particular property of an event

Event | where EventLevel == 4
* ![image_1](images/7_log_analystic_queries/3.png)


4. This can be used to check for the events generated in the previous 5 minutes

Event | where TimeGenerated > ago(5m)
* ![image_1](images/7_log_analystic_queries/4.png)


5. This can be used to project certain properties

Event | where TimeGenerated > ago(5m) | project EventLog, Computer
* ![image_1](images/7_log_analystic_queries/5.png)


6. Here you can summarize the events

Event |  where TimeGenerated > ago(1d) | summarize count() by Computer,Source
* ![image_1](images/7_log_analystic_queries/6.png)


7. Here you can render a bar chart based on the data

Event |  where TimeGenerated > ago(1d) | summarize count() by Computer,Source | render barchart
* ![image_1](images/7_log_analystic_queries/7.png)
8Here you can render a pie chart based on the data

Event |  where TimeGenerated > ago(1d) | summarize count() by Source | render piechart 
* ![image_1](images/7_log_analystic_queries/8.png)