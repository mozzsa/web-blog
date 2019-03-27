from src.common.database import Database
import uuid
import datetime
import pymongo


class Post(object):
    def __init__(self,blog_id,title,content,author,create_date = datetime.datetime.utcnow(),_id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self._id = uuid.uuid4().hex if _id is None else _id
        self.create_date = create_date


    def save_to_mongo(self):
        Database.insert("posts",data = self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'create_date': self.create_date
         }

    @classmethod
    def from_mongo(cls,id):
        post_data =Database.find_one(collection = "posts",query = {"_id" :id})
        #return cls(_id =post_data["_id"],blog_id =post_data["blog_id"],
        #           author = post_data["author"],content=post_data["content"],
        #           title = post_data["title"],
        #           create_date = post_data["create_date"])

        return cls(**post_data)

    @classmethod
    def from_blog(cls,id):
        for i in Database.find(collection = "posts",query ={"blog_id" :id}):
            print(i)
        print(Database.find(collection = "posts",query = {"blog_id" :id}))
        return  [cls(**post) for post in Database.find(collection = "posts",query = {"blog_id" :id})]