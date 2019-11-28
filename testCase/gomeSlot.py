import requests
from locust import HttpLocust, TaskSet, task

class gomeSlot(TaskSet):
    header={"accept":"application/json, text/javascript, */*; q=0.01",
            "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Mobile Safari/537.36"}
    @task
    def mo(self):
        # url="https://sault.gome.com.cn/v1/cms/slot?unique_key=marketsocial"
        self.client.get("/v1/cms/slot?unique_key=marketsocia",headers=self.header)   #访问的接口
        # p
        # rint(result)

class UserOne(HttpLocust):
    task_set = gomeSlot
    weight = 1
    min_wait = 1000
    max_wait = 3000
    stop_timeout = 5
    host = "https://sault.gome.com.cn"

#     在终端中用可以通过命令执行locust -f gomeSlot.py UserOne 启动 在浏览器中http://127.0.0.1:8089访问web ui进行运行


# if __name__=="__main__":
#     gomeSlot.mo()