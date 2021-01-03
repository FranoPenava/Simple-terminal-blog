import uuid
import datetime
from database import Database


class Post(object):
    # Transforming 16-digit id into 4-digit! 
    # Uuid.uuid().hex will generate a random ID with hexadecimal values. 
    STR_ID = str(uuid.uuid4().hex)[:4]
    
    def __init__(self, blog_id, title, author, content, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id = Post.STR_ID if id is None else id

    # Two simple methods:
    # Saving data into collection "posts"!
    def save_to_mongo(self):
        Database.insert(collection = "posts", data = self.json())
    
    # Deleting data from collection "posts"!
    @staticmethod
    def remove_from_mongo(id):
        Database.remove(collection = "posts", query = {"id": id})
    
    # Json is the type of data. It will be sent into collection "posts"!
    def json(self):
        return {
            "id": self.id,
            "blog_id": self.blog_id,
            "author": self.author,
            "content": self.content,
            "title": self.title,
            "date": self.date
        }
    
    # Finding post with post id.
    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection="posts", query={"id": id})
        
        # Retrieving Post object instead of post_data variable.
        return Post(
        blog_id = post_data["blog_id"],
        title = post_data["title"],
        author = post_data["author"], 
        content = post_data["content"], 
        date = post_data["date"], 
        id = post_data["id"]
        )

        
    # Finding post with blog_id and retrieving all the posts for the same blog_id.
    @staticmethod
    def from_blog(blog_id):
        return [post for post in Database.find(collection ="posts", query={"blog_id": blog_id})]

