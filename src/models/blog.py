from src.models.post import Post
import datetime
import uuid
from src.common.database import Database


class Blog(object):
    def __init__(self,author,title,description,author_id ,_id = None):
       self.author = author
       self.title  = title
       self.description = description
       self.author_id = author_id
       self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self,title,content,date=datetime.datetime.utcnow()):
        post = Post(blog_id=self._id,title=title,content = content,created_date= datetime.datetime.strptime(date,"%d%m%Y"),author=self.author)
        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert("blogs", data=self.json())

    def json(self):
        return {
            '_id': self._id,
            "author_id": self.author_id,
            'author': self.author,
            'title': self.title,
            "description" : self.description
     }

    @classmethod
    def from_mongo(cls,id):
        blog_data = Database.find_one(collection="blogs",query={"_id":id})
        return cls(**blog_data)

    @classmethod
    def find_by_author(cls,author):
        blogs = Database.find(collection="blogs",query={"author":author})
        return [cls(**blog) for blog in blogs]
