### Project description used to generate the systems

The backend project for the virtual library, to be developed in \<language
project\>, using the \<project framework\> framework and Microsoft SQL Server
as a database, it will register and manage books and students.
Student data will consist of personal details and rental history, while
for books will include title, author, ISBN, status etc. Registered students only
You can rent a book as long as it is available. Once the book is rented,
its status in the system is updated to ”Rent”.
The return of each book will be manually confirmed by a librarian or
administrator, who can then update the book's status to "Available", "Reserved", or "Under Maintenance" based on the physical condition of the book and future reservations.
To effectively manage loan periods, loan administrators
system can set default loan durations. This loan period
Standard applies to all books, no exceptions.
Librarians will be registered in the system and can be managed (CRUD)
by administrators. An administrator user has broad system rights, including
including management of all system entities and changing settings
of the system. Librarians have more limited rights, focused primarily on
performing CRUD operations for book and student data.
Admin users will initially be preloaded into the database
with your information, which includes credentials. These credentials and settings
general system parameters will be populated from an external configuration file,
which includes settings such as the default book loan duration.
The system will differentiate between entities - students and books - and system users.
theme - librarians and administrators. The former can be managed but not
have system user rights, while the latter have respective rights
as defined in their roles.
