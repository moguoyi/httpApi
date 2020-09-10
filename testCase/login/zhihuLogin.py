# coding:utf-8
import requests


# session管理
session = requests.session()

# 添加信息头headers
session.headers["content-type"] = "application/x-www-form-urlencoded"
session.headers["user-agent"] = "(Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 " \
                                "(KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
session.headers["x-zse-83"] = "3_2.0"

# 请求授权
result = session.post(url="https://www.zhihu.com/udid")
print(result.text)

# 验证码接口
result = session.get(url="https://www.zhihu.com/api/v3/oauth/captcha?lang=en")
print(result.text)

# 发送请求
result = session.post(url="https://www.zhihu.com/api/v3/oauth/sign_in",
                      data="KbOG-ge8UBXxcTYq8LkM39L1e9oY2BH0sTYqk4R92Ltxg_pKzbN924U0g6S_EGO1BBH"
                           "0c79hJvOfELp1tUNKEecGoBXxcTYhAhYqk4__2Ltxg0pMK9p1sUCBi9V9XqYhzqNMcCe"
                           "MsBSYkBF0z_e0g4e8kCV92vCmKC3qk47mF9LxgMNmZrNqk4R92LkfiqxG1wS8S79hSLFp"
                           "2TY0YGOmXg9hHhV9oqoMZu3qk4QqQLYpk720mLtyrQuyPh2pkLP9BLfBJJHmkCOOcBF0zX"
                           "28o6Xy2X2Yc828yu20eQuBe8YfQTFq1LxB26U0HhFXk7YBZBS06eu92LkYkCpGZbSBDggqkL"
                           "PfgG3ZsUO1iugZJvOfXqYhzqNMcCeMST2teTFqmXYqeHrqkH2pr_e0zRVmUbcMgcS_eBF0z_NM"
                           "-ccM2wNOXqYhzuVKeCpGEwxO3BF0zRF0gDUqr02YrXNqzgY827XyNqFp6XY8M828oQLBFqYfXqY"
                           "hygSVe9LBDrOf: ")
print(result.text)


# 查询用户信息

result = session.get(url="https://www.zhihu.com/api/v4/me?include=ad"
                         "_type%2Cavailable_message_types%2Cdefault"
                         "_notifications_count%2Cfollow_notifications_count%2Cvote_t")

print(result.text)
