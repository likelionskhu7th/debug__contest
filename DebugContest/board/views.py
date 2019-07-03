from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import BoardForm,HashtagForm, CommentForm
from models import Board,Hashtag, Comment

# Create your views here.

def board(request):
    boards = Board.objects
    return render(request, 'board/board.html', {'boards': boards})

#글작성
def create(request):
    return render(request, 'board/create.html')

#boardform
def boardform(request, board=None):
    if request.method == 'POST':
        form=BoardForm(request.POST,request.FILES,instance=board)
        if form.is_valid():
            board=form.save(commit=False)
            board.pub_date=timezone.now()
            board.save()
            form.save_m2m()
            return render('board')
        else:
            form =boardform(instance=board)
            return render(request, 'board/create.html',{'form':form})
#게시글 수정하기
def edit(request,pk):
    board=get_object_or_404(Board,pk=pk)
    return boardform(request,board)

#게시글 삭제하기
def remove(request,pk):
    board=get_object_or_404(Board,pk=pk)
    board.delete()
    return redirect('board')

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 댓글 삭제
def comment_remove(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    board = comment.board
    comment.delete()
    return redirect("detail", board.pk)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

#hashtagform
def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, request.FILES,instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'board/hashtag.html', {'form': form, "error_message": error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
                return redirect('board')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'board/hashtag.html', {'form': form})

def detail(request,pk):
    board_detail = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board_detail
            comment.save()
            return redirect("detail", pk)
    else:
        form = CommentForm()
        return render(request, 'board/detail.html', {'board': board_detail}, {"form": form})
