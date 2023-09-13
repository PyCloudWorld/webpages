# What are Azure Storage Account
This is storage on the cloud via the use of different services<hr/>
<b> Azure Blob Storage:</b></br>
  * this is object storage service
  * this is great for storing unstructured data
  * can grow automatically based on demand
  * good for storing backups
  * good for storing images, videos, audio files
    * IMPORTANT: the vm and storage should be separate, if the vm crashes or fails. data is still available.
      * ![image](images/what_are_storage_accounts/1.png)
<hr/>

<b> Azure File Shares </b></br>
  * manage storage for individual users.
    * ![image](images/what_are_storage_accounts/2.png)

<hr/>

<b> Azure  Table Storage </b></br>
* great when you want to store non relational structured data.
* this is when your data is of schemaless design
  
  * example : storing information about files saved in blob

    * ![image](images/what_are_storage_accounts/3.png)

<hr/>

<b> Azure Queue Storage </b>
  * messaging based service between different applications or different components of the application. you can use this application
      * ![image](images/what_are_storage_accounts/4.png)

<hr/>