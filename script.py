from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import *

post1 = Post(
    title="The Future of Web Development",
    content="""
Web development is constantly evolving, with new technologies and frameworks emerging all the time. In this post, we'll explore some of the most exciting trends and predictions for the future of web development.

1. **Progressive Web Apps (PWAs)**: PWAs are web applications that offer a native app-like experience. They are fast, reliable, and can work offline, making them a popular choice for modern web development.

2. **Artificial Intelligence (AI) and Machine Learning (ML)**: AI and ML are transforming the way we build and interact with websites. From chatbots to personalized content, these technologies are enhancing user experiences in unprecedented ways.

3. **Serverless Architecture**: Serverless computing allows developers to build and run applications without managing servers. This approach can reduce costs and improve scalability, making it an attractive option for many projects.

4. **WebAssembly (Wasm)**: WebAssembly is a binary instruction format that allows code written in multiple languages to run on the web at near-native speed. This opens up new possibilities for performance-intensive applications.

5. **Enhanced Security**: With the increasing number of cyber threats, security is a top priority for web developers. Implementing robust security measures and staying updated with the latest best practices is crucial.

Stay tuned as we dive deeper into each of these trends in future posts!
""",
    created_at=timezone.now(),
    updated_at=timezone.now(),
    publish=timezone.now(),
    author=User.objects.get(username="admin"),
    slug="the-future-of-web-development",
    status=Post.Status.PUBLISHED,
)
post1.save()


post2 = Post(
    title="A Beginner's Guide to Django",
    content="""
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. In this guide, we'll cover the basics of getting started with Django.

1. **Installation**: To install Django, you can use pip, the Python package installer. Simply run `pip install django` in your terminal.

2. **Creating a Project**: Once Django is installed, you can create a new project by running `django-admin startproject myproject`. This will generate the necessary files and directories for your project.

3. **Creating an App**: In Django, a project can contain multiple apps. To create a new app, navigate to your project directory and run `python manage.py startapp myapp`.

4. **Models and Migrations**: Django uses models to define the structure of your database. After defining your models, you can create and apply migrations to update your database schema.

5. **Views and Templates**: Views handle the logic for your application, while templates define the HTML structure. Together, they allow you to create dynamic web pages.

6. **Admin Interface**: Django comes with a built-in admin interface that allows you to manage your application's data. You can customize the admin interface to suit your needs.

By following these steps, you'll be well on your way to building powerful web applications with Django. Happy coding!
""",
    created_at=timezone.now(),
    updated_at=timezone.now(),
    publish=timezone.now(),
    author=User.objects.get(username="admin"),
    slug="beginners-guide-to-django",
    status=Post.Status.PUBLISHED,
)
post2.save()


post3 = Post(
    title="Understanding REST APIs",
    content="""
REST (Representational State Transfer) is an architectural style for designing networked applications. In this post, we'll explore the key concepts and benefits of REST APIs.

1. **Statelessness**: REST APIs are stateless, meaning each request from a client to a server must contain all the information needed to understand and process the request. This simplifies the server design and improves scalability.

2. **Resource-Based**: In REST, resources are identified by URLs. Each resource can be manipulated using standard HTTP methods such as GET, POST, PUT, and DELETE.

3. **Representation**: Resources can have multiple representations, such as JSON, XML, or HTML. Clients can request a specific representation using the `Accept` header.

4. **Uniform Interface**: REST APIs follow a uniform interface, which simplifies the interaction between clients and servers. This includes using standard HTTP methods and status codes.

5. **HATEOAS**: Hypermedia as the Engine of Application State (HATEOAS) is a constraint of REST that allows clients to dynamically navigate resources through hyperlinks.

By understanding these principles, you can design and implement robust REST APIs that are easy to use and maintain. Stay tuned for more in-depth tutorials on building REST APIs with Django!
""",
    created_at=timezone.now(),
    updated_at=timezone.now(),
    publish=timezone.now(),
    author=User.objects.get(username="admin"),
    slug="understanding-rest-apis",
    status=Post.Status.PUBLISHED,
)
post3.save()
