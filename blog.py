import uuid
import datetime
from post import Post
from database import Database

class Blog(object):
    # Transforming 16-digit id into 4-digit!
    # Uuid.uuid().hex will generate a random ID with hexadecimal values.
    STR_ID = str(uuid.uuid4().hex)[:4]
    
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = Blog.STR_ID if id is None else id
        
    # Creating new post!
    def new_post(self):
        # Few inputs needed for making a post.
        title = input("Enter title: ")
        content = input("Enter content: ")
        date = input("Enter date (in format DDMMYYYY): ")
        # Possible date inputs are input in format DDMMYYYY or nothing.
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        
        # Creating a Post object with all the peaces of information needed.
        post = Post(
        blog_id=self.id,
        title = title, 
        content = content, 
        author = self.author, 
        date = date
        )
        post.save_to_mongo()
    
    # Getting posts with blog_id.
    def get_posts(self):
        return Post.from_blog(self.id)
    
    # Saving and removing some data from collection "blog".
    def save_to_mongo(self):
        Database.insert(collection="blog", data=self.json())
        
    @staticmethod
    def remove_from_mongo(blog_id):
        Database.remove(collection = "blog", query = {"id": blog_id})
    
    # Data that will be saved into collection "blog".
    def json(self):
        return {
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "id": self.id,
        }
    
    # Finding blog with provided id.
    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection = "blog", query = {"id": id})

        # Retrieving data as Blog object. 
        return cls(
        author=blog_data["author"], 
        title = blog_data["title"], 
        description = blog_data["description"], 
        id = blog_data["id"]
        )


        
