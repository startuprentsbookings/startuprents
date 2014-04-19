from rentsapp.models import Post, Comment

#Create new post
post = Post.objects.create(title='US Constitution',
                           body='We the People of the United States, in Order to form a more perfect Union, establish '
                                'Justice, insure domestic Tranquility, provide for the common defence, promote the '
                                'general. Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, '
                                'do ordain and establish this Constitution for the United States of America.',
                           permalink='TqoHkbHyUgLyCKWgPLqm',
                           author='Jorge Valderrama',
                           tags=['mongodb', 'django'])

post.save()
print(post.tags)

#Get new post and add commentaries
comment = Comment.objects.create(body='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor '
                                      'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis '
                                      'nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '
                                      'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu '
                                      '7 fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt '
                                      'in culpa qui officia deserunt mollit anim id est laborum',
                                 email='joedval@gmail.com',
                                 author="Jorge Valderrama")
comment.save()
print(comment.email)

post.comments = [comment]
post.save()
print(post.comments[0].email)

