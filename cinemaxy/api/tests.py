from django.test import TestCase
from .models import Genre
# Create your tests here.




class GenreTest(TestCase):
    def test_genre_model_exists(self):
        genres = Genre.objects.all()
        self.assertEqual(genres.count(), 0)
        print("Test passed for object creation")
        genre = Genre.objects.create(name="Action")
        self.assertEqual(genre.name, "Action")
        self.assertEqual(genre.description, "")
        self.assertEqual(genres.count(), 1)
        genre.description = "Action movies"
        genre.save()
        self.assertEqual(genre.description, "Action movies")
        genre.delete()
        self.assertEqual(genres.count(), 0)
    def test_genre_object_breaking(self):
        genre = Genre.objects.create(name="")
        self.assertEqual(genre.name, "")
        self.assertEqual(genre.description, "")
        genre.name = "Comedy"
        genre.save()
        self.assertEqual(genre.name, "Comedy")
        genre.delete()
        self.assertEqual(Genre.objects.all().count(), 0)
class MovieTypeTest(TestCase):
    pass

class CinemaTest(TestCase):
    pass

class CinemaRoomTest(TestCase):
    pass

class MovieTest(TestCase):
    pass

class ShowdayTest(TestCase):
    pass

class CustomerTest(TestCase):
    pass

class TicketTest(TestCase):
    pass

class DiscountTest(TestCase):
    pass

class VerifierDeviceTypeTest(TestCase):
    pass

class VerifierTest(TestCase):
    pass

class TakeTicketTest(TestCase):
    pass

class VerifyTicketTest(TestCase):
    pass

class TransferUnusedTicketTest(TestCase):
    pass

class PickSeatNumberTest(TestCase):
    pass

class GetSHowingMoviesTest(TestCase):
    pass

class NotifyDiscountTest(TestCase):
    pass

class GiveOfferTest(TestCase):
    pass

class VerifyCustomerOfferTest(TestCase):
    pass

class HandleFailedNotificationTest(TestCase):
    pass

class ResendFailedNotificationTest(TestCase):
    pass

class UpdateForBookingTest(TestCase):
    pass

