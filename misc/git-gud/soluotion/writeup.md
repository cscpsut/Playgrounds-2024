### git gud 

## Soluotion:
You are given a zip file that contains a web app and other files; one of the files/folders is a.git folder.
When there is a `.git` folder, then we can check for a git log to see if there is anything interesting we can use. 

When you run `git log`, you will notice a commit message with the following:

`oops, this file was added by mistake. Must delete it now.`

indicating a file was deleted; based on this, you need to find a way to retrieve this deleted file:

One way to do this is to `revert` the action:

```git revert --no-commit <commit>```

then a new file will show up with the name `secret.zip`

but its password protected

lets check other commits:
```git log```

There will be another commit message about a password:

`These new interns are ignorant. Who puts a password in a config file???`

If we check it, we will notice that there was a password:
you can check the content of a commit using:

```git show <commit>```

after running the command we will find a password:

![image](https://github.com/user-attachments/assets/ba44fe1b-4255-4176-82fc-a66b8169203b)

password: `putTheseFoolishAmbitionsToRest`
 
lets take the password and try open the zip file with it:


![image](https://github.com/user-attachments/assets/ce057da1-8a4a-4f9f-804d-e83b3d14c4af)

flag: `PlaygroundsCTF{n07_b4d_k1d}`
