from database import Database
from blog import Blog
from post import Post

class Menu(object):
    def __init__(self):
       # Ask a user for author name!
       self.user = input("Enter your author name: ")
       self.user_blog = None

       # Check if they have already got an account!
       if self._user_has_account():
           print(f"Welcome back {self.user}")
        
        # If not, prompt them to create one!
       else:
           self._prompt_user_for_account()
       
       

    def _user_has_account(self):
       # Finding blog with author as query.  
       blog = Database.find_one("blog", {"author": self.user}) 
       
       if blog is not None:
           self.user_blog = Blog.from_mongo(blog["id"])
           return True
       else:
           return False    
    
    # Function for creating a blog. 
    def _prompt_user_for_account(self):
        title = input("Enter title: ")
        description = input("Enter blog description: ")
        
        blog = Blog(self.user, title, description)
        # Saving that blog in our collection "blog"
        blog.save_to_mongo()
    
        self.user_blog = blog        
    
    
    def run_menu(self):
        while True:
            # User read, write, or delete!
            r_w_d = input("Type (Q) to quit! Do you want to read (R), write (W) or delete (D) blogs? ")
            # If user type Q blog will quit.
            if r_w_d == "Q":
                print("You quit this app! ")
                break
            else:
                while r_w_d != "Q":
                    # if read:
                    if r_w_d == "R":
                       # list blogs in database!
                       self._list_blogs()
                       # display posts!
                       self._view_blog()
                       break
                    
                    # if write: 
                    elif r_w_d == "W":
                        # Prompt to write a post!
                        self.user_blog.new_post()
                        break
                    
                    # if delete:    
                    elif r_w_d == "D":
                        # Deleting blog or post. 
                        post_blog = input("Do you want to delete post (P) or blog (B)? ")
                        # If user type Q blog will quit.
                        while post_blog != "Q":
                            # if user type B!
                            if post_blog == "B":
                                # Delete blog
                                self._delete_blog()
                                break
                            
                            # if user type P!
                            elif post_blog == "P":
                                # Delete specific post!
                                self._delete_post()
                                break
                            
                        break
                    
                    
    def _delete_blog(self):
        # Show all blogs. 
        self._list_blogs()
        blog_id = input("Enter the id of the blog you would like to delete? ")
        # Deleting the blog with provided blog_id. 
        Blog.remove_from_mongo(blog_id = blog_id)
    
    def _delete_post(self):
        # Show all blogs.
        self._list_blogs()
        # Show posts for specific blog. 
        self._view_blog()

        Del_Id = input("Enter the ID of the post you would like to delete? ")
        Post.remove_from_mongo(Del_Id)
    

    # Function for showing all the blogs. 
    def _list_blogs(self):
        blogs = Database.find(collection = "blog", query = {})
        
        for blog in blogs:
            print(f"ID: {blog['id']}, Title: {blog['title']}, Author: {blog['author']}")
    
    # Function for showing all the posts for specific blog.
    def _view_blog(self):
        blog_to_see = input("Enter the ID of the blog: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        
        for post in posts:
            print(f"Date: {post['date']}, Title: {post['title']},\n Content: {post['content']}, Id: {post['id']} ")

    
        
        
        
