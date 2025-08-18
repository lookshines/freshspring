from .models import ContactInformation

def latest_contact(request):
    contact = ContactInformation.objects.order_by('-id').first()
    phone = contact.phone if contact else ''
    whatsapp = contact.whatsapp if contact else ''
    
    formated_phone = f"{phone[:3]} ({phone[3:6]}) {phone[6:9]} {phone[-4:]}" if phone else ''
    formated_whatsapp = f"{whatsapp[:3]} ({whatsapp[3:6]}) {phone[6:9]} {phone[-4:]}" if whatsapp else ''
    
    return {
        'contact': contact,
        'formated_phone': formated_phone,
        'formated_whatsapp': formated_whatsapp,
    }