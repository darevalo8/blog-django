from django import forms
from blog.models import Post, UserProfile, Comment
from django.contrib.auth.models import User


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category')





class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'user')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'email', 'password')



class UserProfileForm(forms.ModelForm):


    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'about')


class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('commentary',)