import os

from flask_script import Manager, Server
from flask_script.commands import ShowUrls
from flask_migrate import Migrate, MigrateCommand
from Blog.models.blogs import db, User, Post, Tag
from Blog import create_app

#默认的环境变量
env = os.environ.get('BLOG_ENV', 'Dev')
print(env.capitalize())
app = create_app("Blog.config.%sConfig" % env.capitalize())


migrate = Migrate(db=db, app=app)
manage = Manager(app)
manage.add_command('server', Server())
manage.add_command('show-urls', ShowUrls())
manage.add_command('db', MigrateCommand)


@manage.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Tag=Tag)


if __name__ == '__main__':
    manage.run()
