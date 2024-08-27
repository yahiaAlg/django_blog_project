#!/bin/bash

# Create directories
mkdir -p templates/partials

# Create blog/base.html
cat <<EOL > templates/blog/base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Blog{% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    {% include "blog/partials/_header.html" %}
    <main>
        {% block content %}{% endblock %}
    </main>
    {% include "blog/partials/_footer.html" %}
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>
</body>
</html>
EOL

# Create _header.html
cat <<EOL > templates/partials/_header.html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'blog:post_list' %}">My Blog</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'blog:post_list' %}">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'blog:about' %}">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'blog:contact' %}">Contact</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
EOL

# Create _footer.html
cat <<EOL > templates/partials/_footer.html
<footer class="bg-light text-center text-lg-start mt-5">
    <div class="container p-4">
        <p class="text-center">© 2024 My Blog. All rights reserved.</p>
        <p class="text-center">
            <a href="{% url 'blog:about' %}">About</a> | 
            <a href="{% url 'blog:contact' %}">Contact</a>
        </p>
    </div>
</footer>
EOL

# Create post_list.html
cat <<EOL > templates/post_list.html
{% extends "blog/base.html" %}

{% block content %}
<div class="container mt-5">
    <h1 class="mb-4">Posts</h1>
    <div class="row">
        {% for post in posts %}
        <div class="col-md-4 mb-4">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">{{ post.title }}</h5>
                    <p class="card-text">{{ post.content|truncatewords:30 }}</p>
                    <a href="{{ post.get_absolute_url }}" class="btn btn-primary">Read More</a>
                </div>
                <div class="card-footer text-muted">
                    Published on {{ post.publish|date:"F j, Y" }} by {{ post.author }}
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
EOL

# Create post_detail.html
cat <<EOL > templates/post_detail.html
{% extends "blog/base.html" %}

{% block content %}
<div class="container mt-5">
    <h1 class="mb-4">{{ post.title }}</h1>
    <p class="text-muted">Published on {{ post.publish|date:"F j, Y" }} by {{ post.author }}</p>
    <div class="content">
        {{ post.content|safe }}
    </div>
</div>
{% endblock %}
EOL

# Create about.html
cat <<EOL > templates/about.html
{% extends "blog/base.html" %}

{% block content %}
<div class="container mt-5">
    <h1>About Us</h1>
    <p>Welcome to our blog! We are passionate about sharing insightful articles on various topics. Our team of writers is dedicated to providing high-quality content to our readers.</p>
    <p>Stay tuned for more updates and feel free to reach out to us through our contact page.</p>
</div>
{% endblock %}
EOL

# Create contact.html
cat <<EOL > templates/contact.html
{% extends "blog/base.html" %}

{% block content %}
<div class="container mt-5">
    <h1>Contact Us</h1>
    <form method="post" action="{% url 'blog:contact' %}">
        {% csrf_token %}
        <div class="mb-3">
            <label for="name" class="form-label">Name</label>
            <input type="text" class="form-control" id="name" name="name" required>
        </div>
        <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" id="email" name="email" required>
        </div>
        <div class="mb-3">
            <label for="message" class="form-label">Message</label>
            <textarea class="form-control" id="message" name="message" rows="5" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Send</button>
    </form>
</div>
{% endblock %}
EOL

echo "All files have been created successfully."
