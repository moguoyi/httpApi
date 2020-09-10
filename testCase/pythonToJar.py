import jpype
import time

# java虚拟机的路径
#  jvmPath = r"C:\Program Files (x86)\Java\jre8\bin\server\jvm.dll"
jvmPath = jpype.getDefaultJVMPath()


print(jvmPath)
# 所有调用的方法的绝对路径
ext_classpath = r"/Users/moguoyi/pyStudy/httpApi/file/moyitestMaven.jar"
#
# # 启动虚拟机
# jpype.startJVM(jvmPath)
# # 判断虚拟机是否启动
# print(jpype.isJVMStarted())
# # 调用java程序，执行打印
# jpype.java.lang.System.out.println("hello JPype !")
# # 关闭虚拟机
# jpype.shutdownJVM()
# time.sleep(5)
# print(jpype.isJVMStarted())


# 启动虚拟机
jpype.startJVM(jvmPath, 'ea', '-Djava.class.path=%s' % ext_classpath)     # 启动虚拟机
JPackage = jpype.JPackage('mo.yo')
difference = JPackage.MoyiAdd.moAdd(5, 1)
print(difference)
jpype.shutdownJVM()  # 关闭虚拟机