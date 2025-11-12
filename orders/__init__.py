PENDING='Pending'
PROCESSING='Processing'
COMPLETED='Complted'
CANCELLED='Cancelled'

OrderStatus.objects.get_or_create(name=PENDING)
OrderStatus.objects.get_or_create(name=PROCESSING)
OrderStatus.objects.get_or_create(name=COMPLETED)
OrderStatus.objects.get_or_create(name=CANCELLED)