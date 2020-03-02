from utils import *

GET_MP3_URL = re.compile(r'.*(\.mp3)')

def get_content_url(episode):
    global urls
    del driver.requests
    driver.get(PODME_URL+"?episode="+episode)
    for request in driver.requests:
        if request.response:
            request_path = request.path
            if GET_MP3_URL.match(str(request_path)):
                print('url found:', request_path)
                urls.append(request_path)
                del driver.requests
                break


urls = []
driver = establish_connection()
get_content_url('221266')
get_content_url('221592')
driver.close()


print(urls)