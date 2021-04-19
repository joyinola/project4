from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Posts,User,Follows,Like
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from .models import User
def like(request,post_id):
    user=User.objects.get(username=request.user)
    # like_filter=Like.objects.filter(Post=post_id,User=user)
    post_instance=Posts.objects.get(id=post_id)
    like_filter=Like.objects.filter(Post=post_instance,User=user)
    if not like_filter:
       
        Like.objects.create(Post=post_instance,User=user)
        like=Like.objects.filter(Post=post_instance).all().count()
        text='Unlike'
        #return JsonResponse({'like':like})
    else:
        like_filter.delete()
        like=Like.objects.filter(Post=post_instance).all().count()
        text='Like'  
    return JsonResponse({'like':like, 'text':text})
def edit(request, post_id):
    post=Posts.objects.get(id=post_id)
    if request.method=="POST":
        try:
            request.FILES['myfile']
            myfile = request.FILES['myfile']
            fs = FileSystemStorage(location='media/Post_img', base_url='Post_img')
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            caption=request.POST['Caption']
            #post.User=request.user
            post.Img=uploaded_file_url
            post.Caption=caption
            post.save()
            #post=Posts.objects.create(User=request.user, Img=uploaded_file_url, Caption=caption)
            return HttpResponseRedirect(reverse(index))
        except MultiValueDictKeyError:


            #post.delete()
            caption=request.POST['Caption']
            post.Caption=caption
            #Posts.objects.create(User=request.user, Caption=caption)
            return HttpResponseRedirect(reverse(index))
    else:
        return render(request,'network/edit.html',{'post':post})
            
def Follow(request, user):
    User_=User.objects.get(username=request.user)
    profile=User.objects.get(username=user)
    Follows_related=Follows.objects.filter(Follower=User_.id).filter(User_involved=profile.id)
    #return HttpResponse(Follows.objects.filter(Follower=User_.id))
    if not Follows.objects.filter(Follower=User_.id):
        new_follow=Follows.objects.create(User_involved=profile,Follower=User_)
        person_followed=User.objects.get(username=profile)
        person_followed.Follower+=1
        person_followed.save()
        person_who_followed=User.objects.get(username=User_)
        person_who_followed.Following+=1
        person_who_followed.save()
        #return HttpResponse('here')
    else:
        for i in Follows.objects.filter(Follower=User_.id):
            
            if profile.id!=i.User_involved.id:
                new_follow=Follows.objects.create(User_involved=profile,Follower=User_)
                person_followed=User.objects.get(username=profile)
                person_followed.Follower+=1
                person_followed.save()
                person_who_followed=User.objects.get(username=User_)
                person_who_followed.Following+=1
                person_who_followed.save()
                
            else:
                User_.Following-=1
                User_.save()
                profile.Follower-=1
                profile.save()
                
                Follows.objects.filter(Follower=User_.id).filter(User_involved=profile.id).delete()
   
    return HttpResponseRedirect(reverse(Profile,args=(user,)))
def new_post(request):
    if request.method=='POST': 
        try:
            request.FILES['file']
            myfile = request.FILES['file']
            fs = FileSystemStorage(location='media/Post_img',base_url='Post_img')
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            caption=request.POST['Caption']
            post=Posts.objects.create(User=request.user, Img=uploaded_file_url, Caption=caption)
            return HttpResponseRedirect(reverse('index'))
        except MultiValueDictKeyError:
            caption=request.POST['Caption']
            post=Posts.objects.create(User=request.user, Caption=caption)
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'network/new.html')
def Profile(request, user_profile):
    user=User.objects.get(username=user_profile)
    user_accessing_page=User.objects.get(username=request.user)
    
    state=False
    logged=False
    like=[]
    likes=Like.objects.filter(User=user_accessing_page)
    for i in likes:
        like.append(i.Post)
    Following_no=user.Following
    Followers_no=user.Follower
    User_=User.objects.get(username=request.user)
   
    Followers=Follows.objects.filter(User_involved=user)
    for i in Followers:
        follower=User.objects.get(id=i.Follower.id)
        if User_.username==follower.username:
            state= True
            break
    #return HttpResponse(state)
    if User_.username == user.username:
        logged=True

    all_posts=Posts.objects.filter(User=user).order_by('-Timestamp')
    count=all_posts.count()
    paginator=Paginator(all_posts,5)
    # return HttpResponse(paginator.page(1))
    try:
        page=paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        page=paginator.page(1)
    except EmptyPage:
        page=paginator.page(paginator.num_pages)
    # return HttpResponse(page)
    return render(request, 'network/profile.html', {'profile':user,'page':page,
        'like':like,'state':state,'posts':all_posts,'following':Following_no,
        'paginator': paginator,'count':count,'followers':Followers_no,'logged':logged})
def following(request):
    posts=[]
    user=User.objects.get(username=request.user)
    following=Follows.objects.filter(Follower=user)
    for i in following:
        post_of_following=Posts.objects.filter(User=i.User_involved)
        for j in post_of_following:
            posts.append(j)
    like=[]
    likes=Like.objects.filter(User=user)
    for i in likes:
        like.append(i.Post)
    #posts=[Posts.objects.filter(User=i.User_involved) for i in following]
    #return HttpResponse(post)
    for j in posts:
        likee=Like.objects.filter(Post=j)
        for i in likee:
            # return HttpResponse(i.User.id)
            if user.id == i.User.id:
                state=True
    paginator=Paginator(posts,5)
    try:
        page=paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        page=paginator.page(1)
    except EmptyPage:
        page=paginator.page(paginator.num_pages)
    return render(request,'network/following.html',{'page':page,'like':like})

@login_required
def index(request):

    like=[]
    posts=Posts.objects.all().order_by('-Timestamp')
    user=User.objects.get(username=request.user)
    post=Posts.objects.filter(User=user.id)
    likes=Like.objects.filter(User=user)
    for i in likes:
        like.append(i.Post)

    
    paginator=Paginator(posts,5)
    try:
        page=paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        page=paginator.page(1)
    except EmptyPage:
        page=paginator.page(paginator.num_pages)
    


    return render(request, "network/index.html", {'page':page,'like': like,'user_post':post})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        try:
            request.FILES['File']
            username = request.POST["username"]
            email = request.POST["email"]
            myfile = request.FILES['File']
            fs = FileSystemStorage(location='media/profile_pics',base_url='profile_pics')
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            #return HttpResponseRedirect(reverse('index'))
        except MultiValueDictKeyError:
            uploaded_file_url=''

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
                })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            user.profile_img=uploaded_file_url
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
