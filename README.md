# Voting hub

A web app to host rooms, where users can send in questions. Users can then answer the questions by clicking the yes or no buttons. A user can only vote once on a question. An admin will be able to moderate the room and remove questions he deems unfit.
### Link to the website

[Voting hub](https://tsoha-votinghub.herokuapp.com/)

### Using the website

Create a user or log in with an existing account by clicking the respective buttons in the top right corner. After doing so you can create a room by clicking "Create room" and giving it a unique name. You will be redirected to the room you created. After creating a room, people can find it from the front page (accessible by clicking the "Voting hub" header in the top left corner). Anyone can send in questions to your room and vote "yes" or "no" on them. The tally of the votes can be seen next to the questions. As the creator of a room, you have admin rights in that specific room, allowing you to remove inappropriate questions as you see fit. As an admin, you can also remove the entire room by clicking the "Remove the room button".

### Configuring the program

Download the project. Using the terminal navigate to the folder where the file "requirements.txt" is. Run the command *pip install -r requirements.txt* without the quotation marks to install the required packages. I recommend you use a virtual environment. If you want to upload the program to Heroku run *echo "web: gunicorn --preload --workers 1 application:app" > Procfile* first. Then upload it to Heroku.

### Developing the software further

Right now, once you have cast your vote, you can no longer change it. Ideally, you could change your vote. This could be achieved quite simply with an attribute in the authquestion bridging table. 

### User stories

[User stories](https://github.com/eerorant/voting-hub/blob/master/documentation/user_stories.md)

### Database diagram

![Database diagram](https://raw.githubusercontent.com/eerorant/voting-hub/master/documentation/diagram.png)

