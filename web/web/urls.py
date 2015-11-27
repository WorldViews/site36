from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello, about, entry

blog_urls = [
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/',  include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    url(r'^blog/random/', include('zinnia.urls.random')),
    url(r'^blog/authors/', include('zinnia.urls.authors')),
    url(r'^blog/categories/', include('zinnia.urls.categories')),
    url(r'^blog/comments/', include('zinnia.urls.comments')),
    url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    url(r'^blog/', include('zinnia.urls.shortlink')),
    url(r'^blog/', include('zinnia.urls.quick_entry'))
]

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/', hello),
#    url(r'^about/', 'Registry.views.about', name='about'),
    url(r'^about/', about),
    url(r'^$', entry),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(blog_urls, namespace='zinnia')),
)
