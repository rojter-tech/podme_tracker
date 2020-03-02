from utils import *

driver = establish_connection()
wait_for_access(driver, MY_PODCASTS, timer=20).click()
wait_for_access(driver, FOOTER, timer=20).click()

pod_dict = {}
pod_ids = []
pod_names = []
pod_urls = []

for podelement in driver.find_elements_by_tag_name('a'):
    if podelement.get_attribute('class') == 'pod-item':
        image_element=podelement.find_element_by_tag_name('img')

        name = image_element.get_attribute('alt')
        url = podelement.get_attribute('href')
        pod_id = url.split('/')[-1]

        pod_names.append(name)
        pod_urls.append(url)
        pod_ids.append(pod_id)
        

for pod_id, pod_name, pod_url in zip(pod_ids, pod_names, pod_urls):
    pod_dict[pod_id] = {'name': pod_name, 'url': pod_url}


store_dict_as_json(pod_dict, os.path.join('data', 'pods.json'))