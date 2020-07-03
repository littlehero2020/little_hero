from announcement.models import Post
from enum import Enum


#enum for site domain
class domain_of_url(Enum) :
    ILSAM65 = 1
    VMS = 2


# data type must be dictionary.
def push_data(data) : 
    try :
        temp = Post.objects.get(
            site_domain=data['site_domain'],
            regist_no=data['regist_no']
            )
        ## update
        if temp.recruit_status != data['recruit_status'] :
            temp.recruit_status = data['recruit_status']
            temp.save()
            print('1365 ' + str(data['regist_no']) +' has updated.')
    ## push
    except : 
        Post(
                site_domain=data['site_domain'],
                regist_no=data['regist_no'],
                title=data['title'],
                recruit_status=data['recruit_status'],
                adult_status=data['adult_status'],
                domain=data['domain'],
                text=data['text'],
                do_date=data['do_date'],
                do_date_extra=data['do_date_extra'],
                recruit_member=data['recruit_member'],
                recruit_company=data['recruit_company'],
                telephone=data['telephone'],
                address_city=data['address_city'],
                address_gu=data['address_gu'],
                address_remainder=data['address_remainder'],
                url=data['url']
            ).save()
        print(str(data['regist_no']) +' has pushed.')

