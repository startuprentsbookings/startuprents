<h1>Post Overview</h1>
{% for post in post_list %}
  <h2><a href="{% url post_detail post.id %}">{{ post.title }}</a></h2>
  <p>
    {{ post.date }} |
    {{ post.comments|length }} comments |
    tagged {{ post.tags|join:', ' }}
  </p>
{% endfor %}
