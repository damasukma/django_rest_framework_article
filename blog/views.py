from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


from .models import Category
from .serializers import CategorySerializer


class ListCategories(APIView):

    parser_classes = [JSONParser]

    def get(self, request, **kwargs):

        category = Category.objects.all()

        serializer = CategorySerializer(category, many=True)
        return Response({
            'data': serializer.data
    })


    def post(self, request, format=None, **kwargs):
        """
            request form post
        """
        message = {
            'status': 'failed',
            'message': 'error'
        }

        category_form = request.data

        serializer = CategorySerializer(data=category_form)

        if serializer.is_valid(raise_exception=True):
           category_save = serializer.save()

           message.update({
                'status': 'success',
                'message': "Add {} succesfully".format(category_save)
           })
        return Response(message)


class CategoryDetailView(APIView):

    parser_classes = [JSONParser]

    """

              For GET With APIView


    """

    def get(self, request, pk, **kwargs):

        message = {
            'status': status.HTTP_202_ACCEPTED,
            'data': None
        }

        try:

            category_detail = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category_detail)

            message.update({
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })

            return Response(message)
        except Category.DoesNotExist:

            message.update({
                'status': status.HTTP_404_NOT_FOUND,
                'data': serializer.errors
            })

        return Response(message)
    """
    
    
        For PUT APIView
                    
    """

    def put(self, request, pk, **kwargs):

        message = {
            'status': status.HTTP_202_ACCEPTED,
            'message': None
        }

        try:

            category_by_id = Category.objects.get(pk=pk)
            data = request.data
            serializer = CategorySerializer(instance=category_by_id, data=data, partial=True)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message.update({
                    'status': status.HTTP_200_OK,
                    'message': 'Update data successfully'
                })

        except Category.DoesNotExist:
            message.update({
                'status': status.HTTP_404_NOT_FOUND,
                'message': serializer.errors
            })
        return Response(message)

    """
          
          For Delete With APIView
                
            
    """

    def delete(self, request, pk, **kwargs):

        message = {
            'status': status.HTTP_202_ACCEPTED,
            'message': None
        }

        try:

            category = Category.objects.get(pk=pk)
            category.delete()

            message.update({
                'status': status.HTTP_200_OK,
                'message': 'success'
            })

        except Category.DoesNotExist:

            message.update({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'error'
            })

        return Response(message)