from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from api.services import check_ownership, ownership_required
from .serializers import *
from .models import Article
from .services import *


class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request: Request):
        article_data = request.data
        article_data['user'] = request.user.id

        serializer = ArticleCreateSerializer(data=article_data)
        if serializer.is_valid():
            self.perform_create(serializer)
            #data instead of validated_data, because validated_data returns user as an object
            #Also no need for message field lmao
            return Response({'message': 'Created an article successfully!', **serializer.data}, status=201)
        else:
            return Response({'message': serializer.errors}, status=400)

    def get(self, request: Request, id: int): 
        #Ok, so this shit somehow works only with BaseManager instances
        article_obj = self.queryset.filter(pk=id) 
        if article_obj.count() == 0:
            #this line is straight up stolen lmao
            raise Http404("No %s matches the given query." % self.queryset.model._meta.object_name)
        
        serializer = ArticleURDGetSerializer(
            article_obj, #welp, yeah
            custom_kwargs={ "request_user": request.user },
            many=True
        )

        #only 1 object, so it's ok
        #if there is somehow more than 1 objs with the same pk, well...
        return Response(serializer.data[0], status=200) 
    
    def list(self, request: Request):
        serializer = ArticleListSerializer(self.queryset.filter(is_published=True), many=True) #boilerplate
        return Response(serializer.data, status=200)
            
    #object already exists (can't access /article/edit if it doesn't), so no need tto do checks
    @ownership_required()
    def save_block(self, request: Request, id: int, *args, **kwargs): 
        block_id = int(request.data.get('block_id'))
        block = request.data.get('block')

        article_obj = kwargs.get('sel_obj')
        service = ArticleBlockService(article_obj)
        if service.is_valid_block(block):
            block["content"] = ArticleBlockService.purify_content(block["content"])
            service.modify_block(block_id, block)
            return Response({"block_id": block_id, "block": block}, status=200) 
        else:
            return Response({"message": "Invalid JSON schema!"}, status=400)
        
    @ownership_required()
    def delete_block(self, request: Request, id: int, *args, **kwargs): 
        block_id = int(request.data.get('block_id'))

        article_obj = kwargs.get('sel_obj')
        service = ArticleBlockService(article_obj)
        try:
            block = service.pop_block(block_id)
        except ArticleBlockError as e:
            return Response({"message": str(e)}, status=400)
        else:
            return Response({"message": "Deleted block successfully!"}, status=200)
        
    @ownership_required()
    def reposition_block(self, request: Request, id: int, *args, **kwargs):
        initial_pos = int(request.data.get('initial_pos'))
        final_pos = int(request.data.get('final_pos'))

        article_obj = kwargs.get("sel_obj")
        service = ArticleBlockService(article_obj)
        try:
            block = service.pop_block(initial_pos)
            service.insert_block(final_pos, block)
        except ArticleBlockError as e:
            return Response({"message": str(e)}, status=400)
        else:
            return Response({"message": "Swapped block successfully!"}, status=200) 

    #save & set is_published = True
    @ownership_required()
    def publish(self, request: Request, id: int, *args, **kwargs):
        publish_status: bool = request.data.get('publish_status')

        article_obj = kwargs.get('sel_obj')
        serializer = ArticleCreateSerializer(
            article_obj,
            data={
                'is_published': publish_status,
            },
            partial=True
        ) 
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Published successfully!'}, status=200)
        else:
            return Response({"message": serializer.errors}, status=400) #idk what code to choose lmao, TODO: errors handling