from django import forms
from blog.models import Post 


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category')





class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'user')