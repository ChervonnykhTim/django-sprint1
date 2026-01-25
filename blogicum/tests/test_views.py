def test_blog_posts(posts):
    try:
        from blog.views import posts as solution_posts
    except Exception as err:
        raise AssertionError(
            'При импорте списка `posts` из файла `blog/views.py` '
            f'произошла ошибка: {err}') from err
    assert solution_posts == posts, (
        'Убедитесь, что список с постами `posts` из файла `blog/views.py` '
        'соответствуют списку из задания.')
