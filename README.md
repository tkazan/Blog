# Blog
A simple blogging app created in Python/Django and styled in Bootstrap.
- List of all posts with pagination and links to details on home page
- Single post detail view
- Creating a new post in nice text editor
- Modifying an existing post
- Deleting posts

<hr>

#### DOCUMENTATION
- <b>MODELS</b><br/>
1. Post model to store single post on blog.<br/>
String method return post's title (first 50 chars) and last update.<br/>
Fields:<br/>
    * title: CharField with limit of 128 chars
    * description: TextField
    * created_at: DateTimeField to store a post creation date
    * updated_at: DateTimeField to store last update of post
    
Records are stored in built-in sqlite3 database.

- <b>FORMS</b><br/>
1. NewPostForm - ModelForm related to Post model for creating a new Post.

- <b>VIEWS</b><br/>
1. <b>index</b><br/>
Display a list of posts from newest with links to post details.<br/>
Use template: index.html<br/>
url(r'^$', index, name='home').

2. <b>show_post</b><br/>
Display details of selected post with id from url.<br/>
Use template: post.html<br/>
url(r'^post/(?P<id>(\d)+)$', show_post, name='post').

3. <b>NewPostView</b><br/>
get method: Display a form (NewPostForm) to create a new post.<br/>
post method: Save a new post to database and redirect to index view.<br/>
Use template: new.html<br/>
url(r'^new$', NewPostView.as_view(), name='new').

4. <b>EditPostView</b><br/>  
get method: Display a form to edit a selected post with id from url.<br/>
post method: Save changes made to selected post to database.<br/>
Use template: edit.html<br/>
url(r'^edit/(?P<id>(\d)+)$', EditPostView.as_view(), name='edit').

5. <b>DeletePostView</b><br/>
get method: Display a form to delete a selected post with id from url.<br/>
post method: Delete a selected post from database.<br/>
Use template: delete.html<br/>
url(r'^delete/(?P<id>(\d)+)$', DeletePostView.as_view(), name='delete').

<hr>

#### REQUIREMENTS - How to start working with that project (on Ubuntu):
1. Check if you have a <b>Python 3.5</b> installed:<br/> 
$ python3 --version | if not: <br/>
$ sudo apt-get update <br/>
$ sudo apt-get install python3
2. Check if you have <b>pip3</b> installed: <br/> 
$ pip3 --version | if not: <br/> 
$ sudo apt-get install -y python3-pip
3. Check if you have <b>virtualenv</b> installed: <br/>
$ virtualenv --version | if not: <br/>
$ pip3 install virtualenv
<br/> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
4. Clone a repository on your computer
5. Create and activate a new virtenv: <br/>
$ virtualenv -p python3 DjangoVirtEnv <br/>
$ source DjangoVirtEnv/bin/activate
6. Install requirements: <br/>
$ pip3 install -r requirements.txt
7. Make migrations: <br/>
$ python manage.py makemigrations <br/>
$ python manage.py migrate
8. Runserver: <br/>
$ python manage.py runserver
9. Use the django app on url: <br/>
<a href="http://localhost:8000/">http://localhost:8000</a>
