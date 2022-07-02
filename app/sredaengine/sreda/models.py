from datetime import date

from django.contrib.auth import get_user_model
from django.db import models
from django.urls  import reverse
from django.utils.text import slugify
from transliterate import translit
from ckeditor.fields import RichTextField

User = get_user_model()


def gen_slug(s, with_date=True):
    try:
        new_slug = slugify(translit(s, reversed=True))
    except:
        new_slug = slugify(s)
    if with_date:
        return new_slug + '-' + str(date.today())
    else:
        return new_slug

class Content(models.Model):
    on_main = models.BooleanField(default=False)



class Post(models.Model):
    header_image = models.ImageField(null=True, blank=True, max_length=300, upload_to='images/')
    type_content = models.ForeignKey('TypeContent', blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    community = models.ForeignKey('Community', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_pub = models.DateTimeField(auto_now_add=True)
    topics = models.ManyToManyField('Topic', blank=True, related_name='posts')
    body = RichTextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=250, blank=True, unique=True)
    on_main = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "1. Посты"
        ordering = ['-rating']
    
    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # def __str__(self):
    #     return self.title + ' | ' + str(self.author)


class Questions(models.Model):
    header_image = models.ImageField(null=True, blank=True, max_length=300, upload_to='images/')
    type_content = models.ForeignKey('TypeContent', blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    topics = models.ManyToManyField('Topic', blank=True, related_name='question')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "2. Вопросы"

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author.first_name)+ ' ' + str(self.author.last_name)


class Answer(models.Model):
    question = models.ForeignKey('Questions', on_delete=models.CASCADE, related_name='answer')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = RichTextField(min_length=280, db_index=True)
    body = models.TextField(db_index=True)

    class Meta:
        verbose_name_plural = "3. Ответы"

    def __str__(self):
        return self.body[:25] + ' | ' + str(self.author.first_name)+ ' ' + str(self.author.last_name)




class Topic(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "4. Рубрики"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title, with_date=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Community(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    pic = models.ImageField(max_length=300, upload_to='images/')

    class Meta:
        verbose_name_plural = "5. Сообщества"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title, with_date=False)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class TypeContent(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "6. Тип контента"

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=150, unique=True)
    profile_pic = models.ImageField(max_length=300, upload_to='images/')

    class Meta:
        verbose_name_plural = "7. Профиль"
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #     super().save(*args, **kwargs)
    