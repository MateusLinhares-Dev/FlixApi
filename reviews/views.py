from reviews.models import Review
from rest_framework import generics
from reviews.serializers import ReviewSerializers
from rest_framework.permissions import IsAuthenticated

class  ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class ReviewRetrivierDestroyUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
