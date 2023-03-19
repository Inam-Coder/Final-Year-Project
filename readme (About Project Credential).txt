Following are the weather API credentials:
    username: 2495895@dundee.ac.uk
    Password: S&Tst/A^


Azure services and credentials:

    azure_login: 2495895@dundee.ac.uk
    password: Skying@123456789

    azure postgres DB:
        dbname=postgres
        user=inam_admin
        host=postgres22.postgres.database.azure.com
        port=5432
        password=postgres_24_FEB_23@


    To connect to the VM, user required a username, host, and pem file.
        Username: azureuser
        host: 20.127.24.123

        ssh azureuser@20.127.24.123 -i D:\Final Project\etl-weather-api\root-machine_key.pem
        
    To Connect with Power BI From Azure postgres DB we need:
        dbname=postgres
        user=inam_admin
        host=postgres22.postgres.database.azure.com
        port=5432
        password=postgres_24_FEB_23@

        



The Following Environment software should be installed in the machine that hosts the code. 
Environment software:
1) Python 3.6+
2) git


Python project specific libraries: 
1) pip install git+https://github.com/weatherapicom/python     // version 1.0.0
2) pip install psycopg2==2.9.5




