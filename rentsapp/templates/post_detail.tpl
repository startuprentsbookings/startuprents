<h1>{{ post.title }}</h1>
<p>{{ post.date }}</p>
<p>{{ post.body }}<p>
<h2>Comments</h2>
{% for comment in post.comments %}
  <h3>{{ comment.name }} <small>on {{ comment.email }}</small></h3>
  {{ comment.body }}
{% endfor %}