from reviews.models import Review
from rest_framework import generics
from reviews.serializers import ReviewSerializers

class  ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class ReviewRetrivierDestroyUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
