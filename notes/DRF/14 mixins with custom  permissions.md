class ProductView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

##  def get_permissions(self):
##
##      if self.request.method == 'GET':
##        return [AllowAny()]

##
##        return [IsAuthenticated()]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)