import arrow
from django import template
from django.core.urlresolvers import reverse
from django.utils.html import mark_safe
from accounts.models import Family

register = template.Library()


@register.filter
def get_total_subject_posts(subject):
    total_posts = 0
    for thread in subject.threads.all():
        total_posts += thread.posts.count()
    return total_posts

@register.filter
def get_total_thread_posts(thread):

    return thread.posts.count()


@register.filter
def started_time(created_at):
    return arrow.get(created_at).humanize()


@register.simple_tag
def last_posted_user_name(thread):
    posts = thread.posts.all().order_by('-created_at')
    return posts[posts.count() - 1].user.username


@register.filter
def vote_percentage(subject):
    count = subject.votes.count()

    if count == 0:
        return 0

    total_votes = subject.poll.votes.count()

    return (100 / total_votes) * count


@register.simple_tag
def user_vote_button(thread, subject, user):
    vote = thread.poll.votes.filter(user_id=user.id).first()

    if not vote:
        if user.is_authenticated():
            link = """
                <div class="col-md-3 btn-vote">
                    <a href="%s" class="btn btn-default btn-sm">
                        Add my vote!
                    </a>
                </div>
                """ % reverse('cast_vote', kwargs={
                'thread_id': thread.id,
                'subject_id': subject.id
            })

            return mark_safe(link)
    return ""

@register.filter
def vote_percentage(subject):
   count = subject.votes.count()
   if count == 0:
       return 0
   total_votes = subject.poll.votes.count()
   return (100 / total_votes) * count

@register.assignment_tag
def get_poster_name(post):
    user_id = post.user.id
    all_family = Family.objects.filter(account_name_id=user_id)

    full_name = all_family[0].full_name

    return full_name