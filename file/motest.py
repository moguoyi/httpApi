import jpype


jvmPath = jpype.getDefaultJVMPath()           #the path of jvm.dll
classpath = "/Users/moguoyi/pyStudy/httpApi/file"                 #the path of PasswordCipher.class
jvmArg = "-Djava.class.path=" + classpath
if not jpype.isJVMStarted():                    #test whether the JVM is started
    jpype.startJVM(jvmPath,jvmArg)             #start JVM
javaClass = jpype.JClass("Yit.class")   #create the Java class
ncryptedString = javaClass.moAdd(1,3)
print(ncryptedString)
jpype.shutdownJVM()        #shut down JVM
