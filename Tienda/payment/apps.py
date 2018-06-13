from django.apps import AppConfig


class PaymentConfig(AppConfig):
	name = 'Tienda.payment'
	verbose_name = 'Tienda.Payment'

	def ready(self):
		# import signal handlers
		import Tienda.payment.signals
