Start decompiling the code we can see these: 
```java

    private final native boolean checkInput(String str);

    static {
        System.loadLibrary("yemenionyx");
    }
```

so the function checkInput is being called from the library yemenionyx. 

start running this command:
```bash 
$ apktool d yemenionyx.apk
```

and then go to the lib directory we can see the library there. Decompiliong that file using ghidra we can see that it performs xor with our input and check it against a ciphertext. 

https://gchq.github.io/CyberChef/#recipe=Swap_endianness('Hex',16,true)From_Hex('Auto')XOR(%7B'option':'Hex','string':'d1'%7D,'Standard',false)&input=OTVBQTk3ODU5MkEyQjVCRkE0QkVBM0I2QThCMEJEODEKOEVBNUIwQjlFNjhFQTZFMUJGOUE4RUE0RTFBODhFRTEKRTJBODhFQkZBM0E0QjM4RUE1QkZFNUIyOEVBNEUxQTgKMDAwMDAwMDAwMDAwYWM4OTg4OWZlMThlYjhiZmUyYmM&oeol=CR