from django.views import View
from .models import BookInfo
from django.http import JsonResponse
import json


class BooksView(View):

    def get(self, request):
        books = BookInfo.objects.all()

        book_list = []

        for book in books:
            book_list.append({
                "btitle": book.btitle,
                "bread": book.bread,
                "bpub_data": book.bpub_date.strftime("%Y~%m~%d"),
            })

        return JsonResponse(book_list, safe=False)

    def post(self, request):

        json_data = json.loads(request.body.decode())
        print(json_data)
        book = BookInfo(**json_data)
        book.save()

        book_list = []

        books = BookInfo.objects.all()

        for book in books:
            book_list.append({
                "btitle": book.btitle,
                "bread": book.bread,
                "bpub_data": book.bpub_date.strftime("%Y__%m__%d"),
            })

        return JsonResponse(book_list, safe=False)


class ChangeView(View):

    def put(self, request, id):

        try:
            book = BookInfo.objects.get(id=id)

        except BookInfo.DoesNotExist:
            return JsonResponse({"error": 404})
        try:
            book.btitle = request.GET.get("btitle")
        except:
            pass

        book.save()
        return JsonResponse({
            "btitle": book.btitle,
            "bread": book.bread,
            "bpub_data": book.bpub_date
        })

    def delete(self, request, id):

        try:
            book = BookInfo.objects.get(id=id)

        except BookInfo.DoesNotExist:
            return JsonResponse({"error": 404})
        book.save()
        BookInfo.delete(book)

        return JsonResponse({}, status=200)
