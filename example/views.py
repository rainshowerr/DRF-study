from rest_framework import viewsets, permissions, status, mixins, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer


# Create your views here.

@api_view(['GET']) # 데코레이터
def HelloAPI(request):
	return Response("Hello world!")

# 함수형 뷰
# 모든 책 정보를 넘겨주는 API & 새로운 책 포스팅 API
# /book/ 주소를 사용할 두 API에 대한 처리는 한 함수에서 한번에 처리
@api_view(['GET', 'POST'])
def booksAPI(request):
	if request.method == 'GET':
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True) # many=True : 전체 데이터 한번에 집어넣기
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 책 한 권 정보를 넘겨주는 API
@api_view(['GET'])
def bookAPI(request, bid):
	book = get_object_or_404(Book, bid=bid)
	serializer = BookSerializer(book)
	return Response(serializer.data, status=status.HTTP_200_OK)


# 클래스형 뷰
# get, post 함수를 따로 정의해서 데코레이터와 조건문이 필요없다는 게 장점
class BooksAPI(APIView):
	def get(self, request):
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request):
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
class BookAPI(APIView):
	def get(self, request, bid):
		book = get_object_or_404(Book, bid=bid)
		serilizer = BookSerializer(book)
		return Response(serilizer.data, status=status.HTTP_200_OK)
	
# mixins 활용
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class BookAPIMixins(mixins.RetrieveModelMixin, generics.GenericAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	lookup_field = 'bid'

	# 정보 불러오기
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs) # retrieve: 한개 정보를 가져옴
	# 수정
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	# 삭제
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
	
# generic 활용
class BooksAPIGenerics(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	lookup_field = 'bid'

# viewset 활용
class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer