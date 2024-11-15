from django.db import models


from django.urls import reverse
class BlogAuthorModel(models.Model):
    name = models.CharField(max_length=100,verbose_name='博主姓名')
    age = models.IntegerField(verbose_name='博主年龄')
    desc = models.TextField(verbose_name='博主简介')
    class Meta:
        verbose_name='博主'
        verbose_name_plural='博主列表'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('blogauthor', args=[str(self.id)])
class BlogContentModel(models.Model):
    name = models.CharField(max_length=200,verbose_name='博文名称')
    upload_date = models.DateField(verbose_name='上传日期')
    author = models.ForeignKey(BlogAuthorModel,on_delete=models.CASCADE,verbose_name='博文作者',related_name='blogcontents')
    content = models.TextField(verbose_name='博文内容')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('blogcontent', args=[str(self.id)])
class BlogCommentModel(models.Model):
    name = models.CharField(max_length=10,verbose_name='评论者姓名')
    pub_datetime = models.DateTimeField(verbose_name='评论时间')
    comment = models.TextField(verbose_name='评论内容')
    def __str__(self):
        return self.name